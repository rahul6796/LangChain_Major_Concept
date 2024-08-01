

from langchain.chains.combine_documents import create_stuff_documents_chain
from prompt_template import prompt 
from load_llm_models import LoadllmModel


def chain():
    try:
        llm = LoadllmModel().load_llm_model()
        documents_chain = create_stuff_documents_chain(prompt=prompt, llm=llm)
        return documents_chain

    except Exception as ex:
        print(f'error is coming from given chain :: {ex}')
