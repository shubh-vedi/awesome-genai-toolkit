"""
🤖 AI Agent Team — Streamlit UI
Multi-agent research & writing pipeline with CrewAI.
"""

import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

load_dotenv()

# ── Page Config ────────────────────────────────────────────────
st.set_page_config(page_title="🤖 AI Agent Team", page_icon="🤖", layout="wide")

st.markdown("""
<style>
    .stApp { max-width: 1000px; margin: 0 auto; }
    .agent-card { padding: 1rem; border-radius: 10px; border: 1px solid #333; margin: 0.5rem 0; }
</style>
""", unsafe_allow_html=True)


# ── Define Agents ──────────────────────────────────────────────
def create_agents(model: str = "gpt-4o-mini"):
    researcher = Agent(
        role="Senior Research Analyst",
        goal="Research and gather comprehensive information on the given topic",
        backstory=(
            "You are a world-class research analyst with expertise in finding "
            "and synthesizing information from multiple sources. You are thorough, "
            "accurate, and always cite your sources."
        ),
        verbose=False,
        allow_delegation=False,
        llm=model,
    )

    writer = Agent(
        role="Content Writer",
        goal="Create well-structured, engaging content based on research findings",
        backstory=(
            "You are an expert content writer specializing in technology and AI. "
            "You take complex research and turn it into clear, actionable content "
            "that readers love."
        ),
        verbose=False,
        allow_delegation=False,
        llm=model,
    )

    editor = Agent(
        role="Quality Editor",
        goal="Review and polish content for accuracy, clarity, and engagement",
        backstory=(
            "You are a meticulous editor with years of experience in tech publishing. "
            "You ensure every piece is factually correct, well-organized, and "
            "free of errors."
        ),
        verbose=False,
        allow_delegation=False,
        llm=model,
    )

    return researcher, writer, editor


def run_crew(topic: str, agents: tuple, word_count: int = 800):
    researcher, writer, editor = agents

    research_task = Task(
        description=(
            f"Research the topic: '{topic}'\n\n"
            "Gather information from your knowledge. Include:\n"
            "1. Overview and current state\n"
            "2. Key players and technologies\n"
            "3. Recent developments\n"
            "4. Trends and predictions\n"
            "5. Practical applications"
        ),
        expected_output="A comprehensive research report with key findings",
        agent=researcher,
    )

    writing_task = Task(
        description=(
            f"Write a detailed article about '{topic}' based on the research.\n\n"
            f"The article should be approximately {word_count} words.\n"
            "Include:\n"
            "1. Compelling introduction\n"
            "2. Clear headers and sections\n"
            "3. Practical examples\n"
            "4. Key takeaways"
        ),
        expected_output="A well-written, engaging article ready for publication",
        agent=writer,
    )

    editing_task = Task(
        description=(
            "Review and edit the article for:\n"
            "1. Factual accuracy\n"
            "2. Grammar and spelling\n"
            "3. Flow and readability\n"
            "4. Technical accuracy\n\n"
            "Provide the final polished version."
        ),
        expected_output="A polished, publication-ready article",
        agent=editor,
    )

    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, writing_task, editing_task],
        process=Process.sequential,
        verbose=False,
    )

    return crew.kickoff()


# ── Sidebar ────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuration")

    api_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key

    st.divider()

    model = st.selectbox("Model", ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"], index=0)
    word_count = st.slider("Target Word Count", 300, 2000, 800, step=100)

    st.divider()
    st.markdown("### 🤖 Agent Team")
    st.markdown("""
    **Researcher** — Gathers information  
    **Writer** — Creates the article  
    **Editor** — Polishes the final output
    """)


# ── Main Content ───────────────────────────────────────────────
st.title("🤖 AI Agent Team")
st.caption("A multi-agent system that researches, writes, and edits content on any topic")

# Topic input
col1, col2 = st.columns([4, 1])
with col1:
    topic = st.text_input("📝 Enter a topic to research", placeholder="e.g. The current state of AI agents in 2025")
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    run_button = st.button("🚀 Run Crew", type="primary", use_container_width=True)

# Example topics
st.markdown("**💡 Try:** `AI agents in production` · `RAG vs fine-tuning` · `Open source LLMs landscape` · `AI in healthcare 2025`")

st.divider()

# Run the crew
if run_button and topic:
    if not api_key:
        st.error("⚠️ Please enter your OpenAI API key in the sidebar")
    else:
        agents = create_agents(model)

        # Progress indicators
        progress = st.progress(0)
        status = st.status("🚀 Running Agent Crew...", expanded=True)

        with status:
            st.write("🔍 **Researcher** is gathering information...")
            progress.progress(10)

            try:
                result = run_crew(topic, agents, word_count)
                progress.progress(100)

                st.write("✅ All agents completed!")
                status.update(label="✅ Crew Finished!", state="complete")

            except Exception as e:
                status.update(label="❌ Error", state="error")
                st.error(f"Error: {e}")
                result = None

        if result:
            st.divider()
            st.subheader("📄 Final Output")
            st.markdown(str(result))

            # Download button
            st.download_button(
                label="📥 Download as Markdown",
                data=str(result),
                file_name=f"{topic[:30].replace(' ', '_')}.md",
                mime="text/markdown",
                use_container_width=True,
            )

elif run_button and not topic:
    st.warning("Please enter a topic first!")
