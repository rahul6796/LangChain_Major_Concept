

from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader

import os
import bs4

base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))



def get_data_from_txtfile():
    try:
        file_name = base_dir + '/data/llm_text_file.txt'
        loader = TextLoader(file_name)
        text_documents = loader.load()
        return text_documents
    except Exception as ex:
        print(f'error is coming form given data loader :: {ex}')


def get_data_from_webbase():
    try:
        loader = WebBaseLoader(
            web_path='https://lilianweng.github.io/posts/2024-07-07-hallucination/',
            bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                class_=("post-content", "post-title", "post-header")
            )

        ))

        text_docs = loader.load()
        return text_docs

    except Exception as ex:
        print(f'error is coming get data from webbase :: {ex}')


def get_data_from_pdf():
    try:
        file_path_name = base_dir + '/data/1910.01108v4.pdf'
        loader = PyPDFLoader(file_path=file_path_name)
        text_documents = loader.load()
        return text_documents
    except Exception as ex:
        print(f'error is coming form given get data from pdf :: {ex}')




if __name__ == "__main__":
    # x = get_text_loader()
    # x = get_data_from_webbase()
    x = get_data_from_pdf()
    print(x)