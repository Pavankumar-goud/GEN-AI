import streamlit as st
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# 🔐 Load environment variables from .env file
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# ✅ Initialize Gemini model with API key
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=google_api_key
)

# 🧠 Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful chatbot."),
    ("human", "Question: {question}")
])

# 🛠️ Output Parser
output_parser = StrOutputParser()

# 🔗 Chain everything together
chain = prompt | llm | output_parser

# 🎨 Streamlit App UI
st.title('🤖 PAVAN AI')
input_text = st.text_input("ASK ANY QUESTION TO ME")

if input_text:
    with st.spinner("Thinking..."):
        response = chain.invoke({'question': input_text})
        st.write("**Answer:**", response)
