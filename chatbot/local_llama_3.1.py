from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from langchain_community.llms import Ollama



import streamlit as st
from dotenv import load_dotenv
load_dotenv()

## prompts:

system_template = "You are the helpful assistance. Response the user quries."

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question : {question}")
    ]
)

#streamlit:

st.title('Langchain Demo with Llama 3.1')
input_text = st.text_input('Enter your question')


## llm model:

llm = Ollama(model= 'llama3.1')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question' : input_text}))









