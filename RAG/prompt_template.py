
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
Answer the following questions based on to provided context.
think step by step before providing the detailed answer.
if you do not know the answe simple reply us to Sorry i will not provide the answer.


<context>
{context}
</context>
Question: {input}                             
""")

