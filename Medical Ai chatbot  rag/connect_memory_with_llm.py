from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from os import environ 
import dotenv
from langchain_community.vectorstores import FAISS

dotenv.load_dotenv()

model_name = "llama3-8b-8192"  # Open-access alternative

def load_llm(model_name):
    llm = ChatGroq(
    temperature=0,
    groq_api_key=environ["API_KEY"],
    model_name=model_name
    )
    return llm


CUSTOM_PROMPT_TEMPLATE = """
Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context

Context: {context}
Question: {question}

Start the answer directly. No small talk please.
"""

def set_custom_prompt(custom_prompt_template):
    prompt=PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])
    return prompt

DB_FAISS_PATH="vectorstore/db_faiss"
embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db=FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)

qa_chain = RetrievalQA.from_chain_type(
    llm=load_llm(model_name),
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={"k":3}),
    return_source_documents=True,
    chain_type_kwargs={"prompt":set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)}
)

