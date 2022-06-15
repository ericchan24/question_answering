from collections import defaultdict
import pandas as pd
import spacy
import streamlit as st
from transformers import pipeline
import utils

import importlib
importlib.reload(utils)
# pd.set_option('max_colwidth', None)

nlp = spacy.load('en_core_web_sm')

@st.cache(allow_output_mutation = True)
def load_sa_model():
    '''sentiment analysis model'''
    model = tokenizer = 'yiyanghkust/finbert-tone'
    mod = pipeline(task = 'sentiment-analysis'
        , model = model
        , tokenizer = tokenizer)
    return mod

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8') 

def app():
    # ---- SIDEBAR ----
    options = [
        ''
        , 'Example 1 - Apple - 2022 Q2 Financial Press Release'
        , 'Example 2 - Tesla - 2021 10-k Filing - Risk Factors']

    example = st.sidebar.selectbox(label = 'Examples', options = options)

    default_text = default_question = ''

    if example == 'Example 1 - Apple - 2022 Q2 Financial Press Release':
        default_text = utils.load_apple_example_sentiment_analysis()
        
    if example == 'Example 2 - Tesla - 2021 10-k Filing - Risk Factors':
        default_text = utils.load_tesla_example_sentiment_analysis()

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
                    sent_rating = sa_mod(sent)[0]['label']
                    sentiment_labels.append(sent_rating)
                    counter[sent_rating] += 1
            
            # print report of positive, negative, neutral comments
            num_pos = counter['Positive']
            num_neg = counter['Negative']
            num_neut = counter['Neutral']

            st.write(f'Number of positive sentences: {num_pos}')
            st.write(f'Number of negative sentences: {num_neg}')
            st.write(f'Number of neutral sentences: {num_neut}')

            # print dataframe of results
            df = pd.DataFrame({'SENTENCE_NUM': sentence_number
                , 'SENTENCE': sentences
                , 'SENTIMENT': sentiment_labels})
            df = df.set_index('SENTENCE_NUM')
            df = df.sort_values(by = ['SENTENCE_NUM'])

            print(df['SENTENCE'].values)
            
            st.dataframe(df, width = 750, height = 250) 

            st.download_button(
                label = 'Download data as CSV'
                , data = convert_df(df)
                , file_name = 'sentiment_analysis.csv'
                , mime = 'text/csv'
            )

    # Hide Streamlit branding
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html = True)