"""
🎙️ Voice AI Assistant — Streamlit UI
Speech-to-Text + LLM + Text-to-Speech pipeline.
"""

import os
import tempfile
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

# ── Page Config ────────────────────────────────────────────────
st.set_page_config(page_title="🎙️ Voice AI", page_icon="🎙️", layout="wide")

st.markdown("""
<style>
    .stApp { max-width: 1000px; margin: 0 auto; }
</style>
""", unsafe_allow_html=True)

# ── Session State ──────────────────────────────────────────────
if "voice_messages" not in st.session_state:
    st.session_state.voice_messages = []
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# ── Sidebar ────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuration")

    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key

    st.divider()
    st.header("🎛️ Settings")

    voice = st.selectbox("🔊 TTS Voice", ["alloy", "echo", "fable", "onyx", "nova", "shimmer"], index=0)
    model = st.selectbox("🧠 LLM Model", ["gpt-4o-mini", "gpt-4o"], index=0)
    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful voice assistant. Keep responses concise and conversational (2-3 sentences max).",
        height=100,
    )

    st.divider()
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.voice_messages = []
        st.session_state.conversation_history = []
        st.rerun()


# ── Helper Functions ───────────────────────────────────────────
def transcribe_audio(audio_file) -> str:
    """Transcribe audio using Whisper."""
    client = OpenAI(api_key=api_key)
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text",
    )
    return transcript


def get_llm_response(user_input: str) -> str:
    """Get response from LLM."""
    client = OpenAI(api_key=api_key)
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(st.session_state.conversation_history)
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=300,
        temperature=0.7,
    )
    return response.choices[0].message.content


def text_to_speech(text: str) -> bytes:
    """Convert text to speech."""
    client = OpenAI(api_key=api_key)
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=text,
    )
    return response.content


# ── Main Content ───────────────────────────────────────────────
st.title("🎙️ Voice AI Assistant")
st.caption("Listen → Think → Speak — A complete voice pipeline")

# Tabs for different modes
tab1, tab2, tab3 = st.tabs(["🎤 Voice Chat", "⌨️ Text Chat", "🔊 Text-to-Speech"])

# ── Tab 1: Voice Chat ─────────────────────────────────────────
with tab1:
    st.markdown("### Upload Audio or Record")

    audio_file = st.file_uploader(
        "Upload an audio file",
        type=["mp3", "wav", "m4a", "webm", "ogg"],
        key="audio_upload",
    )

    if audio_file and st.button("🎧 Process Audio", type="primary", key="process_audio"):
        if not api_key:
            st.error("⚠️ Please enter your OpenAI API key")
        else:
            col1, col2, col3 = st.columns(3)

            with col1:
                with st.spinner("🎧 Transcribing..."):
                    transcript = transcribe_audio(audio_file)
                st.success("Transcribed!")
                st.info(f"📝 **You said:** {transcript}")

            with col2:
                with st.spinner("🤖 Thinking..."):
                    response = get_llm_response(transcript)
                st.success("Response ready!")
                st.info(f"🤖 **AI:** {response}")

            with col3:
                with st.spinner("🔊 Generating speech..."):
                    audio_bytes = text_to_speech(response)
                st.success("Audio ready!")
                st.audio(audio_bytes, format="audio/mp3")

            # Update history
            st.session_state.conversation_history.append({"role": "user", "content": transcript})
            st.session_state.conversation_history.append({"role": "assistant", "content": response})

# ── Tab 2: Text Chat (with voice output) ──────────────────────
with tab2:
    st.markdown("### Type & Hear")

    # Display chat history
    for msg in st.session_state.voice_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "audio" in msg:
                st.audio(msg["audio"], format="audio/mp3")

    if prompt := st.chat_input("Type your message...", key="text_chat"):
        if not api_key:
            st.error("⚠️ Please enter your OpenAI API key")
        else:
            # Add user message
            st.session_state.voice_messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Get response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = get_llm_response(prompt)
                st.markdown(response)

                with st.spinner("Generating speech..."):
                    audio_bytes = text_to_speech(response)
                st.audio(audio_bytes, format="audio/mp3")

            st.session_state.voice_messages.append({
                "role": "assistant",
                "content": response,
                "audio": audio_bytes,
            })
            st.session_state.conversation_history.append({"role": "user", "content": prompt})
            st.session_state.conversation_history.append({"role": "assistant", "content": response})

# ── Tab 3: Text-to-Speech Only ─────────────────────────────────
with tab3:
    st.markdown("### Convert Text to Speech")

    tts_text = st.text_area("Enter text to convert to speech", height=150, placeholder="Hello! This is a test of the text-to-speech system...")

    tts_col1, tts_col2 = st.columns([3, 1])
    with tts_col2:
        tts_voice = st.selectbox("Voice", ["alloy", "echo", "fable", "onyx", "nova", "shimmer"], key="tts_voice")

    if st.button("🔊 Generate Speech", type="primary", key="tts_btn"):
        if not api_key:
            st.error("⚠️ Please enter your OpenAI API key")
        elif not tts_text:
            st.warning("Please enter some text first")
        else:
            with st.spinner("Generating speech..."):
                client = OpenAI(api_key=api_key)
                response = client.audio.speech.create(
                    model="tts-1",
                    voice=tts_voice,
                    input=tts_text,
                )
                audio_bytes = response.content

            st.audio(audio_bytes, format="audio/mp3")
            st.download_button(
                "📥 Download Audio",
                data=audio_bytes,
                file_name="speech.mp3",
                mime="audio/mp3",
            )
