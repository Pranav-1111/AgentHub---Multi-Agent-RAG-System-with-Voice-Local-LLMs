import streamlit as st
token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

 # ✅ This must be above HuggingFaceHub import

from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub

class SQLAgent:
    def __init__(self):
        # Set up the MySQL connection
        self.db = SQLDatabase.from_uri(
            "mysql+mysqlconnector://root@localhost/employee_db"
        )

        # Set up TinyLlama model
        self.llm = HuggingFaceHub(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    huggingfacehub_api_token=st.secrets["HUGGINGFACEHUB_API_TOKEN"],
    model_kwargs={"temperature": 0.2, "max_new_tokens": 256},
)


        # Optional: Custom Prompt Template
        _DEFAULT_TEMPLATE = """
        Based on the following input question, write the correct SQL query and return the final answer:
        Question: {query}
        SQLQuery: 
        """

        prompt = PromptTemplate(
            input_variables=["query"],
            template=_DEFAULT_TEMPLATE,
        )

        self.chain = SQLDatabaseChain.from_llm(
            llm=self.llm,
            db=self.db,
            prompt=prompt,
            verbose=True
        )

    def run_query(self, query: str) -> str:  # ✅ Now inside the class
        try:
            response = self.chain.run({"query": query})
            return response
        except Exception as e:
            return f"❌ Error: {str(e)}"
