from langchain.chains import RetrievalQA
from langchain_deepseek import ChatDeepSeek  # or langchain_google_genai for Gemini
from document_loader import load_and_embed
from dotenv import load_dotenv
import os

load_dotenv()

def create_qa_chain(file_path):
    db = load_and_embed(file_path)
    retriever = db.as_retriever()

    llm = ChatDeepSeek(
        model="deepseek-reasoner",  # or "deepseek-chat"
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )

    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
