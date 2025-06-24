from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from document_loader import load_and_embed
from dotenv import load_dotenv
import os

load_dotenv()

def create_qa_chain(file_path):
    db = load_and_embed(file_path)
    retriever = db.as_retriever()

    llm = ChatOpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    return qa_chain
