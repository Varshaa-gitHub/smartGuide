import streamlit as st
from rag_chain import load_rag_chain

st.set_page_config(page_title="Smart Family Guide", layout="wide")
st.title("🧠 Smart Family Guide (RAG + Groq)")

# Load chain
qa_chain = load_rag_chain()

# UI
query = st.text_input("Ask me anything about the document:", placeholder="e.g. What is the process mentioned on page 3?")
if query:
    with st.spinner("Thinking..."):
        answer = qa_chain.run(query)
        st.success(answer)
