# 🔍 RAG Chatbot

A conversational chatbot that answers questions from your own documents using **Retrieval-Augmented Generation (RAG)** with a **Streamlit** UI.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.3-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40-red)

## Features
- 📄 Upload PDF and TXT files via sidebar
- 💬 Chat interface with conversation memory
- 📚 Source citations shown in expandable sections
- ⚡ Powered by ChromaDB vector store

## Quick Start

```bash
cd apps/rag-chatbot
pip install -r requirements.txt
streamlit run app.py
```

## Architecture

```
User uploads docs → PyPDF/Text loader → Chunk (1000 chars)
→ OpenAI Embeddings → ChromaDB vector store
User asks question → Retrieve top-3 chunks → GPT-4o-mini → Answer + Sources
```

## Environment

Create `.env`:
```
OPENAI_API_KEY=sk-...
```

Or enter your API key directly in the sidebar.
