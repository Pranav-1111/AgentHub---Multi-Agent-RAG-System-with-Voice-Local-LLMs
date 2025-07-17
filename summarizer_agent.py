# agents/summarizer_agent.py

from llama_cpp import Llama

class SummarizerAgent:
    def __init__(self):
        self.llm = self.load_llm()

    @staticmethod
    def load_llm():
        return Llama(
            model_path="./models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
            n_ctx=1024,
            n_threads=6
        )

    def summarize_text(self, text):
        prompt = f"""
### Instruction:
Summarize the following text clearly and concisely.

### Text:
{text}

### Summary:
"""

        response = self.llm(prompt, max_tokens=256)
        return response['choices'][0]['text'].strip()
