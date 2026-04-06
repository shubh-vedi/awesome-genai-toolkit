# 🇮🇳 Hinglish Meme Generator — AI Edge Gallery Skill

> Turn any English text into viral-worthy Hinglish memes — running 100% offline on your phone with Gemma 4!

An **Agent Skill** for the [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) app that converts English text into natural Hinglish (Hindi-English code-switching) and renders beautiful, shareable meme cards — all powered by on-device AI.

---

## ✨ What It Does

1. **Translates** English text to natural Hinglish with authentic desi slang
2. **Generates** a styled meme card you can screenshot and share
3. **Picks the vibe** automatically — or lets you choose from 5 styles

### 🎨 5 Meme Styles

| Style | When It Triggers | Look |
|-------|-----------------|------|
| **Classic** | General/funny content | Bold text on purple gradient |
| **Desi Quote** | Motivational/philosophical | Warm tones with decorative quotes |
| **Roast** | Burns/sarcasm/insults | Dark theme with fire 🔥 |
| **Tech Bro** | Coding/startup/tech talk | Terminal/code aesthetic |
| **Wholesome** | Sweet/emotional messages | Soft pastels with 🫶 |

---

## 🚀 Quick Start

### Install on Your Phone

1. Install **Google AI Edge Gallery** from [Play Store](https://play.google.com/store/apps/details?id=com.google.ai.edge.gallery) or [App Store](https://apps.apple.com/us/app/google-ai-edge-gallery/id6749645337)
2. Download a **Gemma 4** model (E2B or E4B)
3. Go to **Agent Skills** → tap **Skills** chip → tap **(+)**
4. Choose **Import local skill** or **Load from URL**

### Import Methods

**Method A: Local Import**
- Download/clone this repo
- Transfer the `hinglish-meme-generator/` folder to your phone
- Import via Skill Manager → Local Skill

**Method B: From URL**
- In Skill Manager, tap (+) → Load from URL
- Enter: `https://github.com/shubh-vedi/hinglish-meme-generator`

---

## 📱 How to Use

Just chat naturally in the Agent Skills mode:

```
You: "Convert 'I'm not lazy, I'm on energy saving mode' to Hinglish"

AI: Bhai main aalsi nahi hoon, energy saving mode pe hoon 😴⚡
    [Renders a Classic meme card]
```

```
You: "Make a tech bro meme about debugging at 3am"

AI: Raat ke 3 baj rahe hain, bug abhi bhi nahi mila, 
    par chai toh unlimited hai bhai ☕💻
    [Renders a Tech Bro terminal-style card]
```

```
You: "Roast someone who uses light mode IDE"

AI: BHAI LIGHT MODE USE KARTA HAI? SEEDHA SURYA KO
    GHOOR KE CODE KAR NA, SAME VIBE HAI 🔥😎
    [Renders a Roast card with fire theme]
```

---

## 📂 Project Structure

```
hinglish-meme-generator/
├── SKILL.md              # Skill metadata + LLM instructions
├── scripts/
│   └── index.html        # JS skill — renders meme cards in webview
└── README.md
```

---

## 🛠 How It Works

This is a **JS-based Agent Skill** for Google AI Edge Gallery:

1. **SKILL.md** tells the on-device LLM (Gemma 4) how to translate English → Hinglish and which meme style to pick
2. The LLM calls `run_js` with the translation data
3. **scripts/index.html** receives the data via `ai_edge_gallery_get_result()`, renders a styled HTML meme card in a hidden webview
4. The card is displayed to the user — ready to screenshot and share!

Everything runs **100% on-device** — no internet, no API calls, complete privacy.

---

## 🤝 Contributing

Got ideas for new meme styles? Found a better Hinglish translation pattern? PRs welcome!

Some ideas:
- [ ] Add "Bollywood Dialogue" style
- [ ] Add "IPL Commentary" style  
- [ ] Add "Desi Mom" style (for the guilt trip translations 😄)
- [ ] Support for custom watermark text

---

## 📄 License

MIT License — use it, share it, meme it. 🫡

---

## 👨‍💻 Built By

**Shubh Vedi** ([@shubh-vedi](https://github.com/shubh-vedi))

If you found this useful, star ⭐ the repo and share your favorite Hinglish meme in [GitHub Discussions](https://github.com/google-ai-edge/gallery/discussions)!

---

*Built with ❤️ for the desi dev community. Jai Hinglish! 🇮🇳*
