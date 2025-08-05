## EaseMyAI RAG Chatbot

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot using **Ollama + LangChain v0.3**, built to answer queries based on content from [EaseMyAI](https://easemyai.com).

---

### 🚀 Features

* 🔍 Web scraping + chunking of EaseMyAI website
* 🧠 Local embeddings + FAISS vector store
* 🤖 RAG pipeline with LLaMA3 or Phi-3 (via Ollama)
* 💬 Streamlit-based chatbot interface
* 🐳 Dockerized + modular

---

### 🗂️ Structure

```
app/
├── ai/                # LLM, retriever, chain setup
├── config/            # .env and settings
├── easemyai_index/    # FAISS vector DB
├── services/          # ⚠️ One-time setup (scraping + indexing)
├── main.py            # Streamlit UI
├── cli.py            
```

---

### 🐳 Run via Docker

```bash
docker compose up --build
```

* Chatbot runs at: [http://localhost:8501](http://localhost:8501)

---

### 🛠️ Stack

* LangChain v0.3
* Ollama (CPU-based LLMs)
* FAISS (Vector DB)
* Streamlit (UI)
* Docker Compose

---

### 🧪 Example Query

> “What services does EaseMyAI provide?”

---
