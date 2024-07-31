

import requests
import streamlit as st

def get_response_ollama(input_text):

    response = requests.post("http://0.0.0.0:56421/answer_of_topic/invoke",
                             json={'input': {'topic':input_text}})
    return response.json()['output']


st.title('Llama3.1 ChatBot Model')
input_text = st.text_input('Enter your topic')

if input_text:
    st.write(get_response_ollama(input_text=input_text))


