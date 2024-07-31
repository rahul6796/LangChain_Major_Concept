
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores import FAISS

from data_transformers import get_data_transform

class VectorDataBase:

    def __init__(self, doc_type):
        self.doc_type = doc_type
        self.ollama_embs = self.load_embedding()


    def load_embedding(self):
        try:
            ollama_emb = OllamaEmbeddings(
                model='nomic-embed-text', 
                show_progress=True  
            )
            return ollama_emb
        except Exception as ex:
            print(f'error coming from load embedding :: {ex}')




def create_vector_using_chromadb(type_doc):

    try:
        vector_db = VectorDataBase(doc_type=type_doc)
        docs = get_data_transform(doc_typ=type_doc)
        db = Chroma.from_documents(embedding=vector_db.ollama_embs, documents=docs)
        return db
    except Exception as ex:
        print(f'error is coming from given create vector embeddings :: {ex}')


def create_vector_using_faiss(type_doc):
    try:
        vector_db = VectorDataBase(doc_type=type_doc)
        docs = get_data_transform(doc_typ=type_doc)
        db = FAISS.from_documents(embedding=vector_db.ollama_embs, documents=docs)
        return db

    except Exception as ex:
        print(f'error is coming from given create vector using faiss :: {ex}')

if __name__ == "__main__":
    # x = create_vector_using_chromadb(type_doc='pdf')
    x = create_vector_using_faiss(type_doc='pdf')
    print(x)