import streamlit as st
from chatbot import create_qa_chain
from utils import is_valid_email, is_valid_phone, extract_date

st.set_page_config(page_title="AI Chatbot")
st.title("AI Chatbot")

uploaded_file = st.file_uploader("Upload your document (PDF)", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    qa_chain = create_qa_chain("temp.pdf")
    st.success("✅ Document loaded successfully.")

    query = st.text_input("Ask a question or say something like 'Call me tomorrow'")

    if query:
        if "call me" in query.lower() or "appointment" in query.lower():
            st.subheader("Contact Form")

            name = st.text_input("Your Name")
            phone = st.text_input("Phone Number (with country code)")
            email = st.text_input("Email")
            date_text = st.text_input("Preferred Date (e.g., next Friday)")

            date_value = extract_date(date_text)

            if name and is_valid_phone(phone) and is_valid_email(email) and date_value:
                st.success("Appointment Booked!")
                st.write(f"Appointment Date: {date_value}")
                st.write(f"Phone: {phone} | 📧 Email: {email}")
            else:
                st.warning("Please enter valid information.")
        else:
            with st.spinner("Generating response..."):
                answer = qa_chain.run(query)
                st.success("Answer:")
                st.write(answer)
