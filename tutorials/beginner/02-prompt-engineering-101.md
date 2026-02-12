# 🎯 Prompt Engineering 101

Master the art of crafting prompts that get consistently great results from LLMs.

## Why Prompt Engineering Matters

The same model can give you a 2/10 or 10/10 answer — the difference is how you ask.

## Technique 1: Be Specific

❌ **Bad prompt:**
```
Tell me about Python
```

✅ **Good prompt:**
```
Explain Python's list comprehension syntax with 3 practical examples,
each increasing in complexity. Show the equivalent for-loop version
for comparison.
```

## Technique 2: Role Prompting

Give the model a persona to adopt:

```python
messages = [
    {
        "role": "system",
        "content": "You are a senior Python developer with 15 years of experience. "
                   "You write clean, Pythonic code following PEP 8. You always explain "
                   "WHY a pattern is preferred, not just WHAT it does."
    },
    {
        "role": "user",
        "content": "Review this code and suggest improvements: ..."
    }
]
```

## Technique 3: Few-Shot Examples

Show the model what you want:

```
Convert these product descriptions to JSON:

Input: "Nike Air Max 90 - Classic sneaker in white/black, size 10, priced at $120"
Output: {"brand": "Nike", "model": "Air Max 90", "color": "white/black", "size": 10, "price": 120}

Input: "Adidas Ultraboost 22 - Running shoe in navy blue, size 9, priced at $180"
Output: {"brand": "Adidas", "model": "Ultraboost 22", "color": "navy blue", "size": 9, "price": 180}

Input: "New Balance 574 - Retro sneaker in grey/red, size 11, priced at $89"
Output:
```

## Technique 4: Chain of Thought (CoT)

Force step-by-step reasoning:

```
Solve this problem step by step:

A store has 150 items. 40% are electronics, and 25% of electronics are on sale.
How many electronics items are on sale?

Think through this step by step before giving the final answer.
```

## Technique 5: Output Formatting

Tell the model exactly how to format the response:

```
Analyze this text for sentiment. Respond in this exact format:

**Sentiment:** [Positive/Negative/Neutral]
**Confidence:** [High/Medium/Low]
**Key phrases:** [comma-separated list]
**Summary:** [one sentence]
```

## Technique 6: Constraints

Set boundaries to get focused answers:

```
Explain quantum computing to a 10-year-old.
- Use at most 100 words
- Use an analogy from everyday life
- No technical jargon
- End with a fun fact
```

## Technique 7: Structured Decomposition

Break complex tasks into steps:

```
I want you to write a blog post about AI in healthcare.

Step 1: Generate 5 possible titles (catchy, SEO-friendly)
Step 2: Create an outline with 5 sections
Step 3: Write the introduction (150 words)
Step 4: Write each section (200 words each)
Step 5: Write a conclusion with a call-to-action

Start with Step 1.
```

## Quick Reference Card

| Technique | When to Use | Example Trigger |
|-----------|-------------|-----------------|
| Be Specific | Always | Add details, constraints, format |
| Role Prompting | Expert tasks | "You are a..." |
| Few-Shot | Pattern matching | Show 2-3 examples |
| Chain of Thought | Math/logic | "Think step by step" |
| Output Formatting | Structured data | "Respond in this format" |
| Constraints | Focused output | Word limits, audience level |
| Decomposition | Complex tasks | "Step 1... Step 2..." |

## Common Mistakes

1. **Too vague** — "Make it better" → "Improve readability by using shorter sentences and active voice"
2. **Too long** — Don't write an essay-prompt. Be concise and clear.
3. **No examples** — For data extraction, always show 1-2 examples
4. **Ignoring temperature** — Use `0` for factual, `0.7-1.0` for creative tasks

## Next Steps

- Try these techniques in the [LangChain Basics](../../notebooks/langchain-basics.ipynb) notebook
- Build a prompt testing framework with [DSPy](../../notebooks/dspy-intro.ipynb)
- Move to [Intermediate Tutorials](../intermediate/) for RAG and agents
