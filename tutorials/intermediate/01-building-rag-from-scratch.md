# 🔧 Building RAG from Scratch

Build a complete Retrieval-Augmented Generation system **without any framework** — understand every piece.

## Why Build from Scratch?

Frameworks like LangChain and LlamaIndex are great, but understanding the internals helps you:
- Debug issues faster
- Customize for your use case
- Make informed framework choices
- Build more efficient pipelines

## Architecture

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Documents│───▶│Chunking  │───▶│Embeddings│───▶│Vector DB │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
                                                      │
┌──────────┐    ┌──────────┐    ┌──────────┐          │
│  Answer  │◀───│   LLM    │◀───│  Prompt  │◀─────────┘
└──────────┘    └──────────┘    └──────────┘
                                      ▲
                                      │
                                ┌──────────┐
                                │  Query   │
                                └──────────┘
```

## Step 1: Document Loading

```python
from pathlib import Path

def load_documents(directory: str) -> list[dict]:
    """Load text files from a directory."""
    documents = []
    for filepath in Path(directory).glob("**/*.txt"):
        text = filepath.read_text(encoding="utf-8")
        documents.append({
            "text": text,
            "source": str(filepath),
            "filename": filepath.name,
        })
    print(f"Loaded {len(documents)} documents")
    return documents
```

## Step 2: Text Chunking

```python
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        # Try to break at a sentence boundary
        if end < len(text):
            last_period = chunk.rfind(". ")
            if last_period > chunk_size * 0.5:
                chunk = chunk[:last_period + 1]
                end = start + last_period + 1

        chunks.append(chunk.strip())
        start = end - overlap

    return chunks
```

**Why overlap?** Without it, if a relevant sentence gets split across two chunks, neither chunk has the full context.

## Step 3: Generate Embeddings

```python
from openai import OpenAI
import numpy as np

client = OpenAI()

def get_embeddings(texts: list[str], model: str = "text-embedding-3-small") -> list[list[float]]:
    """Generate embeddings for a list of texts."""
    response = client.embeddings.create(
        input=texts,
        model=model,
    )
    return [item.embedding for item in response.data]
```

## Step 4: Vector Store (Simple In-Memory)

```python
import numpy as np

class SimpleVectorStore:
    def __init__(self):
        self.vectors = []
        self.documents = []

    def add(self, texts: list[str], embeddings: list[list[float]], metadata: list[dict] = None):
        for i, (text, embedding) in enumerate(zip(texts, embeddings)):
            self.vectors.append(np.array(embedding))
            self.documents.append({
                "text": text,
                "metadata": metadata[i] if metadata else {},
            })

    def search(self, query_embedding: list[float], k: int = 3) -> list[dict]:
        query_vec = np.array(query_embedding)
        similarities = []
        for i, doc_vec in enumerate(self.vectors):
            # Cosine similarity
            sim = np.dot(query_vec, doc_vec) / (
                np.linalg.norm(query_vec) * np.linalg.norm(doc_vec)
            )
            similarities.append((sim, i))
        similarities.sort(reverse=True)
        return [
            {**self.documents[i], "score": float(sim)}
            for sim, i in similarities[:k]
        ]
```

## Step 5: RAG Query

```python
def rag_query(question: str, vector_store: SimpleVectorStore, k: int = 3) -> str:
    # 1. Embed the question
    query_embedding = get_embeddings([question])[0]

    # 2. Retrieve relevant chunks
    results = vector_store.search(query_embedding, k=k)

    # 3. Build the prompt
    context = "\n\n---\n\n".join([r["text"] for r in results])

    prompt = f"""Answer the question based on the provided context. If the context
doesn't contain enough information, say so.

Context:
{context}

Question: {question}

Answer:"""

    # 4. Generate answer
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Answer based on the provided context."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content
```

## Step 6: Putting It All Together

```python
# Load and chunk documents
docs = load_documents("./my_documents")
all_chunks = []
all_metadata = []
for doc in docs:
    chunks = chunk_text(doc["text"])
    all_chunks.extend(chunks)
    all_metadata.extend([{"source": doc["source"]}] * len(chunks))

# Create embeddings and store
embeddings = get_embeddings(all_chunks)
store = SimpleVectorStore()
store.add(all_chunks, embeddings, all_metadata)

# Query
answer = rag_query("What are the main features?", store)
print(answer)
```

## Key Takeaways

1. **RAG = Retrieve + Generate** — it's fundamentally simple
2. **Chunking strategy matters** — too small = no context, too large = noise
3. **Embedding model choice** — `text-embedding-3-small` is a great default
4. **Cosine similarity** — standard metric for comparing embeddings
5. **Prompt engineering** — the prompt template significantly affects answer quality

## Next Steps

- Use a real vector database: [ChromaDB](https://docs.trychroma.com/), [Pinecone](https://www.pinecone.io/), [Weaviate](https://weaviate.io/)
- Try the [RAG Chatbot App](../../apps/rag-chatbot/) with LangChain
- Explore the [LlamaIndex RAG notebook](../../notebooks/llamaindex-rag.ipynb) for framework-based RAG
- Move to [Advanced Tutorials](../advanced/) for agent architectures
