# llm_local.py

from llama_cpp import Llama

class LocalMistral:
    def __init__(self, model_path="./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"):
        self.model = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=12  # adjust based on your CPU
        )

    def generate(self, prompt, max_tokens=512):
        response = self.model(
            prompt=f"[INST] {prompt} [/INST]",
            max_tokens=max_tokens,
            stop=["</s>"],
            echo=False
        )
        return response['choices'][0]['text'].strip()
