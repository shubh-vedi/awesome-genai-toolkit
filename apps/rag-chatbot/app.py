"""
🔍 RAG Chatbot — Streamlit UI
Chat with your documents using Retrieval-Augmented Generation.
"""

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

# ── Page Config ────────────────────────────────────────────────
st.set_page_config(page_title="🔍 RAG Chatbot", page_icon="🔍", layout="wide")

# ── Styling ────────────────────────────────────────────────────
st.markdown("""
<style>
    .stApp { max-width: 1000px; margin: 0 auto; }
    .upload-section { padding: 1.5rem; border-radius: 10px; border: 2px dashed #4a4a4a; margin-bottom: 1rem; }
    .source-card { padding: 0.5rem; border-radius: 5px; background: #1e1e1e; margin: 0.3rem 0; }
</style>
""", unsafe_allow_html=True)

# ── Constants ──────────────────────────────────────────────────
CHROMA_DIR = "./chroma_db"


# ── Helper Functions ───────────────────────────────────────────
@st.cache_resource
def get_embeddings():
    return OpenAIEmbeddings(openai_api_key=st.session_state.get("api_key", os.getenv("OPENAI_API_KEY")))


def process_uploaded_files(files):
    """Process uploaded files and return document chunks."""
    documents = []
    for file in files:
        # Save temp file
        temp_path = f"/tmp/{file.name}"
        with open(temp_path, "wb") as f:
            f.write(file.getvalue())

        # Load based on type
        if file.name.endswith(".pdf"):
            loader = PyPDFLoader(temp_path)
        elif file.name.endswith(".txt"):
            loader = TextLoader(temp_path)
        else:
            st.warning(f"Skipping unsupported file: {file.name}")
            continue

        documents.extend(loader.load())
        os.remove(temp_path)

    # Split
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)
    return chunks


def create_vectorstore(chunks):
    """Create ChromaDB vector store from chunks."""
    embeddings = get_embeddings()
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )
    return vectorstore


def get_rag_chain(vectorstore):
    """Create the RAG chain."""
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3,
        openai_api_key=st.session_state.get("api_key", os.getenv("OPENAI_API_KEY")),
    )
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer",
    )
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory=memory,
        return_source_documents=True,
    )
    return chain


# ── Session State Init ─────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "chain" not in st.session_state:
    st.session_state.chain = None


# ── Sidebar ────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuration")

    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    if api_key:
        st.session_state.api_key = api_key
        os.environ["OPENAI_API_KEY"] = api_key

    st.divider()
    st.header("📄 Upload Documents")

    uploaded_files = st.file_uploader(
        "Drop your PDFs or text files here",
        type=["pdf", "txt"],
        accept_multiple_files=True,
    )

    if uploaded_files and st.button("📥 Process Documents", type="primary", use_container_width=True):
        with st.spinner("Processing documents..."):
            chunks = process_uploaded_files(uploaded_files)
            st.session_state.vectorstore = create_vectorstore(chunks)
            st.session_state.chain = get_rag_chain(st.session_state.vectorstore)
            st.success(f"✅ Processed {len(chunks)} chunks from {len(uploaded_files)} file(s)")

    if st.session_state.vectorstore:
        st.success("🟢 Vector store ready")
    else:
        st.info("🔵 Upload documents to start")

    st.divider()
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ── Main Content ───────────────────────────────────────────────
st.title("🔍 RAG Chatbot")
st.caption("Chat with your documents using Retrieval-Augmented Generation")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "sources" in msg:
            with st.expander("📚 Sources"):
                for source in msg["sources"]:
                    st.markdown(f"- `{source}`")

# Chat input
if prompt := st.chat_input("Ask a question about your documents..."):
    if not st.session_state.chain:
        st.error("⚠️ Please upload and process documents first!")
    else:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                result = st.session_state.chain.invoke({"question": prompt})
                answer = result["answer"]
                sources = list(set(
                    doc.metadata.get("source", "Unknown")
                    for doc in result.get("source_documents", [])
                ))

            st.markdown(answer)
            if sources:
                with st.expander("📚 Sources"):
                    for source in sources:
                        st.markdown(f"- `{source}`")

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "sources": sources,
        })
