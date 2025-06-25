from langchain.chains import RetrievalQA
from langchain_deepseek import ChatDeepSeek
from document_loader import load_and_embed
from dotenv import load_dotenv
import os

load_dotenv()

def create_qa_chain(file_path):
    vectorstore = load_and_embed(file_path)
    retriever = vectorstore.as_retriever()

    llm = ChatDeepSeek(
        model="deepseek-chat",
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )

    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
