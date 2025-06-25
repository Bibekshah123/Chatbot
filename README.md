# PDF Chatbot with DeepSeek R1 API

This project is an AI-powered chatbot that can answer questions from **any uploaded PDF document** and collect user information when asked to "call me".

It uses:
-  LangChain for chaining document retrieval and LLM
-  DeepSeek R1 (chat) API for answering questions
-  FAISS for document embeddings
-  Streamlit for a simple and interactive web interface

---

##  Features

-  Upload any PDF document
-  Ask questions like:
  - "Summarize this document"
  - "What are the main goals?"
  - "Please call me tomorrow"
-  Triggers a **contact form** (Name, Email, Phone, Preferred Date) when user says "call me"
-  Validates form inputs (email, phone number, date)
-  Powered by DeepSeek R1 (free API key)

---


---

##  How to Run Locally

# 1. Clone the Repo
    ```bash
    git clone https://github.com/yourusername/pdf-chatbot-deepseek.git
    cd pdf-chatbot-deepseek

# 2. Create Virtual Environment
      ```bash
      python -m venv venv
      source venv\Scripts\activate

# 3. Install Requirements
      ```bash
      pip install -r requirements.txt

# 4. Add API Key to .env
      ```bash
      DEEPSEEK_API_KEY=sk-your-deepseek-api-key-here

# 5. Run the App
    ```bash
    streamlit run streamlit_app.py







