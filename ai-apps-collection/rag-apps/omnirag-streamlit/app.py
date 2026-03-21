"""
OmniRAG — Agentic Multimodal RAG
A Streamlit application that lets users upload PDFs, images, videos, and audio,
then uses a LangGraph ReAct agent with Gemini to answer questions
with source citations using hybrid search (BM25 + Semantic + RRF).
"""

import streamlit as st
from google import genai
import chromadb
import os
import uuid
import base64
import json
import mimetypes
import time
import traceback
import numpy as np
from pathlib import Path
from PIL import Image
from pypdf import PdfReader
from rank_bm25 import BM25Okapi
from dotenv import load_dotenv
from typing import TypedDict, Annotated
import operator

# ── Load environment ──────────────────────────────────────────────────────────
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=GOOGLE_API_KEY)

EMBEDDING_MODEL = "gemini-embedding-2-preview"
GENERATION_MODEL = "gemini-2.5-flash"
DIMENSIONS = 768
UPLOAD_DIR = Path("./uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

# ── Streamlit Page Config ─────────────────────────────────────────────────────
st.set_page_config(
    page_title="OmniRAG — Agentic Multimodal RAG",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ── Global ───────────────────────────────────────────── */
    .stApp {
        background-color: #0a0a0f;
        color: #e2e8f0;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    [data-testid="stSidebar"] {
        background-color: #111118;
    }
    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }

    /* ── Buttons ──────────────────────────────────────────── */
    .stButton > button {
        background: #6ee7b7 !important;
        color: #0a0a0f !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        border: none !important;
        transition: opacity 0.2s;
    }
    .stButton > button:hover {
        opacity: 0.85;
    }

    /* ── Inputs ───────────────────────────────────────────── */
    .stTextInput input, .stTextArea textarea {
        background: #1a1a24 !important;
        border: 1px solid #2a2a3a !important;
        color: #e2e8f0 !important;
        border-radius: 8px !important;
    }

    /* ── File uploader ────────────────────────────────────── */
    [data-testid="stFileUploader"] {
        background: #111118;
        border: 1px dashed #2a2a3a;
        border-radius: 10px;
        padding: 8px;
    }

    /* ── Agent step ───────────────────────────────────────── */
    .agent-step {
        border-left: 3px solid #6ee7b7;
        padding-left: 12px;
        margin: 8px 0;
    }

    /* ── Source chip ───────────────────────────────────────── */
    .source-chip {
        display: inline-block;
        background: #1a1a24;
        border: 1px solid #2a2a3a;
        border-radius: 4px;
        padding: 2px 8px;
        font-size: 12px;
        font-family: monospace;
        margin: 2px 4px;
    }

    /* ── Answer box ───────────────────────────────────────── */
    .answer-box {
        background: rgba(110,231,183,0.06);
        border: 1px solid rgba(110,231,183,0.3);
        border-radius: 10px;
        padding: 16px;
    }

    /* ── Misc overrides ───────────────────────────────────── */
    h1, h2, h3, h4, p, span, li, label, div {
        color: #e2e8f0 !important;
    }
    .stMetric [data-testid="stMetricValue"] {
        color: #6ee7b7 !important;
    }
    [data-testid="stChatInput"] textarea {
        background: #1a1a24 !important;
        border: 1px solid #2a2a3a !important;
        color: #e2e8f0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ══════════════════════════════════════════════════════════════════════════════
#  VECTOR STORE
# ══════════════════════════════════════════════════════════════════════════════
@st.cache_resource
def get_vector_store():
    """Persistent ChromaDB collection."""
    client = chromadb.PersistentClient(path="./chroma_db")
    
    # Check if dimensions match existing collection
    try:
        collection = client.get_collection(name="omnirag")
        # Test dimensionality with a dummy query or check metadata
        # Chroma doesn't store dimensionality in metadata by default in a way that's easy to check without querying
        # We can try a small query to see if it fails
        collection.query(query_embeddings=[[0.0] * DIMENSIONS], n_results=1)
    except Exception as e:
        if "does not match collection dimensionality" in str(e):
            st.warning("⚠️ Dimension mismatch detected. Recreating the knowledge base...")
            client.delete_collection(name="omnirag")
        
    collection = client.get_or_create_collection(
        name="omnirag",
        metadata={"hnsw:space": "cosine"},
    )
    return collection


# ══════════════════════════════════════════════════════════════════════════════
#  EMBEDDING HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def embed_text(text: str) -> list[float]:
    """Embed a text chunk for document storage."""
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
        config={"task_type": "RETRIEVAL_DOCUMENT", "output_dimensionality": DIMENSIONS},
    )
    return response.embeddings[0].values


def embed_query(query: str) -> list[float]:
    """Embed a query for retrieval."""
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=query,
        config={"task_type": "RETRIEVAL_QUERY", "output_dimensionality": DIMENSIONS},
    )
    return response.embeddings[0].values


def embed_image(image_path: str) -> list[float]:
    """Embed an image using Gemini multimodal embeddings."""
    img = Image.open(image_path)
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=img,
        config={"output_dimensionality": DIMENSIONS},
    )
    return response.embeddings[0].values


def _upload_media_file(file_path: str) -> str:
    """Upload a media file to Gemini File API and return its name."""
    mime_type, _ = mimetypes.guess_type(file_path)
    # ... (mime mapping logic remains similar but simplified)
    uploaded = client.files.upload(path=file_path)
    
    while uploaded.state == "PROCESSING":
        time.sleep(2)
        uploaded = client.files.get(name=uploaded.name)
    
    if uploaded.state == "FAILED":
        raise RuntimeError(f"File processing failed for {file_path}")
    return uploaded.name


def _embed_media_with_retry(file_name: str, max_retries: int = 5, initial_wait: int = 30) -> list[float]:
    """Embed a media file with retry logic."""
    from google.genai.errors import ClientError

    for attempt in range(max_retries):
        try:
            response = client.models.embed_content(
                model=EMBEDDING_MODEL,
                contents=client.files.get(name=file_name),
                config={"output_dimensionality": DIMENSIONS},
            )
            return response.embeddings[0].values
        except ClientError as e:
            if "Service agents are being provisioned" in str(e) and attempt < max_retries - 1:
                wait_time = initial_wait * (2 ** attempt)
                time.sleep(wait_time)
            else:
                raise
    raise RuntimeError("Max retries exceeded for media embedding")


def embed_video(file_path: str) -> list[float]:
    """Embed a video using Gemini multimodal embeddings via File API."""
    file_name = _upload_media_file(file_path)
    embedding = _embed_media_with_retry(file_name)
    try:
        client.files.delete(name=file_name)
    except Exception:
        pass
    return embedding


def embed_audio(file_path: str) -> list[float]:
    """Embed an audio file using Gemini multimodal embeddings via File API."""
    file_name = _upload_media_file(file_path)
    embedding = _embed_media_with_retry(file_name)
    try:
        client.files.delete(name=file_name)
    except Exception:
        pass
    return embedding


# ══════════════════════════════════════════════════════════════════════════════
#  INGESTION
# ══════════════════════════════════════════════════════════════════════════════
def ingest_pdf(file_path: str, file_id: str, filename: str) -> int:
    """Parse a PDF, embed each page, and add to ChromaDB. Returns chunk count."""
    collection = get_vector_store()
    reader = PdfReader(file_path)
    chunks_added = 0

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text or not text.strip():
            continue

        doc_id = f"{file_id}_page_{page_num}"
        # Skip if already ingested
        existing = collection.get(ids=[doc_id])
        if existing and existing["ids"]:
            continue

        embedding = embed_text(text)
        collection.add(
            ids=[doc_id],
            embeddings=[embedding],
            documents=[text],
            metadatas=[
                {
                    "file_id": file_id,
                    "filename": filename,
                    "modality": "text",
                    "page": page_num + 1,
                    "type": "pdf",
                }
            ],
        )
        chunks_added += 1

    return chunks_added


def ingest_image(file_path: str, file_id: str, filename: str) -> int:
    """Embed an image and add to ChromaDB. Returns 1."""
    collection = get_vector_store()

    # Skip if already ingested
    existing = collection.get(ids=[file_id])
    if existing and existing["ids"]:
        return 0

    embedding = embed_image(file_path)
    collection.add(
        ids=[file_id],
        embeddings=[embedding],
        documents=[f"Image file: {filename}"],
        metadatas=[
            {
                "file_id": file_id,
                "filename": filename,
                "modality": "image",
                "page": "image",
                "type": "image",
            }
        ],
    )
    return 1


def ingest_video(file_path: str, file_id: str, filename: str) -> int:
    """Embed a video and add to ChromaDB. Returns 1."""
    collection = get_vector_store()
    existing = collection.get(ids=[file_id])
    if existing and existing["ids"]:
        return 0
    embedding = embed_video(file_path)
    collection.add(
        ids=[file_id],
        embeddings=[embedding],
        documents=[f"Video file: {filename}"],
        metadatas=[{"file_id": file_id, "filename": filename, "modality": "video", "page": "video", "type": "video"}],
    )
    return 1


def ingest_audio(file_path: str, file_id: str, filename: str) -> int:
    """Embed an audio file and add to ChromaDB. Returns 1."""
    collection = get_vector_store()
    existing = collection.get(ids=[file_id])
    if existing and existing["ids"]:
        return 0
    embedding = embed_audio(file_path)
    collection.add(
        ids=[file_id],
        embeddings=[embedding],
        documents=[f"Audio file: {filename}"],
        metadatas=[{"file_id": file_id, "filename": filename, "modality": "audio", "page": "audio", "type": "audio"}],
    )
    return 1


# ══════════════════════════════════════════════════════════════════════════════
#  HYBRID SEARCH  (Semantic + BM25 + RRF)
# ══════════════════════════════════════════════════════════════════════════════
def hybrid_search(query: str, collection, n_results: int = 6) -> list[dict]:
    """
    Reciprocal Rank Fusion of semantic (vector) search and BM25 keyword search.
    Returns top-n results with {text, metadata, score}.
    """
    total_docs = collection.count()
    if total_docs == 0:
        return []

    fetch_k = min(10, total_docs)

    # ── Step 1: Semantic search ───────────────────────────────────────────
    query_embedding = embed_query(query)
    sem_results = collection.query(
        query_embeddings=[query_embedding],
        n_results=fetch_k,
        include=["documents", "metadatas", "distances"],
    )
    sem_ids = sem_results["ids"][0]
    sem_docs = sem_results["documents"][0]
    sem_metas = sem_results["metadatas"][0]

    # ── Step 2: BM25 search ───────────────────────────────────────────────
    all_data = collection.get(include=["documents", "metadatas"])
    all_ids = all_data["ids"]
    all_docs = all_data["documents"]
    all_metas = all_data["metadatas"]

    tokenized_corpus = [doc.lower().split() for doc in all_docs]
    bm25 = BM25Okapi(tokenized_corpus)
    query_tokens = query.lower().split()
    bm25_scores = bm25.get_scores(query_tokens)

    # Top-k by BM25
    bm25_top_indices = np.argsort(bm25_scores)[::-1][:fetch_k]
    bm25_ids = [all_ids[i] for i in bm25_top_indices]

    # ── Step 3: Reciprocal Rank Fusion ────────────────────────────────────
    k = 60  # RRF constant
    rrf_scores: dict[str, float] = {}
    doc_map: dict[str, dict] = {}

    # Semantic ranks
    for rank, doc_id in enumerate(sem_ids):
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + 1.0 / (rank + k)
        idx = sem_ids.index(doc_id)
        doc_map[doc_id] = {"text": sem_docs[idx], "metadata": sem_metas[idx]}

    # BM25 ranks
    for rank, doc_id in enumerate(bm25_ids):
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + 1.0 / (rank + k)
        if doc_id not in doc_map:
            idx = all_ids.index(doc_id)
            doc_map[doc_id] = {"text": all_docs[idx], "metadata": all_metas[idx]}

    # Sort by combined score
    sorted_ids = sorted(rrf_scores, key=lambda x: rrf_scores[x], reverse=True)
    n_results = min(n_results, len(sorted_ids))

    results = []
    for doc_id in sorted_ids[:n_results]:
        entry = doc_map[doc_id]
        entry["score"] = rrf_scores[doc_id]
        results.append(entry)

    return results


# ══════════════════════════════════════════════════════════════════════════════
#  GEMINI HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def describe_image_with_gemini(image_path: str) -> str:
    """Use Gemini Vision to describe an image in detail."""
    img = Image.open(image_path)
    response = client.models.generate_content(
        model=GENERATION_MODEL,
        contents=[
            "Describe this image in detail. If it contains charts, graphs, tables, or diagrams, "
            "extract all data points, labels, values, and trends visible. If it contains text, transcribe it.",
            img,
        ]
    )
    return response.text


def describe_video_with_gemini(video_path: str) -> str:
    """Use Gemini to describe a video in detail."""
    file_name = _upload_media_file(video_path)
    response = client.models.generate_content(
        model=GENERATION_MODEL,
        contents=[
            "Describe this video in detail. Include: the main subject, actions, scene changes, "
            "any text overlays, spoken dialogue or narration, data shown in charts/graphs, "
            "and any key information visible. Provide a comprehensive summary.",
            client.files.get(name=file_name),
        ]
    )
    try:
        client.files.delete(name=file_name)
    except Exception:
        pass
    return response.text


def describe_audio_with_gemini(audio_path: str) -> str:
    """Use Gemini to transcribe and describe an audio file."""
    file_name = _upload_media_file(audio_path)
    response = client.models.generate_content(
        model=GENERATION_MODEL,
        contents=[
            "Transcribe and describe this audio in detail. Include: any spoken words (full transcription), "
            "the tone and mood, background sounds, music descriptions, speaker identification if possible, "
            "and a summary of the key information conveyed.",
            client.files.get(name=file_name),
        ]
    )
    try:
        client.files.delete(name=file_name)
    except Exception:
        pass
    return response.text


def rewrite_query(query: str) -> str:
    """Rewrite query to be more retrieval-friendly."""
    response = client.models.generate_content(
        model=GENERATION_MODEL,
        contents=f"Rewrite this search query to be more specific and retrieval-friendly for a vector database. "
                 f"Return only the rewritten query, nothing else. Original query: {query}"
    )
    return response.text.strip()


# ══════════════════════════════════════════════════════════════════════════════
#  LANGGRAPH AGENT
# ══════════════════════════════════════════════════════════════════════════════
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    query: str
    rewritten_query: str
    retrieved_chunks: list[dict]
    media_descriptions: list[str]
    context: str
    answer: str
    sources: list[str]
    agent_steps: Annotated[list[dict], operator.add]


# ── Node 1: Query Rewriting ──────────────────────────────────────────────────
def rewrite_query_node(state: AgentState) -> dict:
    original = state["query"]
    rewritten = rewrite_query(original)
    return {
        "rewritten_query": rewritten,
        "agent_steps": [
            {
                "type": "rewrite",
                "icon": "✏️",
                "label": "Query Rewriting",
                "text": f"Original: {original}\nRewritten: {rewritten}",
            }
        ],
    }


# ── Node 2: Hybrid Retrieval ─────────────────────────────────────────────────
def retrieve_node(state: AgentState) -> dict:
    collection = get_vector_store()
    n = st.session_state.get("n_results", 6)
    chunks = hybrid_search(state["rewritten_query"], collection, n_results=n)

    sources = []
    for c in chunks:
        meta = c["metadata"]
        modality = meta.get("modality", "text")
        if modality in ("image", "video", "audio"):
            sources.append(f"{meta['filename']} ({modality})")
        else:
            sources.append(f"{meta['filename']} p.{meta.get('page', '?')}")

    source_list = ", ".join(sources) if sources else "None"
    return {
        "retrieved_chunks": chunks,
        "sources": sources,
        "agent_steps": [
            {
                "type": "retrieve",
                "icon": "🔍",
                "label": "Hybrid Retrieval",
                "text": f"Found {len(chunks)} chunks using BM25 + Semantic + RRF fusion\nSources: {source_list}",
            }
        ],
    }


# ── Node 3: Media Analysis (Images, Videos, Audio) ──────────────────────────
def analyze_media_node(state: AgentState) -> dict:
    media_chunks = [
        c for c in state["retrieved_chunks"]
        if c["metadata"].get("modality") in ("image", "video", "audio")
    ]

    if not media_chunks:
        return {
            "media_descriptions": [],
            "agent_steps": [
                {
                    "type": "analyze",
                    "icon": "🖼️",
                    "label": "Media Analysis",
                    "text": "No media chunks retrieved — skipping media analysis",
                }
            ],
        }

    descriptions = []
    counts: dict[str, int] = {"image": 0, "video": 0, "audio": 0}
    for chunk in media_chunks:
        file_id = chunk["metadata"]["file_id"]
        modality = chunk["metadata"]["modality"]
        found = None
        for f in UPLOAD_DIR.iterdir():
            if f.stem.startswith(file_id) or file_id in f.stem:
                found = str(f)
                break
        if found:
            if modality == "image":
                desc = describe_image_with_gemini(found)
            elif modality == "video":
                desc = describe_video_with_gemini(found)
            elif modality == "audio":
                desc = describe_audio_with_gemini(found)
            else:
                continue
            descriptions.append(desc)
            counts[modality] += 1

    parts = []
    if counts["image"]: parts.append(f"{counts['image']} image(s)")
    if counts["video"]: parts.append(f"{counts['video']} video(s)")
    if counts["audio"]: parts.append(f"{counts['audio']} audio file(s)")
    summary = ", ".join(parts) if parts else "0 media files"

    return {
        "media_descriptions": descriptions,
        "agent_steps": [
            {
                "type": "analyze",
                "icon": "🖼️",
                "label": "Media Analysis",
                "text": f"Analyzed {summary} with Gemini",
            }
        ],
    }


# ── Node 4: Answer Generation ────────────────────────────────────────────────
def generate_answer_node(state: AgentState) -> dict:
    # Build context
    context_parts = []
    for i, chunk in enumerate(state["retrieved_chunks"], 1):
        meta = chunk["metadata"]
        label = f"{meta['filename']}"
        modality = meta.get("modality", "text")
        if modality in ("image", "video", "audio"):
            label += f" ({modality})"
        else:
            label += f" p.{meta.get('page', '?')}"
        context_parts.append(f"[Source {i}: {label}]\n{chunk['text']}")

    for j, desc in enumerate(state.get("media_descriptions", []), 1):
        context_parts.append(f"[MEDIA CONTENT {j}]\n{desc}")

    context_str = "\n\n---\n\n".join(context_parts)
    chunk_count = len(state["retrieved_chunks"])

    prompt = f"""You are a helpful assistant. Answer the user's question based ONLY on the provided context.
Always cite your sources at the end.

CONTEXT:
{context_str}

USER QUESTION: {state['query']}

Instructions:
- Answer clearly and completely
- If the context includes image, video, or audio descriptions, use that information
- Cite sources as [filename, page X] or [filename, image/video/audio]
- If context doesn't contain the answer, say so clearly"""

    model = GENERATION_MODEL
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return {
        "answer": response.text,
        "context": context_str,
        "agent_steps": [
            {
                "type": "answer",
                "icon": "✅",
                "label": "Answer Generated",
                "text": f"Generated grounded answer from {chunk_count} chunks",
            }
        ],
    }


# ── Build & Cache Agent ──────────────────────────────────────────────────────
def build_agent():
    graph = StateGraph(AgentState)
    graph.add_node("rewrite", rewrite_query_node)
    graph.add_node("retrieve", retrieve_node)
    graph.add_node("analyze_media", analyze_media_node)
    graph.add_node("generate", generate_answer_node)
    graph.add_edge(START, "rewrite")
    graph.add_edge("rewrite", "retrieve")
    graph.add_edge("retrieve", "analyze_media")
    graph.add_edge("analyze_media", "generate")
    graph.add_edge("generate", END)
    return graph.compile()


@st.cache_resource
def get_agent():
    return build_agent()


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN APP
# ══════════════════════════════════════════════════════════════════════════════
def main():
    # ── Session state init ────────────────────────────────────────────────
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "uploaded_files_meta" not in st.session_state:
        st.session_state.uploaded_files_meta = []
    if "last_agent_steps" not in st.session_state:
        st.session_state.last_agent_steps = []

    # ══════════════════════════════════════════════════════════════════════
    #  SIDEBAR
    # ══════════════════════════════════════════════════════════════════════
    with st.sidebar:
        st.markdown("## 🧠 OmniRAG")
        st.caption("Agentic Multimodal RAG")
        st.divider()

        # ── Upload section ────────────────────────────────────────────────
        st.markdown("### 📁 Upload Knowledge Base")
        uploaded_files = st.file_uploader(
            "Drop PDFs, images, videos, or audio here",
            type=["pdf", "png", "jpg", "jpeg", "mp4", "mov", "avi", "mkv", "webm", "mp3", "wav", "ogg", "flac", "aac", "m4a"],
            accept_multiple_files=True,
            key="file_uploader",
        )

        if uploaded_files:
            for uf in uploaded_files:
                # Check if already processed
                already_done = any(
                    m["filename"] == uf.name for m in st.session_state.uploaded_files_meta
                )
                if already_done:
                    continue

                file_id = str(uuid.uuid4())[:12]
                ext = Path(uf.name).suffix.lower()
                save_name = f"{file_id}_{uf.name}"
                save_path = UPLOAD_DIR / save_name

                # Save to disk
                with open(save_path, "wb") as f:
                    f.write(uf.getbuffer())

                try:
                    with st.spinner(f"Ingesting **{uf.name}**..."):
                        if ext == ".pdf":
                            chunks = ingest_pdf(str(save_path), file_id, uf.name)
                            modality = "text"
                        elif ext in (".png", ".jpg", ".jpeg"):
                            chunks = ingest_image(str(save_path), file_id, uf.name)
                            modality = "image"
                        elif ext in (".mp4", ".mov", ".avi", ".mkv", ".webm"):
                            chunks = ingest_video(str(save_path), file_id, uf.name)
                            modality = "video"
                        elif ext in (".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a"):
                            chunks = ingest_audio(str(save_path), file_id, uf.name)
                            modality = "audio"
                        else:
                            st.warning(f"⚠️ Unsupported file type: {ext}")
                            continue

                    st.success(f"✅ {uf.name} — {chunks} chunk{'s' if chunks != 1 else ''} indexed")
                    st.session_state.uploaded_files_meta.append(
                        {
                            "file_id": file_id,
                            "filename": uf.name,
                            "modality": modality,
                            "chunks": chunks,
                        }
                    )
                except Exception as e:
                    st.error(f"❌ Failed to ingest {uf.name}: {e}")
                    traceback.print_exc()

        # ── Knowledge base overview ───────────────────────────────────────
        if st.session_state.uploaded_files_meta:
            st.divider()
            st.markdown("### 📚 Knowledge Base")
            total_chunks = 0
            for meta in st.session_state.uploaded_files_meta:
                icon_map = {"text": "📄", "image": "🖼️", "video": "🎬", "audio": "🎵"}
                icon = icon_map.get(meta["modality"], "📎")
                st.markdown(f"{icon} **{meta['filename']}** ({meta['modality']})")
                total_chunks += meta["chunks"]
            st.metric("Total Chunks Indexed", total_chunks)

        # ── Settings ─────────────────────────────────────────────────────
        st.divider()
        st.markdown("### ⚙️ Settings")
        st.slider("Results to retrieve", min_value=3, max_value=10, value=6, key="n_results")
        st.checkbox("Show agent reasoning steps", value=True, key="show_steps")
        st.checkbox("Show retrieved sources", value=True, key="show_sources")
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.session_state.last_agent_steps = []
            st.rerun()
        
        if st.button("🧨 Reset Knowledge Base"):
            chroma_client = chromadb.PersistentClient(path="./chroma_db")
            chroma_client.delete_collection(name="omnirag")
            st.session_state.uploaded_files_meta = []
            # Delete files from uploads
            for f in UPLOAD_DIR.iterdir():
                f.unlink()
            st.success("Knowledge base cleared. Please refresh.")
            st.rerun()

    # ══════════════════════════════════════════════════════════════════════
    #  MAIN CHAT AREA
    # ══════════════════════════════════════════════════════════════════════
    st.title("🧠 OmniRAG")
    st.caption("Agentic Multimodal RAG · Gemini Embedding 2 · Hybrid Search · LangGraph Agent")

    # ── Chat history ──────────────────────────────────────────────────────
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg["role"] == "assistant" and msg.get("sources"):
                st.caption("📎 " + " · ".join(msg["sources"]))

    # ── Empty state ───────────────────────────────────────────────────────
    if not st.session_state.uploaded_files_meta:
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(
                """
                <div style="text-align:center; padding: 60px 0;">
                    <div style="font-size:80px;">🧠</div>
                    <h2 style="color:#6ee7b7 !important;">Upload documents to get started</h2>
                    <ol style="text-align:left; max-width:400px; margin:auto; line-height:2;">
                        <li>📁 Upload PDFs, images, videos, or audio in the sidebar</li>
                        <li>💬 Ask any question about your documents</li>
                        <li>🤖 Watch the agent reason and retrieve</li>
                    </ol>
                    <br/>
                    <div style="background:#111118; border:1px solid #2a2a3a; border-radius:10px; padding:16px; text-align:left;">
                        <strong style="color:#6ee7b7 !important;">✨ Powered by Gemini Embedding 2</strong><br/>
                        Text, images, videos, and audio are embedded into a unified multimodal
                        vector space, enabling cross-modal retrieval with a single model.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        return

    # ── Chat input ────────────────────────────────────────────────────────
    query = st.chat_input("Ask anything about your documents...")

    if query:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        # Check collection has data
        collection = get_vector_store()
        if collection.count() == 0:
            st.warning("⚠️ The knowledge base is empty. Please upload documents first.")
            return

        # Run agent
        with st.chat_message("assistant"):
            with st.spinner("🤖 Agent is thinking..."):
                try:
                    agent = get_agent()
                    result = agent.invoke(
                        {
                            "query": query,
                            "rewritten_query": "",
                            "retrieved_chunks": [],
                            "media_descriptions": [],
                            "context": "",
                            "answer": "",
                            "sources": [],
                            "agent_steps": [],
                        }
                    )

                    answer = result.get("answer", "No answer generated.")
                    sources = result.get("sources", [])
                    agent_steps = result.get("agent_steps", [])

                    # Display answer
                    st.markdown(
                        f'<div class="answer-box">{answer}</div>',
                        unsafe_allow_html=True,
                    )

                    # Agent reasoning steps
                    if st.session_state.get("show_steps", True) and agent_steps:
                        with st.expander("🤖 Agent Reasoning Steps", expanded=True):
                            for step in agent_steps:
                                step_type = step.get("type", "")
                                color_map = {
                                    "rewrite": "#60a5fa",
                                    "retrieve": "#a78bfa",
                                    "analyze": "#f472b6",
                                    "answer": "#6ee7b7",
                                }
                                color = color_map.get(step_type, "#6ee7b7")
                                st.markdown(
                                    f"""<div class="agent-step" style="border-left-color:{color};">
                                        <strong>{step['icon']} {step['label']}</strong><br/>
                                        <code style="white-space:pre-wrap; font-size:13px;">{step['text']}</code>
                                    </div>""",
                                    unsafe_allow_html=True,
                                )

                    # Sources
                    if st.session_state.get("show_sources", True) and sources:
                        st.markdown("**📎 Sources**")
                        chips_html = " ".join(
                            f'<span class="source-chip">{s}</span>' for s in sources
                        )
                        st.markdown(chips_html, unsafe_allow_html=True)

                    # Persist
                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer, "sources": sources}
                    )
                    st.session_state.last_agent_steps = agent_steps

                except Exception as e:
                    error_msg = f"❌ An error occurred: {e}"
                    st.error(error_msg)
                    traceback.print_exc()
                    st.session_state.messages.append(
                        {"role": "assistant", "content": error_msg, "sources": []}
                    )


if __name__ == "__main__":
    main()
