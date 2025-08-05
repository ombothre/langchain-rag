## EaseMyAI RAG Chatbot

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot for EaseMyAI.It leverages the **LangChain** framework and a CPU-based **Ollama** LLM to intelligently answer user queries based on content scraped from the [EaseMyAI website](https://easemyai.com).

-----

### 🚀 **Features**

  * **Web Scraper:** Ingests content directly from the EaseMyAI website.
  * **Local Vector Store:** Uses **FAISS** to store document embeddings for fast, local retrieval.
  * **RAG Pipeline:** Integrates a local LLM (e.g., `phi3`) with the vector store via **Ollama** and **LangChain** to generate context-aware answers.
  * **Web Interface:** A simple and interactive chatbot UI built with **Streamlit**.
  * **Containerized:** Fully containerized with **Docker**, allowing for easy setup and offline execution.

-----

### 🗂️ **Project Structure**

```
app/
├── ai/                # Core AI logic: LLM, retriever, and chain setup
│   └── components/
├── config/            # Configuration files and settings
├── easemyai_index/    # Stores the local FAISS vector database
├── services/          # One-time services for data scraping and indexing
│   ├── rag_setup/
│   └── scraper/
├── main.py            # Entrypoint for the Streamlit UI
├── cli.py             # Command-line interface for interaction
└── ...
```

-----

### 🐳 **Run with Docker**

**Prerequisites:**

  * Docker installed.
  * Ollama service running with a model pulled (e.g., `ollama pull phi3`).

To build and run the application, execute the following command from the project root:

```bash
docker compose up --build
```

The chatbot will be accessible at: **[http://localhost:8501](https://www.google.com/search?q=http://localhost:8501)**

-----

### 🛠️ **Tech Stack**

  * **Orchestration:** LangChain
  * **LLM Framework:** Ollama (for CPU-based models like `phi3`)
  * **Vector Database:** FAISS (Local)
  * **UI:** Streamlit
  * **Containerization:** Docker, Docker Compose

-----

### 🧪 **Example Query**

> "What services does EaseMyAI provide?"