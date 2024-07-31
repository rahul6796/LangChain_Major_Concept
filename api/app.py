

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes

import uvicorn
import os

from langchain_community.llms import Ollama

from dotenv import load_dotenv
load_dotenv()



app = FastAPI(
    title = "Langchain server",
    version  = "1.0",
    description = "A simple llm  server"

)


# model
llm = Ollama(model= 'llama3.1')

## prompt

prompt = ChatPromptTemplate.from_template(
    """
you are the AI assistent which you can provide the accurate answer related the topic which i will given
to you {topic}
"""
)

add_routes(
    app,
    prompt|llm,
    path = '/answer_of_topic'
)


if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 0000)










