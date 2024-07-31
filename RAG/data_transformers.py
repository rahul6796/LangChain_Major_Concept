

from langchain.text_splitter import RecursiveCharacterTextSplitter
from data_ingestions import get_data_from_txtfile, get_data_from_webbase, get_data_from_pdf


def get_data_transform(doc_typ):
    try:
        
        docs = None
        if doc_typ == 'text_file':
            docs = get_data_from_txtfile()
            
        elif doc_typ == 'pdf':
            docs = get_data_from_pdf()

        else:
            docs = get_data_from_webbase()

        text_spliter = RecursiveCharacterTextSplitter(chunk_size = 1000,
                                                     chunk_overlap = 100)
        text_documents = text_spliter.split_documents(docs)
        return text_documents
    except Exception as ex:
        print(f'error is coming from get data transfrom :: {ex}')




if __name__ == "__main__":
    x = get_data_transform('pdf')
    print(x)
