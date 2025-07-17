# 🤖 AgentHub: Local Multi-Agent AI System

AgentHub is a modular multi-agent AI system built with LangChain, Streamlit, and local LLMs. It supports RAG from PDFs, CSV cleaning, SQL querying, summarization, and a dual-mode (voice/text) assistant—all running **offline** with fast local inference.

[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

---

## 🚀 Features

| Agent         | Description                                             |
|---------------|---------------------------------------------------------|
| 📄 PDF RAG     | Ask questions from PDFs using local vector search (FAISS) |
| 📝 Summarizer  | Summarize long text files with Transformers             |
| 🧹 CSV Cleaner | Clean noisy datasets, remove duplicates, empty values   |
| 💾 SQL Agent   | Query local MySQL databases in natural language         |
| 🎙 Voice Agent | Dual-mode AI assistant: Voice 🎤 + Text ⌨️ input/output   |

---

## 🧠 Tech Stack

- **LangChain** for agent orchestration
- **LLM**: Local quantized LLaMA/Mistral via `llama-cpp-python`
- **Embeddings**: SentenceTransformers (`all-MiniLM-L6-v2`)
- **Vector Store**: FAISS
- **Speech Recognition**: OpenAI `whisper`
- **Text-to-Speech**: `pyttsx3`
- **UI**: Streamlit

---

## 🎙 Voice Agent (Offline Voice + Text Assistant)

This agent allows fully offline voice and text interaction with your local LLM.

### 🔹 Features:
- 🎤 **Voice Input** (via mic) using `Whisper`
- ⌨️ **Text Input** (manual entry)
- 🧠 **LLM Response** using `llama-cpp-python` with TinyLLaMA or Mistral GGUF
- 🔊 **Voice Output** using `pyttsx3` with a background TTS queue
- ✅ **Thread-safe & Streamlit-compatible**

### 🔧 Modes Available:
- Select **Input Mode** from Sidebar:
  - `🎤 Voice` – Press “Start Listening”
  - `⌨️ Text` – Enter your prompt manually
- Displays response on screen and speaks it aloud

---

## 🛠 Setup (Python 3.10 Recommended)

```bash
# Step 1: Create virtual environment (Python 3.10 recommended)
python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate (Linux/macOS)

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Place your GGUF LLM model in /models directory
# Step 4: Run the app
streamlit run app.py
```

---

## 🧪 Demo Use Cases

- Ask questions from your semester notes (PDF)
- Summarize research papers or book chapters (TXT)
- Clean student data before visualization (CSV)
- Convert plain English to MySQL queries
- Ask GenAI questions using voice or text locally

---

## 📂 Project Structure

```
AgentHub/
├── agents/
│   ├── rag_agent.py
│   ├── summarizer_agent.py
│   ├── cleaner_agent.py
│   ├── sql_agent.py
│   └── voice_agent.py
├── tool/
│   ├── sql_tool.py
├── util/
│   ├── logger.py
├── db/
│   ├── employeel.py        #it's an demo File
├── models/                 # GGUF model files here
├── uploads/                # Uploaded user files
├── app.py
├── test_db.py
├── test_local_llm.py
├── test_env.py
└── README.md
```

---
Built with ❤️ by Pranav Bhatt

🔗 GitHub: https://github.com/Pranav-1111 🔗 LinkedIn: https://linkedin.com/in/pranavbhatt

## 📝 License

Licensed under the **Apache License 2.0**. See the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) file for details.
