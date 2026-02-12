# 🤖 AI Agent Team

A multi-agent system built with **CrewAI** where specialized AI agents collaborate to research, write, and edit content — all via **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-0.80-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40-red)

## Features
- 🤖 3 agents: Researcher → Writer → Editor
- 📊 Real-time progress indicators
- 📥 Download results as Markdown
- 🎛️ Model & word count selection

## Quick Start

```bash
cd apps/ai-agent
pip install -r requirements.txt
streamlit run app.py
```

## Agent Pipeline

```
User enters topic → Researcher gathers info → Writer creates article
→ Editor polishes → Final output + download
```

## Environment

Create `.env`:
```
OPENAI_API_KEY=sk-...
```
