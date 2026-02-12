# 🚀 Your First LLM App

Build a conversational chatbot using the OpenAI API in under 30 minutes.

## What We're Building

A terminal-based chatbot that:
- Responds to user messages using GPT-4o-mini
- Maintains conversation history
- Has a custom personality/system prompt

## Prerequisites

- Python 3.9+
- OpenAI API key

## Step 1: Setup

```bash
pip install openai python-dotenv
```

Create a `.env` file:
```
OPENAI_API_KEY=sk-your-key-here
```

## Step 2: Hello, LLM!

Let's start with the simplest possible call:

```python
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "What is generative AI in one sentence?"}
    ]
)

print(response.choices[0].message.content)
```

**What's happening:**
1. We create an OpenAI client (it auto-reads `OPENAI_API_KEY` from env)
2. We call the Chat Completions API with a message
3. We extract and print the response

## Step 3: Add a System Prompt

System prompts define your bot's personality:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a friendly coding tutor. Explain concepts simply with examples. Use emojis."
        },
        {
            "role": "user",
            "content": "What is a function in Python?"
        }
    ]
)
```

## Step 4: Build the Chat Loop

Now let's make it conversational:

```python
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

system_prompt = {
    "role": "system",
    "content": (
        "You are a helpful AI assistant. You are concise, friendly, "
        "and always provide practical examples when explaining concepts."
    )
}

conversation = [system_prompt]

print("🤖 AI Chatbot (type 'quit' to exit)\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ("quit", "exit"):
        print("👋 Bye!")
        break

    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation,
        temperature=0.7,
        max_tokens=500,
    )

    reply = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": reply})

    print(f"🤖: {reply}\n")
```

## Step 5: Add Streaming

Make responses appear word-by-word (feels much more natural):

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=conversation,
    stream=True,  # ← Enable streaming
)

print("🤖: ", end="")
full_reply = ""
for chunk in response:
    if chunk.choices[0].delta.content:
        word = chunk.choices[0].delta.content
        print(word, end="", flush=True)
        full_reply += word
print()  # New line after response
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| `model` | Which LLM to use (gpt-4o-mini is fast & cheap) |
| `messages` | The conversation history (system + user + assistant messages) |
| `temperature` | Creativity level (0 = deterministic, 1 = creative) |
| `max_tokens` | Maximum response length |
| `stream` | Whether to stream the response token by token |

## 💰 Cost Tips

- **GPT-4o-mini** costs ~$0.15/M input tokens — extremely affordable
- Keep `max_tokens` reasonable (500 is fine for most responses)
- Use `temperature=0` for factual questions (less retry = less cost)

## Next Steps

- [Prompt Engineering 101](02-prompt-engineering-101.md) — Master prompt techniques
- [RAG Chatbot App](../../apps/rag-chatbot/) — Add document knowledge to your bot
- [LangChain Basics Notebook](../../notebooks/langchain-basics.ipynb) — Level up with frameworks
