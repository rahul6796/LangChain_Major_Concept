

from retriever import get_retriever
from chain import chain
from langchain.chains import create_retrieval_chain

import streamlit as st 



if __name__ == "__main__":



    rt = get_retriever()
    question_answer_chain = chain()
    rag_chain = create_retrieval_chain(rt, question_answer_chain)
    
    st.title('Chat With your PDF by using LLama3.1 ')
    input_text = st.text_input('Enter your question')
    if input_text:
        response = rag_chain.invoke({"input": {input_text} })
        st.write(response["answer"])
    
