# 🧠 Mythos-AI

> A multi-persona, memory-driven AI system that simulates evolving intelligence through distinct behavioral agents.

Built by **Blvck**, Mythos-AI is an experimental conversational framework where intelligence is not singular—but distributed across multiple persistent personas, each with its own identity, tone, and decision patterns.

It blends LLM orchestration, long-term memory, and behavioral routing to create the illusion of a system that doesn’t just respond… but persists.

---

## 🎬 Live Demo — Mythos-AI

A real-time demonstration of Mythos-AI showcasing:
multi-persona switching (Hades, Athena, Ares),
memory-driven responses, and dynamic routing logic.

[![Watch Demo](https://img.youtube.com/vi/rr7qmFmsxBU/0.jpg)](https://www.youtube.com/watch?v=rr7qmFmsxBU)

## ⚡ Overview

It is a multi-agent cognitive system designed to simulate independent personalities that react differently to the same user based on context, memory, and internal state.

```text
User Input
    ↓
Intent + Context Parser
    ↓
Routing Engine (Policy Layer)
    ↓
Persona Selection
    ↓
Memory Retrieval Layer (FAISS + Logs + State)
    ↓
Prompt Construction Engine
    ↓
LLM Dispatch Layer (Multi-Provider)
    ↓
Response Post-Processing
    ↓
Memory + State Persistence
```

The result is a system that feels less like AI output—and more like interacting with distinct minds.

---

## ⚙️ System Architecture

                         ┌────────────────────┐
                         │      User Input    │
                         └─────────┬──────────┘
                                   ↓
                    ┌────────────────────────────┐
                    │   Intent Classification    │
                    └─────────┬──────────────────┘
                              ↓
                    ┌────────────────────────────┐
                    │     Routing Engine         │
                    └─────────┬──────────────────┘
                              ↓
        ┌────────────────────────────────────────────┐
        │          Persona Selection Layer           │
        │           Hades | Athena | Ares            │
        └───────────────┬────────────────────────────┘
                        ↓
        ┌────────────────────────────────────────────┐
        │        Memory Orchestration Layer          │
        │  - FAISS Vector Search                     │
        │  - JSONL Conversation Logs                 │
        │  - Persistent User State                   │
        └───────────────┬────────────────────────────┘
                        ↓
        ┌────────────────────────────────────────────┐
        │        Prompt Construction Engine          │
        │  - Persona Templates                       │
        │  - Memory Injection                        │
        │  - State Conditioning                      │
        └───────────────┬────────────────────────────┘
                        ↓
        ┌────────────────────────────────────────────┐
        │          LLM Dispatch Layer                │
        │  Gemini / Groq / HF / Local Models         │
        └───────────────┬────────────────────────────┘
                        ↓
        ┌────────────────────────────────────────────┐
        │         Response Assembly Layer            │
        └───────────────┬────────────────────────────┘
                        ↓
        ┌────────────────────────────────────────────┐
        │      Memory + State Update System          │
        └────────────────────────────────────────────┘

---


## 🎭 Personas

### 🖤 Hades — The Observer
“I remember what others discard.”

- Calm, stoic, and detached  
- Deep memory orientation  
- Minimal but meaningful speech  
- Pattern-focused reasoning  

Hades acts as the memory core of the system.

---

### 🌿 Athena — The Interpreter
“Understanding comes before response.”

- Warm, thoughtful, and analytical  
- Context-aware reasoning  
- Structured communication style  
- Balances emotion and logic  

Athena serves as the reasoning layer.

---

### ⚔️ Ares — The Instinct
“Act first. Refine later.”

- Fast, energetic, direct  
- Action-driven responses  
- Simple, high-impact communication  
- Low hesitation behavior  

Ares represents the execution layer.

---

## 🧠 Core Features

### Multi-Persona Routing
Dynamic selection of personas based on user input, context, and internal routing logic. Each persona behaves as an independent cognitive agent.

---

### Persistent Memory System
- User-specific memory storage  
- Conversation logs (log.jsonl)  
- Behavioral state tracking (state.json)  
- Long-term interaction continuity  

The system evolves based on repeated interaction patterns.

---

### Semantic Memory (FAISS)
Vector-based retrieval of past conversations enabling long-term contextual recall beyond immediate chat history.

---

### Multi-Model LLM Routing
Supports multiple inference providers:
- Gemini  
- Groq  
- HuggingFace  
- Local models (Phi / Ollama-compatible)

Includes fallback routing for reliability.

---

### Behavioral Prompt Engine
Every response is shaped by persona rules, memory state, recent chat context, and routing decisions.

---

## 🏗️ Architecture

User (Discord)
↓
Bot Interface (main/bot.py)
↓
Router Engine (router/)
↓
Persona Selector (Hades / Athena / Ares)
↓
Prompt Builder
↓
LLM Layer (Gemini / Groq / Local fallback)
↓
Memory System (FAISS + JSON state)
↓
Response returned to user

---

## 🧩 Project Structure

engine/        core chat engine + orchestration
router/        persona + routing logic
llm/           multi-provider LLM interfaces
brain/         memory + behavior evolution
memory/        persistent user logs and state
data/          FAISS index + embeddings
main/          Discord bot runtime
scrapers/      conversation ingestion tools
tests/         debugging and evaluation

---

## 🔥 What makes Mythos-AI different

Most AI systems are:
- single model
- stateless
- no identity persistence

Mythos-AI is:
- multi-persona
- memory-driven
- dynamically routed
- behaviorally consistent over time

It simulates intelligence as a system of interacting identities rather than a single model.

---

## 🧠 Design Philosophy

1. Identity over output  
2. Memory as behavior  
3. Distributed cognition  

---

## 🚀 Future Improvements

- Emotional state modeling per persona  
- Self-evolving personality traits  
- Web memory visualization dashboard  
- Plugin-based persona system  
- Reinforcement-based behavior tuning  

---

## 🖤 Creator

Blvck

Mythos-AI explores what happens when AI stops being a chatbot—and starts becoming a system of minds.

---

## 📜 License

MIT License
