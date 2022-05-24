import streamlit as st
from transformers import pipeline
import utils

@st.cache(allow_output_mutation = True)
def load_qa_model():
    model = tokenizer = 'deepset/roberta-base-squad2'
    mod = pipeline(task = "question-answering", model = model, tokenizer = tokenizer)
    return mod

# ---- SIDEBAR ----
options = [
    ''
    , 'Example 1 - Apple']

example = st.sidebar.selectbox(label = 'Examples', options = options)

default_text = default_question = ''

if example == 'Example 1 - Apple':
    default_text, default_question = utils.load_apple_example()

qa = load_qa_model()
st.title('Question Answering App')
sentence = st.text_area('Input text', height = 500, value = default_text)
question = st.text_input('Ask a question', value = default_question)
button = st.button('Submit')
with st.spinner('Generating answer . . .'):
    if button and sentence:
        answers = qa(question = question, context = sentence)
        st.write(answers['answer'])

# Hide Streamlit branding
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html = True)