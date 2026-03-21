# 🧠 OmniRAG — Agentic Multimodal RAG

> Upload PDFs, images, videos, and audio, then ask questions. An AI agent retrieves context from all modalities and answers with source citations.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## ✨ Features

- **📄 Multimodal Upload** — Ingest PDFs, images (PNG, JPG, JPEG), videos (MP4, MOV, AVI, MKV, WebM), and audio (MP3, WAV, OGG, FLAC, AAC, M4A)
- **🔍 Hybrid Search** — Reciprocal Rank Fusion of BM25 keyword search + semantic vector search
- **🤖 Agentic RAG** — 4-node LangGraph agent: query rewrite → retrieval → media analysis → generation
- **🖼️ Gemini Vision & Audio** — Automatically describes retrieved images, transcribes audio, and summarizes videos
- **🔄 Robust Processing** — Built-in exponential backoff retries for Google Cloud provisioning errors
- **📎 Source Citations** — Every answer cites the exact file and page used
- **✏️ Query Rewriting** — Rewrites user queries for better retrieval performance
- **🎨 Dark UI** — Premium dark-themed Streamlit interface

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone <repo-url>
cd omnirag-streamlit
pip install -r requirements.txt
```

### 2. Set up your API key

```bash
cp .env.example .env
```

Edit `.env` and add your Google API key:

```
GOOGLE_API_KEY=your_actual_key_here
```

Get a key from [Google AI Studio](https://aistudio.google.com/apikey).

### 3. Run

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## 🏗️ Architecture

OmniRAG uses a **4-node LangGraph agent** that processes every question through a deterministic pipeline:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  ✏️ Query     │ ──▶ │  🔍 Hybrid    │ ──▶ │  🖼️ Media     │ ──▶ │  ✅ Answer    │
│   Rewriting  │     │  Retrieval   │     │   Analysis   │     │  Generation  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

| Node | What it does |
|---|---|
| **Query Rewriting** | Rewrites the user query to be more specific and retrieval-friendly |
| **Hybrid Retrieval** | Runs BM25 + semantic search, fuses results with Reciprocal Rank Fusion (RRF) |
| **Media Analysis** | If images/videos/audio were retrieved, Gemini describes, transcribes, or summarizes them |
| **Answer Generation** | Generates a grounded answer from all retrieved context with source citations |

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| UI | Streamlit |
| Embeddings | Gemini Embedding 2 (`gemini-embedding-2-preview`), 1536 dims |
| Generation | Gemini 2.5 Flash (`gemini-2.5-flash`) |
| Agent Framework | LangGraph (StateGraph) |
| Vector DB | ChromaDB (local persistent) |
| PDF Parsing | pypdf |
| Image Handling | Pillow |
| Video/Audio | Gemini File API (upload → embed → describe) |
| Keyword Search | rank_bm25 (BM25Okapi) |
| Environment | python-dotenv |

---

## 💬 Example Questions

After uploading documents, try:

- *"Summarize the key findings in the uploaded report"*
- *"What does the chart on page 3 show?"*
- *"Compare the data in the image with page 5 of the PDF"*
- *"What are the main trends visible in the uploaded graph?"*
- *"Extract all numbers from the tables in my documents"*
- *"What is being discussed in the uploaded audio recording?"*
- *"Summarize the key moments from the uploaded video"*

---

## 🔬 How It Works

### Ingestion
1. **PDFs** → Parsed page-by-page with `pypdf` → each page embedded with Gemini Embedding 2 → stored in ChromaDB
2. **Images** → Converted to base64 → embedded with Gemini Embedding 2 multimodal endpoint → stored in ChromaDB
3. **Videos** → Uploaded via Gemini File API → embedded with Gemini Embedding 2 (with automatic retries for provisioning) → stored in ChromaDB
4. **Audio** → Uploaded via Gemini File API → embedded with Gemini Embedding 2 (with automatic retries for provisioning) → stored in ChromaDB

All modalities are embedded into the **same vector space**, enabling cross-modal retrieval.

### Query Processing
1. **Query Rewriting** — Gemini Flash rewrites the user query for better retrieval
2. **Hybrid Search** — Runs two searches in parallel:
   - **Semantic**: Embeds the query and finds nearest neighbors in ChromaDB
   - **BM25**: Tokenizes all documents, scores with BM25Okapi
   - **RRF Fusion**: Combines ranks with `score = 1/(rank + 60)` from both methods
3. **Media Analysis** — If image/video/audio chunks were retrieved, Gemini generates descriptions, transcriptions, or summaries
4. **Answer Generation** — All context (text + media descriptions) is fed to Gemini with a grounded generation prompt

### Storage
- **ChromaDB** persists to `./chroma_db/` — survives app restarts
- **Uploaded files** persist to `./uploads/` — needed for media re-analysis

---

## 📁 File Structure

```
omnirag-streamlit/
├── app.py              # Complete application (UI + agent + logic)
├── requirements.txt    # Python dependencies
├── .env.example        # API key template
├── .env                # Your actual API key (gitignored)
├── README.md           # This file
├── uploads/            # Uploaded files (auto-created)
└── chroma_db/          # Vector database (auto-created)
```

---

## 📝 License

MIT
