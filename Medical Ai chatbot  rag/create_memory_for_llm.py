from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores.faiss import FAISS

#Load raw file

DATA_PATH = "data/"
def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    return documents

documents = load_pdf_files(DATA_PATH)

def create_chunks(extracted_data):
    text_split = RecursiveCharacterTextSplitter(chunk_size=500,
                                                chunk_overlap=50)
    text_chunks = text_split.split_documents(extracted_data)
    return text_chunks

text_chunks = create_chunks(documents)

def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model

embedding_model = get_embedding_model()
DB_FAISS_PATH = "vectorstore/db_faiss"
vectorstore = FAISS.from_documents(text_chunks,embedding_model)
vectorstore.save_local(DB_FAISS_PATH)

