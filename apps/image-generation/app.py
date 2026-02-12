"""
🎨 Image Generation App — Streamlit UI
Generate images from text using DALL-E 3.
"""

import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

# ── Page Config ────────────────────────────────────────────────
st.set_page_config(page_title="🎨 Image Generator", page_icon="🎨", layout="wide")

st.markdown("""
<style>
    .stApp { max-width: 1200px; margin: 0 auto; }
    .image-card { border-radius: 10px; overflow: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Session State ──────────────────────────────────────────────
if "generated_images" not in st.session_state:
    st.session_state.generated_images = []

# ── Sidebar ────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuration")

    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key

    st.divider()
    st.header("🎛️ Settings")

    size = st.selectbox("Size", ["1024x1024", "1792x1024", "1024x1792"], index=0)
    quality = st.selectbox("Quality", ["standard", "hd"], index=0)
    style = st.selectbox("Style", ["vivid", "natural"], index=0)

    st.divider()
    if st.button("🗑️ Clear Gallery", use_container_width=True):
        st.session_state.generated_images = []
        st.rerun()

    st.markdown("---")
    st.markdown(f"**Images generated:** {len(st.session_state.generated_images)}")


# ── Main Content ───────────────────────────────────────────────
st.title("🎨 AI Image Generator")
st.caption("Generate stunning images from text prompts using DALL-E 3")

# Prompt input
prompt = st.text_area(
    "📝 Describe your image",
    placeholder="A serene Japanese garden at sunset with cherry blossoms, digital art style...",
    height=100,
)

col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    generate_btn = st.button("🎨 Generate Image", type="primary", use_container_width=True)
with col2:
    st.markdown(f"**Size:** {size}")
with col3:
    st.markdown(f"**Quality:** {quality}")

# Example prompts
with st.expander("💡 Example Prompts"):
    examples = [
        "A futuristic cityscape at night with neon lights and flying cars, cyberpunk style",
        "A cozy coffee shop interior with warm lighting, watercolor painting",
        "An astronaut playing guitar on the moon with Earth in the background",
        "A magical forest with bioluminescent mushrooms and fireflies, fantasy art",
        "A minimalist tech startup office with clean lines, architectural visualization",
    ]
    for ex in examples:
        if st.button(ex, key=f"ex_{ex[:20]}"):
            st.session_state.prompt_fill = ex
            st.rerun()

st.divider()

# Generate
if generate_btn and prompt:
    if not api_key:
        st.error("⚠️ Please enter your OpenAI API key in the sidebar")
    else:
        with st.spinner("🎨 Generating image..."):
            try:
                client = OpenAI(api_key=api_key)
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size=size,
                    quality=quality,
                    style=style,
                    n=1,
                )

                image_url = response.data[0].url
                revised_prompt = response.data[0].revised_prompt

                st.session_state.generated_images.insert(0, {
                    "url": image_url,
                    "prompt": prompt,
                    "revised_prompt": revised_prompt,
                    "settings": f"{size} · {quality} · {style}",
                    "timestamp": datetime.now().strftime("%H:%M:%S"),
                })

                st.success("✅ Image generated!")

            except Exception as e:
                st.error(f"❌ Error: {e}")

elif generate_btn and not prompt:
    st.warning("Please enter a prompt first!")

# ── Gallery ────────────────────────────────────────────────────
if st.session_state.generated_images:
    st.subheader("🖼️ Generated Images")

    for i, img in enumerate(st.session_state.generated_images):
        with st.container():
            col1, col2 = st.columns([2, 1])
            with col1:
                st.image(img["url"], use_container_width=True)
            with col2:
                st.markdown(f"**Prompt:** {img['prompt']}")
                st.markdown(f"**Settings:** {img['settings']}")
                st.markdown(f"**Time:** {img['timestamp']}")
                with st.expander("📝 Revised Prompt"):
                    st.write(img["revised_prompt"])

            st.divider()
else:
    st.info("🎨 Enter a prompt above and click Generate to create your first image!")
