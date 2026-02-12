# 🏗️ Multi-Agent Architectures

A deep dive into design patterns for building multi-agent systems that actually work.

## Overview

Multi-agent systems use multiple specialized AI agents that collaborate to solve complex tasks. This tutorial covers the major architectural patterns, when to use each, and production considerations.

## Pattern 1: Sequential Pipeline

Agents execute in a fixed order, each building on the previous output.

```
Agent A → Agent B → Agent C → Final Output
```

**Best for:** Content creation, data processing pipelines, ETL

```python
"""
Example: Research → Write → Edit pipeline
"""
from crewai import Agent, Task, Crew, Process

researcher = Agent(role="Researcher", goal="Find accurate information", ...)
writer = Agent(role="Writer", goal="Create engaging content", ...)
editor = Agent(role="Editor", goal="Polish and fact-check", ...)

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process=Process.sequential,
)
```

**Pros:** Simple, predictable, easy to debug
**Cons:** No parallelism, failure in one stage blocks everything

---

## Pattern 2: Hierarchical (Manager + Workers)

A manager agent delegates tasks to specialized workers.

```
         ┌──────────┐
         │ Manager  │
         └────┬─────┘
      ┌───────┼───────┐
      ▼       ▼       ▼
  ┌──────┐ ┌──────┐ ┌──────┐
  │Worker│ │Worker│ │Worker│
  │  A   │ │  B   │ │  C   │
  └──────┘ └──────┘ └──────┘
```

**Best for:** Complex tasks with independent subtasks

```python
crew = Crew(
    agents=[manager, researcher, analyst, writer],
    tasks=[complex_task],
    process=Process.hierarchical,
    manager_agent=manager,
)
```

**Pros:** Dynamic task allocation, parallel execution possible
**Cons:** Manager is a single point of failure, higher token usage

---

## Pattern 3: Debate / Adversarial

Two agents argue for/against a position, a judge decides.

```
  ┌────────┐     ┌────────┐
  │ Pro    │◄───▶│ Con    │
  │ Agent  │     │ Agent  │
  └────┬───┘     └────┬───┘
       └──────┬───────┘
              ▼
        ┌──────────┐
        │  Judge   │
        └──────────┘
```

**Best for:** Decision-making, code review, risk assessment

---

## Pattern 4: Tool-Augmented Agents

Agents equipped with tools to interact with external systems.

```python
from crewai_tools import SerperDevTool, FileReadTool, CodeInterpreterTool

agent = Agent(
    role="Data Analyst",
    tools=[
        SerperDevTool(),           # Web search
        FileReadTool(),            # Read files
        CodeInterpreterTool(),     # Run code
    ],
)
```

**Tool Design Principles:**
1. Tools should do one thing well
2. Clear input/output contracts
3. Handle errors gracefully
4. Include retry logic for external APIs

---

## Pattern 5: Reflection / Self-Improvement

An agent generates output, then critiques and improves its own work.

```
Generate → Critique → Revise → Critique → Final
```

```python
def reflect_and_improve(task: str, max_iterations: int = 3) -> str:
    # Generate initial output
    output = generate(task)

    for i in range(max_iterations):
        # Self-critique
        critique = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Critically review this output. List specific improvements."},
                {"role": "user", "content": f"Task: {task}\n\nOutput:\n{output}"},
            ],
        ).choices[0].message.content

        # Check if good enough
        if "no improvements needed" in critique.lower():
            break

        # Revise
        output = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Revise the output based on the critique."},
                {"role": "user", "content": f"Original:\n{output}\n\nCritique:\n{critique}"},
            ],
        ).choices[0].message.content

    return output
```

---

## Production Considerations

### Error Handling
```python
# Always implement retry logic
import time

def retry_with_backoff(func, max_retries=3):
    for i in range(max_retries):
        try:
            return func()
        except Exception as e:
            if i == max_retries - 1:
                raise
            time.sleep(2 ** i)
```

### Cost Management
- Use cheaper models (gpt-4o-mini) for simple agent tasks
- Reserve GPT-4o for complex reasoning and final outputs
- Set `max_tokens` limits per agent
- Cache repeated queries

### Observability
- Log every agent action and tool call
- Track token usage per agent
- Monitor task completion times
- Set up alerts for failures

## Choosing the Right Pattern

| Scenario | Pattern | Why |
|----------|---------|-----|
| Blog writing | Sequential | Natural flow: research → write → edit |
| Customer support | Hierarchical | Route to the right specialist |
| Investment decisions | Debate | Need balanced analysis |
| Data analysis | Tool-Augmented | Need to query databases, run code |
| Code generation | Reflection | Iterative improvement works best |

## Next Steps

- Build a multi-agent app with [CrewAI](../../apps/ai-agent/)
- Try the [CrewAI notebook](../../notebooks/crewai-agents.ipynb)
- Explore [new agent frameworks](../../new-libraries/weekly-drops.md)
