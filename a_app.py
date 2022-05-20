import streamlit as st
from transformers import pipeline

@st.cache(allow_output_mutation = True)
def load_qa_model():
    model = pipeline("question-answering")
    return model

qa = load_qa_model()
st.title('Question Answering App')
sentence = st.text_area('Input text', height = 500)
question = st.text_input('Ask a question')
button = st.button('Submit')
with st.spinner('Generating answer . . .'):
    if button and sentence:
        answers = qa(question = question, context = sentence)
        st.write(answers['answer'])