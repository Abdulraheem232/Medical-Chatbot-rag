import streamlit as st
from connect_memory_with_llm import qa_chain

st.title("Medical Ai chatbot")
st.write("A ai medical chatbot made using rag technoloy and groq")
text_query = st.text_area(height=250,placeholder="Enter your query related to medical here..",label="Medical query")
submit_button = st.button("Enter")


if submit_button or text_query:
   response = qa_chain.invoke({"query":text_query})
   st.chat_message("ai").markdown(response["result"])
   st.write("Source")
   sources = response["source_documents"][0]
   st.code(f"Page {sources.metadata["page"]} out of {sources.metadata["total_pages"]} of {sources.metadata["source"]}")