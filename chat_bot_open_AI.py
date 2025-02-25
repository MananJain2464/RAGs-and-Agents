from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 

import streamlit as st 
import os 
from dotenv import load_dotenv 

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true" # LANGSMITH TRACKING 


prompt = ChatPromptTemplate.from_messages(
    [
        ("system" , "You are a helpful assistan. Please response to the queries "),
        ("user" , "Question: {question}")
    ]
)

st.title('Langchain Demo with OpenAI API')
input_text = st.text_input("Search the topic you want")


llm = ChatOpenAI(model = 'gpt-3.5-turbo')
output_parser = StrOutputParser()
chain= prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
    