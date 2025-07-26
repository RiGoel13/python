import streamlit as st
import PyPDF2
import tempfile

st.set_page_config(page_title="PDF Reader", layout="centered")
st.title("📄 Simple PDF Reader App")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    reader = PyPDF2.PdfReader(tmp_file_path)
    st.success(f"PDF has {len(reader.pages)} pages.")

    for i, page in enumerate(reader.pages):
        with st.expander(f"Page {i+1}"):
            st.write(page.extract_text())
