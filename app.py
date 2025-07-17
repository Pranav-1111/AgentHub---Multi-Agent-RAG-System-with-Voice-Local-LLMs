# app.py
import os
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

import os
import streamlit as st
from agents.rag_agent import RAGAgent
from agents.summarizer_agent import SummarizerAgent
from agents.cleaner_agent import CSVCleaner
from agents.sql_agent import SQLAgent  # Optional if added
import speech_recognition as sr
import pyttsx3
from agents.voice_agent import VoiceAgent


# Initialize agents
rag = RAGAgent()
summarizer = SummarizerAgent()
cleaner = CSVCleaner()
sql = SQLAgent()
voice_agent = VoiceAgent()

# Streamlit UI
st.set_page_config(page_title="AgentHub - Multi-Agent AI", layout="wide")
st.title("🤖 AgentHub: Your Local Multi-Agent AI System")
st.markdown("---")

# Sidebar mode selection
mode = st.sidebar.radio("Choose Mode", ["PDF QA (RAG)", "Summarize Text", "Clean CSV", "SQL Query","Voice Agent"])


# ========== MODE 1: PDF RAG ==========
if mode == "PDF QA (RAG)":
    st.header("📄 Ask Questions from a PDF")
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"], key="pdf")
    
    if uploaded_file:
        text = rag.load_pdf(uploaded_file)
        chunks = rag.create_chunks(text)
        rag.build_vector_store(chunks)
        st.success("✅ PDF processed and indexed!")

        question = st.text_input("💬 Ask your question:")
        if question:
            with st.spinner("Thinking..."):
                answer = rag.answer_question(question)
            st.markdown(f"**🧠 Answer:** {answer}")

# ========== MODE 2: Summarizer ==========
elif mode == "Summarize Text":
    st.header("📝 Summarize a TXT Document")
    uploaded_file = st.file_uploader("Upload a TXT file", type=["txt"], key="txt")

    if uploaded_file:
        text = uploaded_file.read().decode("utf-8")
        with st.spinner("Summarizing..."):
            summary = summarizer.summarize_text(text)
        st.text_area("📄 Summary", summary, height=200)

# ========== MODE 3: CSV Cleaner ==========
elif mode == "Clean CSV":
    st.header("🧹 Clean a CSV File")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"], key="csv")

    if uploaded_file:
        upload_path = os.path.join("uploads", uploaded_file.name)
        with open(upload_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        cleaned_path, before, after = cleaner.clean_csv(upload_path)
        st.success(f"✅ Cleaned CSV saved: {cleaned_path}")
        st.info(f"📊 Rows before: {before} → after: {after}")

        with open(cleaned_path, "rb") as file:
            st.download_button("⬇️ Download Cleaned CSV", file, file_name="cleaned.csv")

# ========== MODE 4: SQL Agent ==========
elif mode == "SQL Query":
    st.header("💾 Ask Questions from a MySQL Database")
    query = st.text_input("Enter your question for the database:")

    if st.button("Submit") and query:
        with st.spinner("Querying..."):
            try:
                result = sql.run_query(query)
                st.success("✅ Answered successfully!")
                st.write(result)
            except Exception as e:
                st.error(f"❌ Error: {e}")


elif mode == "Voice Agent":
    st.header("🎙️ Voice Assistant")

    input_mode = st.radio("Select Input Mode", ["🎤 Voice", "⌨️ Text"], horizontal=True)

    if input_mode == "🎤 Voice":
        if st.button("🎤 Start Listening"):
            with st.spinner("🎙️ Listening for voice input..."):
                query, response = voice_agent.run()
            st.info(f"🗣️ You said: {query}")
            if response.strip():
                st.success(f"🧠 AI Response: {response}")
            else:
                st.warning("⚠️ No response from AI. Try rephrasing.")
    else:
        query = st.text_input("💬 Enter your question:")
        if st.button("Submit"):
            with st.spinner("Thinking..."):
                response = voice_agent.ask_llm(query)
                voice_agent.speak_response(response)
            st.success(f"🧠 AI Response: {response}")
