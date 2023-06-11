import os
import os
from dotenv import load_dotenv
import streamlit as st
import os
import streamlit as st
from save_file import save_uploaded_file

uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf"])

if uploaded_file is not None:
    # Perform any processing or analysis on the uploaded file here
    st.write(f"File uploaded: {uploaded_file.name}")
    save_uploaded_file(uploaded_file)
else:
    st.write("No file uploaded.")


load_dotenv()
if os.getenv("OPENAI_API_KEY") is None:
    #please enter your openai api key here
    os.environ["OPENAI_API_KEY"] = "insert your api key here"
from langchain.document_loaders import UnstructuredFileLoader 
loader = UnstructuredFileLoader(f'./doc.txt')
from langchain.indexes import VectorstoreIndexCreator
index = VectorstoreIndexCreator().from_loaders([loader])
def get_response(user_input):
    return index.query(user_input)
st = 'True'
while st!= '' or st.lower() != "stop":
    st = input('Human: ')
    print('AI: ' + get_response(st))