# 📀 Retrieval Augmented Apps

> Build smarter AI apps by grounding LLMs in your own data — from basic RAG chains to agentic, self-correcting retrieval systems.

## 📂 Structure

```
rag-techniques/
├── basic-rag/            # Simple retrieval + generation pipelines
├── agentic-rag/          # RAG with agent-based reasoning & tool use
├── hybrid-search/        # Combining vector + keyword search
├── vision-rag/           # RAG over images and multimodal data
└── knowledge-graphs/     # Graph-based retrieval with citations
```

## 🔥 Why This Is Trending

RAG remains the most practical way to build production AI apps — it eliminates hallucinations, keeps responses grounded in facts, and works with any LLM. New techniques like Agentic RAG, Corrective RAG (CRAG), and Knowledge Graph RAG are pushing the boundaries of what's possible.

## 🚀 Getting Started

```bash
cd rag-techniques/<project-name>
pip install -r requirements.txt
python main.py
```

## 📋 Projects

| Project | Description | Difficulty |
|---------|-------------|------------|
| [Build RAG from Scratch](./build_rag_from_scratch.ipynb) | Chat with your PDF using OpenAI + ChromaDB — no frameworks, ~50 lines of core logic | Beginner |
| *Agentic RAG* | Self-correcting retrieval with LangGraph | Coming soon |
| *Hybrid Search* | Combine vector + keyword search (BM25) | Coming soon |
| *RAG Evaluation with Ragas* | Measure faithfulness, relevancy, and recall | Coming soon |

## 🤝 Contributing

Have a RAG project? We'd love to include it! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.
