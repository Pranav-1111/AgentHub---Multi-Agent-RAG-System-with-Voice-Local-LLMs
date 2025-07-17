# test_env.py
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config.env")
print("✅ HUGGINGFACEHUB_API_TOKEN =", os.getenv("HUGGINGFACEHUB_API_TOKEN"))
