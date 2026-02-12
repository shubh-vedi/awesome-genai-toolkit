# 🛠️ GenAI Developer Tools & Platforms

Essential tools, APIs, and platforms for building GenAI applications.

---

## 🧠 LLM Providers

| Provider | Models | Best For | Pricing |
|----------|--------|----------|---------|
| [OpenAI](https://platform.openai.com/) | GPT-4o, o1, DALL-E 3 | Best overall, multimodal | Pay-per-token |
| [Anthropic](https://www.anthropic.com/) | Claude 3.5, Claude 4 | Long context, coding | Pay-per-token |
| [Google](https://ai.google.dev/) | Gemini 2.0, 1.5 | Multi-modal, large context | Free tier + paid |
| [Mistral](https://mistral.ai/) | Mistral Large, Codestral | Open-weight models | Pay-per-token |
| [Meta](https://llama.meta.com/) | Llama 3.3 | Open-source, self-hosting | Free (open weights) |
| [OpenRouter](https://openrouter.ai/) | 200+ models | Unified API for all models | Pay-per-token |
| [Groq](https://groq.com/) | Llama, Mixtral | Fastest inference | Free tier + paid |
| [Together.ai](https://www.together.ai/) | Open models | Fast inference, fine-tuning | Pay-per-token |

---

## 🔗 Frameworks & Libraries

### Agent Frameworks

| Tool | Language | What It Does |
|------|----------|--------------|
| [LangChain](https://github.com/langchain-ai/langchain) | Python/JS | Most popular LLM framework |
| [LlamaIndex](https://github.com/run-llama/llama_index) | Python | RAG-first framework |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Python | Multi-agent orchestration |
| [AutoGen](https://github.com/microsoft/autogen) | Python | Microsoft's agent framework |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | Python | Type-safe agents |
| [Smolagents](https://github.com/huggingface/smolagents) | Python | Lightweight HF agents |
| [DSPy](https://github.com/stanfordnlp/dspy) | Python | Programmatic prompt optimization |

### Structured Output

| Tool | What It Does |
|------|--------------|
| [Instructor](https://github.com/instructor-ai/instructor) | Structured extraction with Pydantic |
| [Outlines](https://github.com/dottxt-ai/outlines) | Guaranteed structured generation |
| [BAML](https://github.com/BoundaryML/baml) | DSL for LLM functions |

### Evaluation & Monitoring

| Tool | What It Does |
|------|--------------|
| [LangSmith](https://smith.langchain.com/) | LangChain observability |
| [Weights & Biases](https://wandb.ai/) | Experiment tracking |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | LLM observability (open-source) |
| [Braintrust](https://www.braintrust.dev/) | LLM evals and logging |

---

## 💾 Vector Databases

| Database | Type | Best For |
|----------|------|----------|
| [ChromaDB](https://www.trychroma.com/) | Embedded | Prototyping, local dev |
| [Pinecone](https://www.pinecone.io/) | Managed | Production, zero-ops |
| [Weaviate](https://weaviate.io/) | Self-hosted/Cloud | Hybrid search |
| [Qdrant](https://qdrant.tech/) | Self-hosted/Cloud | High performance |
| [Milvus](https://milvus.io/) | Self-hosted | Large-scale vector search |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL ext | If you already use Postgres |

---

## 🖼️ Image & Media Generation

| Tool | What It Does |
|------|--------------|
| [DALL-E 3](https://openai.com/dall-e-3) | Text-to-image (OpenAI) |
| [Midjourney](https://midjourney.com/) | Best quality images |
| [Stable Diffusion](https://stability.ai/) | Open-source image gen |
| [Flux](https://blackforestlabs.ai/) | Latest open image model |
| [ElevenLabs](https://elevenlabs.io/) | Voice synthesis & cloning |
| [Suno](https://suno.com/) | Music generation |

---

## 🚀 Deployment & Infrastructure

| Tool | What It Does |
|------|--------------|
| [Modal](https://modal.com/) | Serverless GPU compute |
| [Replicate](https://replicate.com/) | Run models via API |
| [vLLM](https://github.com/vllm-project/vllm) | Fast LLM inference server |
| [Ollama](https://ollama.com/) | Run LLMs locally |
| [LM Studio](https://lmstudio.ai/) | Local LLM GUI |
| [Hugging Face Spaces](https://huggingface.co/spaces) | Free app hosting |
| [Streamlit](https://streamlit.io/) | Quick Python web UIs |
| [Gradio](https://gradio.app/) | ML demo interfaces |

---

## 📊 Data & Datasets

| Resource | What It Offers |
|----------|---------------|
| [Hugging Face Datasets](https://huggingface.co/datasets) | 100k+ datasets |
| [Kaggle](https://www.kaggle.com/datasets) | ML datasets + competitions |
| [Common Crawl](https://commoncrawl.org/) | Web-scale text data |
| [The Pile](https://pile.eleuther.ai/) | Curated language dataset |

---

## 🔑 Quick Setup Checklist

```bash
# 1. Get API keys
# → OpenAI: platform.openai.com
# → Anthropic: console.anthropic.com
# → Google: ai.google.dev

# 2. Install core tools
pip install openai anthropic langchain chromadb

# 3. Set up local models (optional)
# Install Ollama: ollama.com
ollama pull llama3.3

# 4. Start building!
```
