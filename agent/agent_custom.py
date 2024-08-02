
from langchain_community.document_loaders import WebBaseLoader
import bs4

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool
from langchain_community.embeddings import OllamaEmbeddings



def load_custom_data():
    try:
        loader = WebBaseLoader(web_path='https://docs.smith.langchain.com/')
        text_docs = loader.load()
        return text_docs

    except Exception as ex:
        print(f'error is coming get data from webbase :: {ex}')

def load_embedding():
    try:
        ollama_emb = OllamaEmbeddings(
            model='nomic-embed-text', 
            show_progress=True  
        )
        return ollama_emb
    except Exception as ex:
        print(f'error coming from load embedding :: {ex}')



def custom_agent_tool():
    emb = load_embedding()
    doc_loader = load_custom_data()
    document = RecursiveCharacterTextSplitter(chunk_size =1000, chunk_overlap = 100)
    docs = document.split_documents(documents=doc_loader)

    vectorstore = FAISS.from_documents(documents=docs, embedding=emb)
    retriever = vectorstore.as_retriever()
    retriever_tool = create_retriever_tool(retriever, 'langsmith_search',
                                           'Search for information about langsmith. for any question about langsmith you must used this tool')
    return retriever_tool

# if __name__ == "__main__":
#     main()








