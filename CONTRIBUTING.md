# 🤝 Contributing to Awesome GenAI Toolkit

First off, **thank you** for considering contributing! Every contribution helps make this resource better for the entire GenAI community.

---

## 📋 Table of Contents

- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Contribution Guidelines](#contribution-guidelines)
- [Style Guide](#style-guide)
- [Pull Request Process](#pull-request-process)
- [Good First Issues](#good-first-issues)

---

## How Can I Contribute?

| Type | Description |
|------|-------------|
| 🐛 **Bug Fixes** | Fix broken code, links, or typos |
| ✨ **New Apps** | Add a new GenAI application to `apps/` |
| 📓 **Notebooks** | Add a Jupyter notebook to `notebooks/` |
| 📖 **Tutorials** | Write a tutorial in `tutorials/` |
| 📦 **Library Reviews** | Review a new GenAI library in `new-libraries/` |
| 📚 **Resources** | Add papers, courses, or tools to `resources/` |

---

## Getting Started

1. **Fork** this repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/awesome-genai-toolkit.git
   cd awesome-genai-toolkit
   ```
3. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** and commit:
   ```bash
   git add .
   git commit -m "feat: add XYZ tutorial"
   ```
5. **Push** and open a Pull Request:
   ```bash
   git push origin feature/your-feature-name
   ```

---

## Contribution Guidelines

### Apps
- Each app should live in its own folder under `apps/`
- Include a `README.md` with setup instructions, screenshots, and usage
- Include a `requirements.txt` with pinned dependencies
- Code should be well-commented and production-ready
- Add an "Open in Colab" or "Deploy" button where applicable

### Notebooks
- Must be runnable end-to-end on Google Colab
- Include an "Open in Colab" badge at the top
- Use clear markdown headers to separate sections
- Install dependencies in the first cell with `!pip install`
- Add explanatory markdown between code cells

### Tutorials
- Place in the appropriate level folder (`beginner/`, `intermediate/`, `advanced/`)
- Use numbered prefixes: `01-topic-name.md`
- Include prerequisites, step-by-step instructions, and expected outputs
- Add code snippets that readers can copy-paste

### Library Reviews
- Follow the template in `new-libraries/library-reviews/`
- Include: Overview, Installation, Hello World example, Pros/Cons, Verdict
- Be objective and fair in your assessment

---

## Style Guide

### Naming Conventions
- **Folders**: `kebab-case` (e.g., `rag-chatbot`)
- **Python files**: `snake_case.py` (e.g., `app.py`)
- **Notebooks**: `kebab-case.ipynb` (e.g., `langchain-basics.ipynb`)
- **Markdown**: `kebab-case.md` (e.g., `prompt-engineering-101.md`)

### Code Style
- Python: Follow [PEP 8](https://pep8.org/)
- Use type hints where possible
- Add docstrings to functions and classes
- Keep functions focused and under 50 lines

### Commit Messages
Use [Conventional Commits](https://www.conventionalcommits.org/):
- `feat: add new CrewAI agent tutorial`
- `fix: correct import in RAG chatbot`
- `docs: update README with new badges`
- `chore: update dependencies`

---

## Pull Request Process

1. Ensure your code runs without errors
2. Update the main `README.md` if you've added new content
3. Fill out the PR template describing your changes
4. Wait for review — maintainers will respond within 48 hours
5. Address any feedback and push updates

---

## Good First Issues

Look for issues tagged with `good first issue` — these are perfect for first-time contributors! Examples include:

- 📝 Fix typos or broken links
- 📓 Add "Open in Colab" buttons to notebooks
- 📖 Write a beginner tutorial
- 📚 Add a paper or course to resources

---

## 💬 Questions?

Open an [issue](https://github.com/shubh-vedi/awesome-genai-toolkit/issues) or start a [discussion](https://github.com/shubh-vedi/awesome-genai-toolkit/discussions). We're happy to help!

---

**Thank you for making the GenAI community better! 🚀**
