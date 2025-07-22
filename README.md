

# **Smart Family Guide (RAG Chatbot)**

This project is a **Retrieval-Augmented Generation (RAG) application** that allows you to upload PDF manuals and query them through an intelligent chatbot. The chatbot retrieves relevant content from the uploaded manuals using vector embeddings and answers questions accurately.

---

## **Project Structure**

```
smartFamilyGuide/
│
├── app.py               # Main chatbot application
├── ingest.py            # Script to process and embed PDF manuals
├── rag_chain.py         # RAG pipeline implementation
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (ignored in Git)
├── .gitignore           # Git ignore rules
│
├── env/                 # Virtual environment (ignored in Git)
├── family_vectorstore/  # Vector database (ignored in Git)
├── manuals/             # PDF manuals (ignored in Git)
└── __pycache__/         # Python cache (ignored in Git)
```

---

## **Setup Instructions**

### **1. Clone or Download Project**

```bash
git clone https://github.com/<your-username>/smartFamilyGuide.git
cd smartFamilyGuide
```

---

### **2. Create and Activate Virtual Environment**

```bash
python -m venv env
```

* **Windows:**

  ```bash
  env\Scripts\activate
  ```
* **Linux/Mac:**

  ```bash
  source env/bin/activate
  ```

---

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

### **4. Add `.env` File**

Create a `.env` file in the root directory with the following keys:

```
OPENAI_API_KEY=your_openai_api_key
VECTOR_DB_PATH=./family_vectorstore
```

*(This file is **ignored in Git** for security.)*

---

### **5. Add Your Manuals**

Place your PDF manuals inside the `manuals/` directory.

---

### **6. Run Ingestion Script**

```bash
python ingest.py
```

This will process the manuals and build the vector embeddings in `family_vectorstore/`.

---

### **7. Start the Chatbot**

```bash
python app.py
```

---


