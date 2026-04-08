<!-- SEO Meta: Awesome GenAI Toolkit - The most comprehensive open-source collection of Generative AI resources, tools, frameworks, apps, notebooks, and tutorials for developers, researchers, and AI engineers. Covers LangChain, LlamaIndex, CrewAI, RAG pipelines, AI Agents, Voice AI, MCP Servers, Fine-Tuning LLMs with LoRA/QLoRA, Prompt Engineering, PageIndex, Agentic RAG, and more. Best generative AI toolkit 2025-2026. Learn how to build RAG from scratch, fine-tune open-source models, create AI agents, and deploy production-ready GenAI applications. -->
<!-- AEO Optimized: Answers "What is the best generative AI toolkit?", "How to build RAG from scratch?", "Best AI agent frameworks 2025", "How to fine-tune an LLM?", "What is MCP in AI?", "Best open-source AI tools for developers" -->
<!-- GEO Optimized: Structured data, FAQ schema-ready, hierarchical headings, internal linking, keyword-rich anchor text -->

<div align="center">

<img src="./assets/banner.png" alt="Awesome GenAI Toolkit - The Most Comprehensive Open-Source Collection of Generative AI Resources, Tools, Frameworks, Notebooks, and Apps for Developers and AI Engineers" width="900px" />

# Awesome GenAI Toolkit

### The Most Comprehensive Open-Source Generative AI Resource Hub for Developers

**1000+ curated tools, frameworks, runnable notebooks, and production-ready apps for building with LLMs, RAG, AI Agents, Voice AI, and MCP**

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![GitHub Stars](https://img.shields.io/github/stars/shubh-vedi/awesome-genai-toolkit?style=for-the-badge&logo=github&color=f4c542&labelColor=1a1a2e)](https://github.com/shubh-vedi/awesome-genai-toolkit/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/shubh-vedi/awesome-genai-toolkit?style=for-the-badge&logo=git&color=6366f1&labelColor=1a1a2e)](https://github.com/shubh-vedi/awesome-genai-toolkit/network/members)
[![Contributors](https://img.shields.io/github/contributors/shubh-vedi/awesome-genai-toolkit?style=for-the-badge&logo=contributorcovenant&color=10b981&labelColor=1a1a2e)](https://github.com/shubh-vedi/awesome-genai-toolkit/graphs/contributors)
[![Last Commit](https://img.shields.io/github/last-commit/shubh-vedi/awesome-genai-toolkit?style=for-the-badge&logo=github&color=ec4899&labelColor=1a1a2e)](https://github.com/shubh-vedi/awesome-genai-toolkit/commits/main)
[![License: MIT](https://img.shields.io/github/license/shubh-vedi/awesome-genai-toolkit?style=for-the-badge&logo=opensourceinitiative&color=22d3ee&labelColor=1a1a2e)](./LICENSE)

**RAG Pipelines** · **AI Agent Frameworks** · **LLM Fine-Tuning** · **Voice AI** · **MCP Servers** · **Production AI Apps** · **Runnable Colab Notebooks** · **Prompt Engineering**

<a href="https://github.com/shubh-vedi/awesome-genai-toolkit/stargazers"><img src="https://img.shields.io/badge/Star_This_Repo-It_Helps!-f4c542?style=for-the-badge&labelColor=1a1a2e" alt="Star this repo" /></a>
<a href="https://github.com/shubh-vedi/awesome-genai-toolkit/fork"><img src="https://img.shields.io/badge/Fork_It-Start_Contributing-6366f1?style=for-the-badge&labelColor=1a1a2e" alt="Fork this repo" /></a>
<a href="https://twitter.com/intent/tweet?text=Just%20found%20Awesome%20GenAI%20Toolkit%20%E2%80%94%20the%20most%20comprehensive%20open-source%20collection%20of%201000%2B%20Generative%20AI%20resources%20for%20developers!%0A%0ARAG%20%E2%80%A2%20AI%20Agents%20%E2%80%A2%20Fine-Tuning%20%E2%80%A2%20Voice%20AI%20%E2%80%A2%20MCP%20%26%20more%0A%0AStar%20it%20on%20GitHub%3A&url=https://github.com/shubh-vedi/awesome-genai-toolkit&hashtags=GenAI,LLM,AI,OpenSource,MachineLearning"><img src="https://img.shields.io/badge/Share_on_X-Spread_the_Word-000000?style=for-the-badge&logo=x&labelColor=1a1a2e" alt="Share on X/Twitter" /></a>

</div>

---

## What Makes This Different?

Most "awesome lists" are just link dumps. **This toolkit gives you runnable code.**

Every section includes **Google Colab notebooks** you can run in 2 minutes, **production-ready apps** you can clone and deploy, and **step-by-step guides** that actually teach you how things work under the hood.

| What You Get | Details |
|:---|:---|
| **Runnable Notebooks** | Build RAG from scratch, test PageIndex, fine-tune LLMs — all in Colab, zero setup |
| **Production Apps** | Clone and deploy real AI apps — meme generators, multimodal RAG, chat-with-PDF |
| **Not Just Links** | Architecture diagrams, code walkthroughs, side-by-side comparisons with benchmarks |
| **Always Current** | Community-maintained with the latest tools, models, and frameworks (2025-2026) |
| **Beginner Friendly** | Great first open-source contribution — most additions need no code at all |

---

## Table of Contents

| # | Section | What's Inside |
|:--|:--------|:-------------|
| 1 | [RAG Techniques and Patterns](#rag-techniques-and-patterns) | Build RAG from scratch, PageIndex, Agentic RAG, Hybrid Search, Vision RAG |
| 2 | [AI Agent Frameworks](#ai-agent-frameworks) | LangGraph, CrewAI, AutoGen, Agno + deployed agent apps |
| 3 | [Open-Source AI Libraries](#open-source-ai-libraries) | LangChain, LlamaIndex, Haystack, vLLM, Ollama, ChromaDB |
| 4 | [AI Apps Collection](#ai-apps-collection) | Deployable apps: RAG apps, Agno apps, meme generators |
| 5 | [LLM Benchmarks and Evaluation](#llm-benchmarks-and-evaluation) | Ragas, DeepEval, HELM, Guardrails, safety testing |
| 6 | [Fine-Tuning LLMs](#fine-tuning-llms) | LoRA, QLoRA, DPO, RLHF — step-by-step on consumer GPUs |
| 7 | [Voice AI Agents](#voice-ai-agents) | Whisper, ElevenLabs, Vapi, Livekit, real-time voice pipelines |
| 8 | [MCP AI Agents](#mcp-ai-agents) | Model Context Protocol servers, transports, integrations |
| 9 | [Prompt Optimization](#prompt-optimization) | LLMLingua, GPTCache, DSPy, cost reduction strategies |

---

## RAG Techniques and Patterns

> **Learn Retrieval Augmented Generation from zero to production** — from a basic pipeline in 50 lines of Python to advanced vectorless reasoning-based retrieval.

### Runnable Notebooks

| Notebook | What You'll Build | Colab | Difficulty |
|:---------|:-----------------|:-----:|:----------:|
| [Build RAG from Scratch](./rag-techniques/basic-rag/build_rag_from_scratch.ipynb) | Complete RAG pipeline: PDF → Chunks → ChromaDB → GPT answers with citations | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shubh-vedi/awesome-genai-toolkit/blob/main/rag-techniques/basic-rag/build_rag_from_scratch.ipynb) | Beginner |
| [PageIndex RAG (Cloud API)](./rag-techniques/pageindex-rag/pageindex_rag_complete_guide.ipynb) | Vectorless RAG: tree index + LLM reasoning retrieval (98.7% on FinanceBench) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shubh-vedi/awesome-genai-toolkit/blob/main/rag-techniques/pageindex-rag/pageindex_rag_complete_guide.ipynb) | Beginner |

### All RAG Patterns Covered

| Pattern | Description | Status |
|:--------|:-----------|:------:|
| **Basic RAG** | PDF → Chunks → Embeddings → Vector DB → LLM answer | Notebook ready |
| **PageIndex RAG** | No vectors, no chunking — LLM reasons over document tree index | Notebook ready |
| **Agentic RAG** | Self-correcting retrieval with tool use and multi-hop reasoning | Coming soon |
| **Hybrid Search** | Vector similarity + BM25 keyword search combined | Coming soon |
| **Vision RAG** | Multimodal retrieval over images, charts, and PDFs | Coming soon |
| **Knowledge Graph RAG** | Graph-based retrieval for connected entities and relationships | Coming soon |

**[Browse All RAG Techniques ->](./rag-techniques/)**

---

## AI Agent Frameworks

> **Build autonomous AI agents** — from single-agent tool use to multi-agent systems that collaborate, reason, and execute code.

| Framework | Best For | Key Feature |
|:----------|:---------|:-----------|
| **LangGraph** | Stateful agent workflows | Cycles, persistence, human-in-the-loop |
| **CrewAI** | Multi-agent collaboration | Role-based teams with shared memory |
| **AutoGen** | Task automation | Conversable agents with code execution |
| **Agno** | Lightweight multi-modal agents | Fast, model-agnostic with built-in tools |
| **OpenAI Agents SDK** | Tool-use agents | Native function calling and streaming |

### Deployed Agent Apps

| App | What It Does | Live Demo |
|:----|:------------|:---------:|
| [Hinglish Meme Generator](./agent-skills/hinglish-meme-generator/) | AI agent that generates culturally relevant Hinglish memes in multiple styles | [Try It](./agent-skills/hinglish-meme-generator/index.html) |
| [Trending Meme Creator](./agent-skills/trending-meme-creator/) | AI-powered meme creation using trending templates | Coming soon |

**[Browse AI Agent Frameworks ->](./agent-skills/)**

---

## Open-Source AI Libraries

> **The most popular open-source libraries for building generative AI applications**, organized by category with comparison tables.

| Category | Top Tools | Combined Stars |
|:---------|:---------|:--------------:|
| **LLM Frameworks** | LangChain, LlamaIndex, Haystack, DSPy | 90K+ |
| **Agent Frameworks** | CrewAI, AutoGen, Agno, LangGraph | 50K+ |
| **Vector Databases** | ChromaDB, Pinecone, Weaviate, Milvus, Qdrant | 40K+ |
| **Inference Engines** | vLLM, Ollama, llama.cpp, TGI, SGLang | 80K+ |

Includes comparison tables, setup guides, and recommendations for choosing the right tool.

**[Browse All Open-Source AI Libraries ->](./open-source-libraries/)**

---

## AI Apps Collection

> **Production-ready generative AI applications** — clone, deploy, and build on top of them.

| App Type | Description | Tech Stack |
|:---------|:-----------|:----------|
| **Agno Apps** | AI Storyboard Generator, Agentic React Apps | Agno, React, Python |
| **Multimodal RAG Apps** | Enterprise RAG with text, image, and PDF support | Gemini, Streamlit |
| **Chat with Data** | Talk to PDFs, YouTube videos, GitHub repos, CSVs | Streamlit, FastAPI |
| **Vision Apps** | Image analysis, OCR, object detection pipelines | GPT-4o, Claude |

Every app includes source code, deployment instructions, and architecture diagrams.

**[Browse AI Apps Collection ->](./ai-apps-collection/)**

---

## LLM Benchmarks and Evaluation

> **How to test, evaluate, and benchmark LLMs** for accuracy, safety, retrieval quality, and production readiness.

| Focus Area | Tools | Purpose |
|:-----------|:------|:--------|
| **Performance Testing** | LMSYS Chatbot Arena, HELM | Accuracy and speed benchmarking |
| **RAG Evaluation** | Ragas, DeepEval, Arize Phoenix | Retrieval and generation quality metrics |
| **Safety and Guardrails** | NeMo Guardrails, Guardrails AI | Content filtering, prompt injection defense |

### Runnable Notebooks

| Notebook | What It Covers |
|:---------|:-------------|
| [Gemini Embedding Testing](./llm-testing/gemini/Gemini_Embedding_2_Testing.ipynb) | Benchmark Google's Gemini Embedding 2 model |
| [Agentic RAG with Agno + Gemini](./llm-testing/gemini/Agentic_RAG_with_Agno_+_Gemini_Embeddings_2.ipynb) | Build and test Agentic RAG using Agno framework + Gemini embeddings |
| [Gemma 4 E2B Quickstart](./llm-testing/gemma/Gemma_4_E2B_quickstart.ipynb) | Run Google's Gemma 4 model in E2B sandbox |

**[Browse LLM Benchmarks ->](./llm-testing/)**

---

## Fine-Tuning LLMs

> **Step-by-step guides for fine-tuning large language models** using LoRA, QLoRA, RLHF, DPO, and full fine-tuning — on consumer GPUs.

| Technique | Libraries | Use Case |
|:----------|:---------|:---------|
| **LoRA / QLoRA (PEFT)** | PEFT, BitsAndBytes, Unsloth | Fine-tune 7B-70B models on a single GPU |
| **Full Fine-Tuning** | Axolotl, Unsloth, TRL | Domain-specific model adaptation |
| **Alignment Training** | TRL, Alignment Handbook | SFT, DPO, RLHF for instruction-following |

Includes training recipes, hyperparameter configs, and cost estimates.

**[Browse Fine-Tuning Guides ->](./fine-tuning-llms/)**

---

## Voice AI Agents

> **Build real-time voice-enabled AI applications** with speech-to-text, text-to-speech, and low-latency conversational voice pipelines.

| Component | Top Tools | Capabilities |
|:----------|:---------|:------------|
| **STT / TTS** | Whisper, ElevenLabs, Deepgram | Transcription and voice synthesis |
| **Voice Pipelines** | Vapi, Retell, Livekit | Low-latency conversational AI |
| **Local / Edge Voice** | Piper, Sherpa-ONNX | On-device voice processing |

Includes integration guides, latency benchmarks, and sample voice agent implementations.

**[Browse Voice AI Agents ->](./voice-ai-agents/)**

---

## MCP AI Agents

> **Model Context Protocol (MCP)** — the emerging open standard for connecting LLMs to databases, APIs, and external tools.

| Category | Examples | Purpose |
|:---------|:--------|:--------|
| **MCP Servers** | SQLite, Postgres, Slack, GitHub | Structured data access for LLMs |
| **Transports** | Stdio, SSE, HTTP Streaming | Communication protocols |
| **MCP Clients** | Claude Desktop, Cursor, Claude Code | User-facing interfaces |

Includes MCP server setup guides, transport configuration, and real-world integration examples.

**[Browse MCP Agents ->](./mcp-ai-agents/)**

---

## Prompt Optimization

> **Reduce LLM costs, lower latency, and improve output quality** through better prompting strategies and caching.

| Method | Description | Tooling |
|:-------|:-----------|:--------|
| **Prompt Compression** | Reduce token counts without losing meaning | LLMLingua |
| **Semantic Caching** | Cache and reuse similar query results | GPTCache |
| **Automated Prompt Tuning** | Iteratively optimize prompts with metrics | DSPy |

**[Browse Prompt Optimization ->](./prompt-optimization/)**

---

## Frequently Asked Questions

<details>
<summary><strong>What is Generative AI?</strong></summary>
<br/>

Generative AI refers to artificial intelligence systems that can create new content — including text, images, code, audio, and video — based on patterns learned from training data. Popular generative AI models include ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google), LLaMA (Meta), and Stable Diffusion (Stability AI). These models power applications ranging from chatbots and code assistants to image generators and autonomous AI agents.

</details>

<details>
<summary><strong>What is RAG (Retrieval Augmented Generation) and how does it work?</strong></summary>
<br/>

RAG (Retrieval Augmented Generation) is a technique that enhances LLM responses by retrieving relevant information from external knowledge bases before generating an answer. A basic RAG pipeline works in three steps: (1) **Index** — documents are split into chunks, embedded into vectors, and stored in a vector database like ChromaDB; (2) **Retrieve** — when a user asks a question, the query is embedded and similar chunks are retrieved; (3) **Generate** — retrieved chunks are passed as context to the LLM, which generates a grounded answer. RAG reduces hallucinations, keeps responses up-to-date, and is the most popular pattern for building enterprise AI applications. This toolkit covers basic RAG, agentic RAG, hybrid search, vision RAG, and vectorless approaches like PageIndex. See our [RAG Techniques section](#rag-techniques-and-patterns).

</details>

<details>
<summary><strong>What is PageIndex RAG and how is it different from vector RAG?</strong></summary>
<br/>

PageIndex RAG is a vectorless, reasoning-based retrieval approach that replaces traditional vector databases and embedding-based similarity search. Instead of chunking documents and computing cosine similarity, PageIndex builds a hierarchical tree index of the document's natural structure (sections, sub-sections, page ranges) and uses an LLM to reason over the tree to identify which sections are relevant to a query. This approach achieved 98.7% accuracy on FinanceBench, compared to ~80% for traditional vector RAG. Try our [PageIndex RAG notebook](./rag-techniques/pageindex-rag/pageindex_rag_complete_guide.ipynb) to see it in action.

</details>

<details>
<summary><strong>What is the best framework for building AI agents in 2025?</strong></summary>
<br/>

The best AI agent framework depends on your use case:
- **LangGraph** — Best for complex stateful workflows with cycles, persistence, and human-in-the-loop control
- **CrewAI** — Best for multi-agent collaboration with role-based teams and shared memory
- **AutoGen** — Best for automated task execution with conversable agents and code execution
- **Agno** — Best for lightweight, model-agnostic agents with built-in tools and fast prototyping
- **OpenAI Agents SDK** — Best for native function calling and streaming with OpenAI models

See our [AI Agent Frameworks section](#ai-agent-frameworks) for detailed comparisons and code examples.

</details>

<details>
<summary><strong>What is MCP (Model Context Protocol)?</strong></summary>
<br/>

MCP (Model Context Protocol) is an open standard created by Anthropic that allows large language models to securely connect to external tools, databases, and APIs through a unified interface. Think of it as "USB for AI" — a universal way for LLMs to access real-time data and perform actions like querying databases, sending messages, or reading files. MCP uses a client-server architecture with transports like stdio and SSE. Popular MCP clients include Claude Desktop, Cursor, and Claude Code. See our [MCP section](#mcp-ai-agents).

</details>

<details>
<summary><strong>How do I fine-tune an LLM on my own data?</strong></summary>
<br/>

Start with parameter-efficient methods like **LoRA** or **QLoRA** using libraries like PEFT, Unsloth, and Axolotl — they let you fine-tune 7B-70B parameter models on a single consumer GPU (even an RTX 3090 or free Colab T4). The typical workflow is: (1) prepare your dataset in instruction format, (2) load a base model with quantization (4-bit for QLoRA), (3) attach LoRA adapters to target layers, (4) train for 1-3 epochs, (5) merge adapters back into the base model. For alignment training (making models follow instructions safely), use SFT followed by DPO or RLHF with the TRL library. See our [Fine-Tuning Guides](#fine-tuning-llms).

</details>

<details>
<summary><strong>How do I build a RAG pipeline from scratch?</strong></summary>
<br/>

You can build a complete RAG pipeline in ~50 lines of Python using OpenAI + ChromaDB. The steps are: (1) load a PDF using PyMuPDF, (2) split text into overlapping chunks, (3) embed chunks using OpenAI's text-embedding-3-small model, (4) store embeddings in ChromaDB, (5) at query time, embed the user question and retrieve the top-K most similar chunks, (6) pass retrieved chunks as context to GPT and generate a grounded answer. Our [Build RAG from Scratch notebook](./rag-techniques/basic-rag/build_rag_from_scratch.ipynb) walks through every step with runnable code.

</details>

<details>
<summary><strong>Is this repo actively maintained?</strong></summary>
<br/>

Yes. New tools, notebooks, and apps are added every week. The repo is community-maintained and accepts contributions. Check the badges at the top for the latest commit date and contributor count.

</details>

---

## How to Contribute

> **One of the most beginner-friendly open-source projects — most contributions need no code at all.**

### Quick Ways to Help (< 5 Minutes)

| Action | Impact |
|:-------|:-------|
| [Star this repo](../../stargazers) | Helps others discover it in GitHub search and trending |
| [Fork it](../../fork) | Shows the community is active and growing |
| [Report broken links](../../issues) | Keeps the toolkit reliable and up-to-date |
| [Suggest new tools](../../issues) | Helps expand coverage of the GenAI ecosystem |
| [Share on social media](#share-this-repo) | Spreads the word to more developers worldwide |

### Code and Content Contributions

1. **Fork** the repository
2. **Create** a new branch: `git checkout -b add-resource-name`
3. **Add** your resource to the appropriate category
4. **Submit** a Pull Request with a clear description

See the full [Contributing Guide](CONTRIBUTING.md) for detailed guidelines.

> **First time contributing to open source?** Look for issues tagged `good first issue` — they're designed for getting started.

---

## Roadmap

- [x] Launch initial 9 categories with curated resources
- [x] Add deployable AI apps (Agno, RAG, meme generators)
- [x] Add runnable Colab notebooks (RAG from scratch, PageIndex, Gemini, Gemma)
- [ ] Community voting on best tools per category
- [ ] Monthly "What's New in GenAI" digest newsletter
- [ ] Multilingual documentation (Hindi, Mandarin, Spanish, Japanese)
- [ ] Interactive web version with search and filtering
- [ ] Hall of Fame for top contributors

---

## Star History

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=shubh-vedi/awesome-genai-toolkit&type=Date)](https://star-history.com/#shubh-vedi/awesome-genai-toolkit&Date)

</div>

---

## Share This Repo

> **Help us reach more developers. Pick your platform:**

<div align="center">

<a href="https://twitter.com/intent/tweet?text=Just%20found%20Awesome%20GenAI%20Toolkit%20%E2%80%94%20the%20most%20comprehensive%20open-source%20collection%20of%201000%2B%20Generative%20AI%20resources!%0A%0ARAG%20from%20scratch%20%E2%80%A2%20PageIndex%20%E2%80%A2%20AI%20Agents%20%E2%80%A2%20Fine-Tuning%20%E2%80%A2%20Voice%20AI%20%E2%80%A2%20MCP%0A%0AStar%20it%20now%3A&url=https://github.com/shubh-vedi/awesome-genai-toolkit&hashtags=GenAI,LLM,AI,OpenSource,RAG"><img src="https://img.shields.io/badge/Share_on_X_(Twitter)-000000?style=for-the-badge&logo=x&logoColor=white" alt="Share on X/Twitter" /></a>
<a href="https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/shubh-vedi/awesome-genai-toolkit"><img src="https://img.shields.io/badge/Share_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Share on LinkedIn" /></a>
<a href="https://www.reddit.com/submit?url=https://github.com/shubh-vedi/awesome-genai-toolkit&title=Awesome%20GenAI%20Toolkit%20-%201000%2B%20Curated%20Generative%20AI%20Resources%20with%20Runnable%20Notebooks"><img src="https://img.shields.io/badge/Share_on_Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white" alt="Share on Reddit" /></a>
<a href="https://news.ycombinator.com/submitlink?u=https://github.com/shubh-vedi/awesome-genai-toolkit&t=Awesome%20GenAI%20Toolkit%20-%201000%2B%20Generative%20AI%20Resources%20with%20Runnable%20Colab%20Notebooks"><img src="https://img.shields.io/badge/Share_on_Hacker_News-F0652F?style=for-the-badge&logo=ycombinator&logoColor=white" alt="Share on Hacker News" /></a>
<a href="https://dev.to/new?prefill=---%0Atitle%3A%20Awesome%20GenAI%20Toolkit%20-%201000%2B%20AI%20Resources%20with%20Runnable%20Notebooks%0Apublished%3A%20false%0Atags%3A%20ai%2C%20machinelearning%2C%20opensource%2C%20genai%0A---%0A%0ACheck%20out%20this%20amazing%20collection%3A%20https%3A%2F%2Fgithub.com%2Fshubh-vedi%2Fawesome-genai-toolkit"><img src="https://img.shields.io/badge/Write_on_Dev.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white" alt="Share on Dev.to" /></a>

</div>

---

<div align="center">

### Built by the GenAI Community, for the GenAI Community

<br/>

Every star, fork, and contribution makes this toolkit better for everyone.

<br/>

<a href="https://github.com/shubh-vedi/awesome-genai-toolkit/stargazers"><img src="https://img.shields.io/badge/Star_This_Repo-f4c542?style=for-the-badge&labelColor=1a1a2e" alt="Star" /></a>
<a href="https://github.com/shubh-vedi/awesome-genai-toolkit/fork"><img src="https://img.shields.io/badge/Fork_It-6366f1?style=for-the-badge&labelColor=1a1a2e" alt="Fork" /></a>
<a href="https://github.com/shubh-vedi/awesome-genai-toolkit/pulls"><img src="https://img.shields.io/badge/Contribute-10b981?style=for-the-badge&labelColor=1a1a2e" alt="Contribute" /></a>

<br/>
<br/>

**Made with love by [Shubh Vedi](https://github.com/shubh-vedi) and [Contributors](https://github.com/shubh-vedi/awesome-genai-toolkit/graphs/contributors)**

<br/>

<sub><strong>Keywords:</strong> awesome list, generative AI, GenAI toolkit, LLM frameworks, LangChain tutorial, LlamaIndex guide, CrewAI, AutoGen, RAG tutorial, retrieval augmented generation, how to build RAG from scratch, PageIndex RAG, vectorless RAG, agentic RAG, AI agents 2025, AI agent frameworks, voice AI, text to speech AI, MCP model context protocol, fine-tune LLM, LoRA tutorial, QLoRA guide, prompt engineering, open source AI tools, best AI tools 2025, best AI tools 2026, ChatGPT alternatives, Claude AI, Gemini AI, Gemma, LLaMA, vector database, ChromaDB, Pinecone, AI developer toolkit, machine learning resources, deep learning tools, GPT-4o, production AI apps, Google Colab notebooks AI</sub>

</div>
