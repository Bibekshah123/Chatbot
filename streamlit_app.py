import streamlit as st
from chatbot import create_qa_chain
from utils import is_valid_email, is_valid_phone, extract_date
import os

st.set_page_config(page_title="📄 PDF Q&A + Contact Bot", page_icon="🤖")
st.title("🤖 Ask Anything from Your PDF")

# 📄 Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Initialize session state to store chain
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

if uploaded_file:
    # Save file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    st.session_state.qa_chain = create_qa_chain("temp.pdf")
    st.success("✅ PDF loaded successfully. Ask me anything!")

# 🧠 Ask Question
if st.session_state.qa_chain:
    query = st.text_input("📝 Ask a question about the PDF (or say 'call me'):")

    if query:
        if "call me" in query.lower() or "appointment" in query.lower():
            st.subheader("📞 Contact Form")

            name = st.text_input("Full Name")
            phone = st.text_input("Phone Number")
            email = st.text_input("Email Address")
            preferred_date = st.text_input("Preferred Contact Date (e.g., next Monday)")
            parsed_date = extract_date(preferred_date)

            if name and is_valid_phone(phone) and is_valid_email(email) and parsed_date:
                st.success("✅ Form submitted successfully!")
                st.write(f"📅 Date: {parsed_date}")
                st.write(f"📞 Phone: {phone} | 📧 Email: {email}")
            else:
                st.warning("⚠️ Please fill in all fields correctly.")
        else:
            with st.spinner("Thinking..."):
                response = st.session_state.qa_chain.run(query)
                st.success("💬 Answer:")
                st.write(response)
