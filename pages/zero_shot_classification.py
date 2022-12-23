import streamlit as st
from transformers import pipeline
import utils

import importlib
importlib.reload(utils)

@st.cache(allow_output_mutation = True)
def load_zero_shot_classification_model():
    mod = pipeline("zero-shot-classification"
        , model = "facebook/bart-large-mnli")
    return mod

def app():
    # ---- SIDEBAR ----
    options = [
        ''
        , 'Example 1 - Apple - Finance News'
        , 'Example 2 - World Cup - Sports News']

    example = st.sidebar.selectbox(label = 'Examples', options = options)

    default_text = default_categories = ''

    if example == 'Example 1 - Apple - Finance News':
        default_text, default_categories = utils.load_apple_finance()
        
    if example == 'Example 2 - World Cup - Sports News':
        default_text, default_categories = utils.world_cup_sports()
        
    zero_shot_classification = load_zero_shot_classification_model()
    st.title('Zero Shot Classification')
    sentence = st.text_area('Input text', height = 500, value = default_text)
    categories = st.text_input('Input categories', value = default_categories)
    # format the categories as a list
    categories = categories.split(',')
    categories = [category.strip() for category in categories]
    
    button = st.button('Submit')
    with st.spinner('Generating answer . . .'):
        if button and sentence:
            try:
                answers = zero_shot_classification(answer, categories)
                label = answers['labels'][0]
                score = answers['scores'][0] 

                st.write(f'Predicted Category: {label}, Predicted Probability: {score}')
            except:
                st.write('Something went wrong, please try again')


    # Hide Streamlit branding
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html = True)