
---

## 🩺 Medical RAG Chatbot

This is a **RAG (Retrieval-Augmented Generation)**-based chatbot built with **LangChain**, **Streamlit**, and **LLMs** (e.g., LLaMA via Groq API). It answers **medical questions** based on a local PDF document, providing context-grounded responses using vector embeddings and retrieval.

---

### 📂 Features

* 🔍 Ask detailed medical questions based on your PDF (e.g., "Java Notes.pdf")
* 🧠 Uses **FAISS** for document indexing & search
* 💬 Interactive **chat interface via Streamlit**
* 🔗 Integrates with **Groq API** (e.g., LLaMA3)
* 📚 Cites source page numbers from the PDF
* 🧠 Embeddings via **HuggingFace BGE model**

---

### 🛠️ Tech Stack

* Python 🐍
* [LangChain](https://www.langchain.com/)
* [Streamlit](https://streamlit.io/)
* [FAISS](https://github.com/facebookresearch/faiss)
* Hugging Face Transformers
* Groq (for LLM inference)

---

### 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Example `requirements.txt` (add this to your project if missing):

```
streamlit
langchain
langchain-community
langchain-groq
faiss-cpu
huggingface-hub
sentence-transformers
python-dotenv
```

---

### 🔐 Environment Setup

Create a `.env` file in the root directory with:

```env
API_KEY=your_groq_api_key_here
```

---

---

### 🚀 Run the App

Launch your chatbot using:

```bash
streamlit run your_script_name.py
```

Example:

```bash
streamlit run medical_chatbot.py
```

---

### 💬 Example Query

> "What are the symptoms of diabetes?"

The model responds with factual answers from the PDF and includes page references when available.

---

### 📌 Notes

* The app does **not** generate responses beyond the given PDF context.
* If no relevant context is found, the chatbot replies:
  *"I cannot answer this based on the document."*
* Adjust `chunk_size` and `chunk_overlap` for better vectorization results.

---

### 🧪 Future Improvements

* Upload new PDFs via UI
* Multilingual support
* Add memory or chat history context
* Improved medical validation (e.g., PubMed integration)

---

### 📜 License

MIT License (or specify your preferred license)

---


