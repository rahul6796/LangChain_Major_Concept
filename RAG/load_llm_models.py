

from langchain_community.llms import Ollama


class LoadllmModel:

    def load_llm_model():
        return Ollama(model = 'llama3.1')

