# 📦 Instructor — Structured Outputs from LLMs

> **TL;DR:** The simplest way to extract structured, validated data from any LLM. Uses Pydantic models to define your output schema.

## Overview

| | |
|---|---|
| **GitHub** | [instructor-ai/instructor](https://github.com/instructor-ai/instructor) |
| **Category** | Structured Output |
| **Stars** | 8,500+ |
| **License** | MIT |
| **Python** | 3.9+ |

## Installation

```bash
pip install instructor openai
```

## Hello World

```python
import instructor
from openai import OpenAI
from pydantic import BaseModel

client = instructor.from_openai(OpenAI())

class UserInfo(BaseModel):
    name: str
    age: int
    email: str

user = client.chat.completions.create(
    model="gpt-4o-mini",
    response_model=UserInfo,
    messages=[
        {"role": "user", "content": "John Doe is 30 years old. Email: john@example.com"}
    ],
)

print(user)
# → UserInfo(name='John Doe', age=30, email='john@example.com')
```

## Extract Multiple Items

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    category: str

products = client.chat.completions.create(
    model="gpt-4o-mini",
    response_model=list[Product],
    messages=[
        {"role": "user", "content": """
        Products: MacBook Pro ($2499, electronics),
        Running Shoes ($120, sports), Coffee Maker ($89, kitchen)
        """}
    ],
)

for p in products:
    print(f"{p.name}: ${p.price} ({p.category})")
```

## With Validation

```python
from pydantic import BaseModel, field_validator

class ValidatedUser(BaseModel):
    name: str
    age: int
    email: str

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, v):
        if v < 0 or v > 150:
            raise ValueError("Age must be between 0 and 150")
        return v

    @field_validator("email")
    @classmethod
    def email_must_contain_at(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email")
        return v
```

## Pros & Cons

### ✅ Pros
- **Dead simple** — Patch OpenAI client and add `response_model`
- **Validation** — Pydantic validators + automatic retries
- **Multi-provider** — OpenAI, Anthropic, Gemini, Ollama, LiteLLM
- **Battle-tested** — Widely used in production
- **Streaming** — Partial streaming of structured outputs
- **Great docs** — Excellent documentation with cookbooks

### ❌ Cons
- **Single purpose** — Only does structured extraction
- **Retry cost** — Validation failures cost extra tokens
- **No agents** — Not an agent framework, just a tool

## Verdict

⭐⭐⭐⭐⭐ (5/5)

Instructor is the gold standard for structured LLM outputs. It does one thing and does it perfectly. If you need to extract data from LLMs, this should be your first choice.

**Best for:** Data extraction, API response parsing, form filling, content classification
**Skip if:** You need agents, chains, or complex workflows
