"""
🌐 Multi-Modal AI App — Streamlit UI
Vision + Text + Audio analysis with GPT-4o.
"""

import os
import base64
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

# ── Page Config ────────────────────────────────────────────────
st.set_page_config(page_title="🌐 Multi-Modal AI", page_icon="🌐", layout="wide")

st.markdown("""
<style>
    .stApp { max-width: 1100px; margin: 0 auto; }
</style>
""", unsafe_allow_html=True)

# ── Session State ──────────────────────────────────────────────
if "mm_messages" not in st.session_state:
    st.session_state.mm_messages = []

# ── Sidebar ────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuration")

    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key

    st.divider()
    model = st.selectbox("Model", ["gpt-4o", "gpt-4o-mini"], index=0)
    detail = st.selectbox("Vision Detail", ["high", "low", "auto"], index=0)

    st.divider()
    if st.button("🗑️ Clear All", use_container_width=True):
        st.session_state.mm_messages = []
        st.rerun()


# ── Helper Functions ───────────────────────────────────────────
def encode_image(uploaded_file) -> str:
    return base64.b64encode(uploaded_file.getvalue()).decode("utf-8")


def get_media_type(filename: str) -> str:
    ext = Path(filename).suffix.lower()
    types = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
             ".gif": "image/gif", ".webp": "image/webp"}
    return types.get(ext, "image/png")


def analyze_image(image_file, prompt: str) -> str:
    client = OpenAI(api_key=api_key)
    base64_image = encode_image(image_file)
    media_type = get_media_type(image_file.name)

    response = client.chat.completions.create(
        model=model,
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {
                    "url": f"data:{media_type};base64,{base64_image}",
                    "detail": detail,
                }},
            ],
        }],
        max_tokens=1500,
    )
    return response.choices[0].message.content


def analyze_multiple_images(image_files, prompt: str) -> str:
    client = OpenAI(api_key=api_key)
    content = [{"type": "text", "text": prompt}]

    for img in image_files:
        base64_image = encode_image(img)
        media_type = get_media_type(img.name)
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:{media_type};base64,{base64_image}",
                "detail": detail,
            },
        })

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=2000,
    )
    return response.choices[0].message.content


def transcribe_audio(audio_file) -> str:
    client = OpenAI(api_key=api_key)
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text",
    )
    return transcript


# ── Main Content ───────────────────────────────────────────────
st.title("🌐 Multi-Modal AI")
st.caption("Analyze images, charts, documents, and audio — all in one place")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["👁️ Image Analysis", "🔍 Compare Images", "📝 OCR & Charts", "🎧 Audio"])

# ── Tab 1: Image Analysis ─────────────────────────────────────
with tab1:
    st.markdown("### Analyze an Image")

    uploaded_image = st.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg", "gif", "webp"],
        key="single_image",
    )

    if uploaded_image:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
        with col2:
            analysis_prompt = st.text_area(
                "What would you like to know?",
                value="Describe this image in detail.",
                key="analysis_prompt",
                height=100,
            )

            preset = st.selectbox("Or use a preset:", [
                "Custom (use text above)",
                "Describe in detail",
                "Extract all text (OCR)",
                "Analyze chart/graph",
                "Identify objects",
                "Suggest improvements",
                "Generate alt text",
            ])

            presets = {
                "Describe in detail": "Describe this image in detail, including colors, composition, and mood.",
                "Extract all text (OCR)": "Extract ALL text from this image exactly as written. Preserve formatting.",
                "Analyze chart/graph": "Analyze this chart: type, data represented, key trends, takeaways.",
                "Identify objects": "List all identifiable objects in this image with their approximate positions.",
                "Suggest improvements": "If this is a design/UI, suggest specific improvements for better UX.",
                "Generate alt text": "Write concise, descriptive alt text for this image (max 125 characters).",
            }

            if preset != "Custom (use text above)":
                analysis_prompt = presets[preset]

            if st.button("🔍 Analyze", type="primary", key="analyze_btn"):
                if not api_key:
                    st.error("⚠️ Please enter your API key")
                else:
                    with st.spinner("Analyzing..."):
                        result = analyze_image(uploaded_image, analysis_prompt)
                    st.markdown("### Result")
                    st.markdown(result)

# ── Tab 2: Compare Images ─────────────────────────────────────
with tab2:
    st.markdown("### Compare Multiple Images")

    compare_images = st.file_uploader(
        "Upload 2+ images to compare",
        type=["png", "jpg", "jpeg", "gif", "webp"],
        accept_multiple_files=True,
        key="compare_images",
    )

    if compare_images and len(compare_images) >= 2:
        cols = st.columns(min(len(compare_images), 4))
        for i, img in enumerate(compare_images):
            with cols[i % len(cols)]:
                st.image(img, caption=f"Image {i+1}", use_container_width=True)

        compare_prompt = st.text_input(
            "Comparison prompt",
            value="Compare these images in detail. Note similarities and differences.",
        )

        if st.button("🔍 Compare", type="primary", key="compare_btn"):
            if not api_key:
                st.error("⚠️ Please enter your API key")
            else:
                with st.spinner("Comparing..."):
                    result = analyze_multiple_images(compare_images, compare_prompt)
                st.markdown("### Comparison Result")
                st.markdown(result)
    elif compare_images:
        st.warning("Please upload at least 2 images to compare")

# ── Tab 3: OCR & Charts ───────────────────────────────────────
with tab3:
    st.markdown("### Extract Text or Analyze Charts")

    ocr_image = st.file_uploader(
        "Upload a screenshot, document, or chart",
        type=["png", "jpg", "jpeg", "webp"],
        key="ocr_image",
    )

    if ocr_image:
        st.image(ocr_image, caption="Uploaded", use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("📝 Extract Text (OCR)", type="primary", use_container_width=True):
                with st.spinner("Extracting text..."):
                    result = analyze_image(
                        ocr_image,
                        "Extract ALL text from this image exactly as written. Preserve formatting, line breaks, and structure.",
                    )
                st.code(result)
        with col2:
            if st.button("📊 Analyze Chart", type="primary", use_container_width=True):
                with st.spinner("Analyzing chart..."):
                    result = analyze_image(
                        ocr_image,
                        "Analyze this chart/graph in detail:\n1. What type of chart?\n2. What data is represented?\n3. Key trends and insights?\n4. Main takeaways?",
                    )
                st.markdown(result)

# ── Tab 4: Audio ───────────────────────────────────────────────
with tab4:
    st.markdown("### Transcribe & Analyze Audio")

    audio_file = st.file_uploader(
        "Upload an audio file",
        type=["mp3", "wav", "m4a", "webm", "ogg"],
        key="audio_file",
    )

    if audio_file:
        st.audio(audio_file)

        analyze_audio = st.checkbox("Also analyze content after transcription", value=True)

        if st.button("🎧 Transcribe", type="primary", key="transcribe_btn"):
            if not api_key:
                st.error("⚠️ Please enter your API key")
            else:
                with st.spinner("Transcribing..."):
                    transcript = transcribe_audio(audio_file)

                st.markdown("### 📝 Transcript")
                st.text_area("", value=transcript, height=200, key="transcript_display")

                if analyze_audio:
                    with st.spinner("Analyzing content..."):
                        client = OpenAI(api_key=api_key)
                        analysis = client.chat.completions.create(
                            model=model,
                            messages=[
                                {"role": "system", "content": "Analyze the following transcript. Provide: 1) Summary, 2) Key points, 3) Action items (if any), 4) Sentiment."},
                                {"role": "user", "content": transcript},
                            ],
                            max_tokens=1000,
                        ).choices[0].message.content

                    st.markdown("### 📊 Analysis")
                    st.markdown(analysis)
