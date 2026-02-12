# 📦 DSPy — Programmatic Prompt Optimization

> **TL;DR:** Stop hand-writing prompts. DSPy compiles high-level programs into optimized prompts automatically.

## Overview

| | |
|---|---|
| **GitHub** | [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) |
| **Category** | Prompt Optimization |
| **Stars** | 20,000+ |
| **License** | MIT |
| **Origin** | Stanford NLP |
| **Python** | 3.9+ |

## Installation

```bash
pip install dspy
```

## Hello World

```python
import dspy

# Configure the LM
lm = dspy.LM("openai/gpt-4o-mini")
dspy.configure(lm=lm)

# Define a simple module
qa = dspy.Predict("question -> answer")
result = qa(question="What is the capital of France?")
print(result.answer)
```

## Key Concept: Signatures

Instead of writing prompts, you write **signatures** — declarative descriptions of what you want:

```python
# Simple question-answer
qa = dspy.Predict("question -> answer")

# Summarization
summarizer = dspy.Predict("document -> summary")

# Classification
classifier = dspy.Predict("text -> label, confidence")

# With descriptions
detailed = dspy.Predict(
    "context: str, question: str -> reasoning: str, answer: str"
)
```

## Chain of Thought (Built-in)

```python
# Automatically adds reasoning steps
cot = dspy.ChainOfThought("question -> answer")
result = cot(question="If I have 3 apples and give away 2, how many do I have?")
print(result.reasoning)  # Step-by-step thinking
print(result.answer)     # "1 apple"
```

## RAG with DSPy

```python
class RAG(dspy.Module):
    def __init__(self, num_passages=3):
        super().__init__()
        self.retrieve = dspy.Retrieve(k=num_passages)
        self.generate = dspy.ChainOfThought("context, question -> answer")

    def forward(self, question):
        context = self.retrieve(question).passages
        answer = self.generate(context=context, question=question)
        return answer

rag = RAG()
result = rag("What are the benefits of RAG?")
print(result.answer)
```

## Pros & Cons

### ✅ Pros
- **No prompt engineering** — Define what, not how
- **Automatic optimization** — Compiles to optimized prompts
- **Composable** — Build complex pipelines from simple modules
- **Research-backed** — From Stanford NLP group
- **Metrics-driven** — Optimize for your specific metrics
- **Active community** — Rapidly growing ecosystem

### ❌ Cons
- **Steep learning curve** — New paradigm takes time to learn
- **Training data needed** — Optimization requires examples
- **Debugging** — Compiled prompts can be hard to understand
- **Overhead** — Overkill for simple use cases

## Verdict

⭐⭐⭐⭐ (4/5)

DSPy is a paradigm shift in how we build LLM applications. Instead of hand-tuning prompts, you write programs and let DSPy optimize them. It's academic in origin but increasingly production-ready.

**Best for:** Complex LLM pipelines, teams tired of prompt engineering, production systems
**Skip if:** You need something simple and quick, or have very few examples for optimization
