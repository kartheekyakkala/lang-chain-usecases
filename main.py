import os
from dotenv import load_dotenv
from save_file import save_uploaded_file

load_dotenv()
if os.getenv("OPENAI_API_KEY") is None:
    #please enter your openai api key here
    os.environ["OPENAI_API_KEY"] = "insert your api key here"
from langchain.document_loaders import UnstructuredFileLoader 
loader = UnstructuredFileLoader(f'./Bhagavad_Gita_As_It_Is.pdf')
from langchain.indexes import VectorstoreIndexCreator
index = VectorstoreIndexCreator().from_loaders([loader])
def get_response(user_input):
    return index.query(user_input)
st = 'True'
while st!= '' or st.lower() != "stop":
    st = input('Human: ')
    print('AI: ' + get_response(st))