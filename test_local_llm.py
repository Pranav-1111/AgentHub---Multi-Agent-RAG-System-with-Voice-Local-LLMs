# test_local_llm.py

from llm_local import LocalMistral

llm = LocalMistral()
response = llm.generate("Summarize: Artificial Intelligence is transforming industries across the globe.")
print("🧠 Response:\n", response)
