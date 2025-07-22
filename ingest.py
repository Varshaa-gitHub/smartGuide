import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Folder where your PDFs are stored
pdf_folder = "manuals"

# Collect all PDF file paths
pdf_files = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

# Load all documents
all_docs = []
for pdf_file in pdf_files:
    loader = PyPDFLoader(pdf_file)
    docs = loader.load()
    all_docs.extend(docs)

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(all_docs)

# Embed using HuggingFace
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Save to FAISS
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("family_vectorstore")

print(f"✅ Ingested {len(pdf_files)} PDFs into FAISS.")
