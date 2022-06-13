import pandas as pd
import spacy
import streamlit as st
from transformers import pipeline
import utils

import importlib
importlib.reload(utils)
pd.set_option('max_colwidth', None)

nlp = spacy.load('en_core_web_sm')

@st.cache(allow_output_mutation = True)
def load_sa_model():
    '''sentiment analysis model'''
    model = tokenizer = 'ProsusAI/finbert'
    mod = pipeline(task = 'sentiment-analysis'
        , model = model
        , tokenizer = tokenizer)
    return mod

def app():
    # ---- SIDEBAR ----
    # options = [
    #     ''
    #     , 'Example 1 - Apple - Wikipedia'
    #     , 'Example 2 - Tesla - 2020 10-k Filing']

    # example = st.sidebar.selectbox(label = 'Examples', options = options)

    default_text = default_question = ''

    # if example == 'Example 1 - Apple - Wikipedia':
    #     default_text, default_question = utils.load_apple_example()
        
    # if example == 'Example 2 - Tesla - 2020 10-k Filing':
    #     default_text, default_question = utils.load_tesla_example()

    sa_mod = load_sa_model()
    st.title('Sentiment Analysis')
    input_text = st.text_area('Input text', height = 500, value = default_text)

    button = st.button('Submit')
    with st.spinner('Generating answer . . .'):
        if button and input_text:
#             sentiment_arr = sa_mod(input_text)
#             st.write(sentiment_arr[0]['label'])

            sentence_number = []
            sentences = []
            sentiment_labels = []

            # use spacy to seperate sentences
            doc = nlp(input_text)
            counter = defaultdict(int)
            sent_dict = defaultdict(list)
            for i, sent in enumerate(doc.sents, 1):
                sent = sent.text.strip()
                if sent:    
                    sentence_number.append(i)
                    sentences.append(sent)
                    # use the model to find the sentiment (positive, negative, or neutral)
                    sent_rating = mod(sent)[0]['label']
                    sentiment_labels.append(sent_rating)
                    counter[sent_rating] += 1

            df = pd.DataFrame({'SENTENCE NUM': sentence_number
                , 'SENTENCE': sentences
                , 'SENTIMENT': sentiment_labels})

            st.dataframe(df)  # Same as st.write(df)
    # Hide Streamlit branding
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html = True)