# agents/rag_agent.py

import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from llama_cpp import Llama
import tempfile
import pickle

class RAGAgent:
    def __init__(self):
        self.llm = self.load_llm()
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vector_store = None

    @staticmethod
    def load_llm():
        return Llama(
            model_path="./models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
            n_ctx=1024,
            n_threads=6
        )

    def load_pdf(self, file):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            loader = PyPDFLoader(tmp.name)
            pages = loader.load()
        return " ".join([p.page_content for p in pages])

    def create_chunks(self, text):
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_text(text)
        return chunks

    def build_vector_store(self, chunks):
        self.vector_store = FAISS.from_texts(chunks, self.embeddings)

    def answer_question(self, question):
        if self.vector_store is None:
            return "❌ No PDF data available."
        docs = self.vector_store.similarity_search(question, k=2)
        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
### Instruction:
Answer the question based on the context below.

### Context:
{context}

### Question:
{question}

### Answer:
"""

        result = self.llm(prompt, max_tokens=256)
        return result['choices'][0]['text'].strip()
