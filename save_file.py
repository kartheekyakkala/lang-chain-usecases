import os
import streamlit as st

def save_uploaded_file(uploadedfile):
    current_directory = os.getcwd()
    with open(os.path.join(current_directory, "doc.txt"), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved file :{} in Current working directory".format("doc.txt"))
