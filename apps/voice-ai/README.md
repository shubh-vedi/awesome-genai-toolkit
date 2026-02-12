# 🎙️ Voice AI Assistant

A voice assistant with **3 modes**: voice chat, text chat with audio output, and standalone text-to-speech — powered by Whisper, GPT, and OpenAI TTS.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-Whisper+TTS-purple)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40-red)

## Features
- 🎤 **Voice Chat** — Upload audio → transcribe → respond → speak
- ⌨️ **Text Chat** — Type messages, hear AI responses
- 🔊 **TTS Studio** — Convert any text to speech with 6 voices
- 📥 Download audio responses

## Quick Start

```bash
cd apps/voice-ai
pip install -r requirements.txt
streamlit run app.py
```

## Pipeline

```
Audio Upload → Whisper STT → GPT-4o-mini → OpenAI TTS → Audio playback
```

## Environment

Create `.env`:
```
OPENAI_API_KEY=sk-...
```
