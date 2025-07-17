# 🧠 AgentHub — Multi-Agent AI Assistant (Offline, Fast, Modular)

AgentHub is a fully offline, modular AI system powered by local LLMs like **TinyLlama** or **Mistral**, built using `llama-cpp-python`, `Streamlit`, and `LangChain`. It supports:
- 📄 **PDF Question Answering (RAG)**
- 💬 **Text Summarization**
- 📊 **CSV Cleaner**
- 🧠 **Natural Language SQL Agent**
- 🎙️ **Voice-to-AI Assistant** (Whisper + Local TTS)

---

## 🚀 Features

| Agent Type      | Description                                         |
|-----------------|-----------------------------------------------------|
| **RAG Agent**   | Ask questions from uploaded PDFs using FAISS + LLM  |
| **SQL Agent**   | Ask natural questions, get SQL result from MySQL    |
| **Summarizer**  | Upload text files for summarization (offline LLM)   |
| **CSV Cleaner** | Remove nulls/duplicates from CSV automatically      |
| **Voice Agent** | Speak to AI — transcribe using Whisper, answer with LLM, speak reply locally |

---

## 🖥️ Tech Stack

- **LLMs**: `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` or `mistral-7b.Q4_K_M.gguf`
- **Frameworks**: Streamlit, LangChain
- **Embeddings**: `all-MiniLM-L6-v2` (HuggingFace Transformers)
- **Vector Store**: FAISS
- **Voice Input**: OpenAI `whisper`
- **Voice Output**: `pyttsx3` (thread-safe via `queue`)
- **Database**: MySQL (XAMPP or local)

---

## 📁 Project Structure

```
Agent_Hub/
├── app.py                      # Main Streamlit app
├── models/                     # GGUF models (TinyLlama here)
├── uploads/                    # Temp upload folder
├── agents/
│   ├── rag_agent.py            # PDF QA (RAG)
│   ├── sql_agent.py            # Natural SQL Agent
│   ├── summarizer_agent.py     # Text summarizer
│   ├── cleaner_agent.py        # CSV cleaner
│   └── voice_agent.py          # Voice assistant
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔧 1. Clone or Download

```bash
git clone https://github.com/your-username/AgentHub.git
cd AgentHub
```

### 📦 2. Install Requirements

Make sure you're on **Python 3.10+** (not 3.13 for compatibility). Then:

```bash
pip install -r requirements.txt
```

> If `llama-cpp-python` fails, install CMake + VS Build Tools and use:
```bash
pip install llama-cpp-python --no-cache-dir
```

### 🧠 3. Download GGUF Model

Download **TinyLlama (fastest)**:

👉 [tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/blob/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)

> Place in `Agent_Hub/models/`

---

## 🧪 How to Run

### ✅ Start the App

```bash
streamlit run app.py
```

### 📂 Modes in Sidebar:
- `"PDF QA (RAG)"`
- `"Summarize Text"`
- `"SQL Query"`
- `"Clean CSV"`
- `"Voice Assistant"`

---

## ✅ MySQL Setup

Use **XAMPP** or install MySQL locally.

In your `sql_agent.py`, change DB config:
```python
self.connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",     # if any
    database="employee_db"
)
```

Add a sample `employees` table to test:
```sql
CREATE TABLE employees (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  department VARCHAR(255),
  salary INT
);

INSERT INTO employees (name, department, salary)
VALUES ('Alice', 'AI', 50000), ('Bob', 'HR', 40000);
```

---

## 🎙 Voice Assistant Setup

Uses `speech_recognition` and Google Web Speech API (default, free).

Make sure:
- Mic is working
- You allow browser access to mic when prompted

---

## 💡 Future Ideas

- Add memory for multi-turn conversations
- Replace voice API with `whisper.cpp` for full offline
- Add GUI enhancements with `ShadCN + Tailwind` + FastAPI backend

---

## 📦 `requirements.txt` (Minimal Version)

```
streamlit
llama-cpp-python
langchain
sentence-transformers
faiss-cpu
pypdf
mysql-connector-python
speechrecognition
```

---

## 🧠 Built By

👤 **Pranav Bhatt**  

