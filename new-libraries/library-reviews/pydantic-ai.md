# 📦 Pydantic AI — Type-Safe Agent Framework

> **TL;DR:** Pydantic AI brings type safety and validation to AI agents. Built by the Pydantic team, it's like FastAPI but for AI.

## Overview

| | |
|---|---|
| **GitHub** | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) |
| **Category** | Agent Framework |
| **Stars** | 5,200+ |
| **License** | MIT |
| **Python** | 3.9+ |

## Installation

```bash
pip install pydantic-ai
```

## Hello World

```python
from pydantic_ai import Agent

agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="You are a helpful assistant that gives concise answers.",
)

# Simple text response
result = agent.run_sync("What is the capital of France?")
print(result.data)
# → "The capital of France is Paris."
```

## Structured Output Example

```python
from pydantic import BaseModel
from pydantic_ai import Agent

class CityInfo(BaseModel):
    name: str
    country: str
    population: int
    fun_fact: str

agent = Agent(
    "openai:gpt-4o-mini",
    result_type=CityInfo,
    system_prompt="Provide accurate city information.",
)

result = agent.run_sync("Tell me about Tokyo")
city = result.data

print(f"{city.name}, {city.country}")
print(f"Population: {city.population:,}")
print(f"Fun fact: {city.fun_fact}")
```

## Tool Usage

```python
from pydantic_ai import Agent, RunContext

agent = Agent("openai:gpt-4o-mini")

@agent.tool
async def get_weather(ctx: RunContext, city: str) -> str:
    """Get the current weather for a city."""
    # In production, call a real weather API
    return f"Sunny, 25°C in {city}"

result = agent.run_sync("What's the weather in London?")
print(result.data)
```

## Pros & Cons

### ✅ Pros
- **Type safety** — Pydantic validation for inputs and outputs
- **Familiar API** — If you know FastAPI, you know this
- **Multi-model** — OpenAI, Anthropic, Gemini, Groq, Ollama
- **Streaming** — Built-in support for streamed responses
- **Dependencies** — Clean dependency injection system
- **Active development** — Backed by the Pydantic team

### ❌ Cons
- **Young project** — API still evolving
- **Less ecosystem** — Fewer tools compared to LangChain
- **Limited multi-agent** — No built-in multi-agent orchestration (yet)

## Verdict

⭐⭐⭐⭐ (4/5)

Pydantic AI is excellent for building **type-safe, production-grade AI apps**. If you value clean code and strong typing, this is your framework. It's not yet as feature-rich as LangChain for complex workflows, but for single-agent apps with structured outputs, it's arguably the best choice.

**Best for:** Production apps needing validated I/O, developers who love Pydantic/FastAPI
**Skip if:** You need complex multi-agent orchestration or extensive tool ecosystems
