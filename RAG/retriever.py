

from vector_embeddings import create_vector_using_faiss

def get_retriever():
    try:
        vec_db = create_vector_using_faiss(type_doc='pdf')
        rt = vec_db.as_retriever(search_type="similarity", search_kwargs={"k": 6})
        return rt
    except Exception as ex:
        print(f'error is coming  from given get retriever :: {ex}')
