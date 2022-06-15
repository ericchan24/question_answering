import spacy
import spacy_streamlit
import streamlit as st
import utils

import importlib
importlib.reload(utils)
# pd.set_option('max_colwidth', None)

nlp = spacy.load('en_core_web_sm')

# @st.cache(allow_output_mutation = True)
# def load_sa_model():
#     '''sentiment analysis model'''
#     model = tokenizer = 'yiyanghkust/finbert-tone'
#     mod = pipeline(task = 'sentiment-analysis'
#         , model = model
#         , tokenizer = tokenizer)
#     return mod

# @st.cache
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode('utf-8') 

def app():
    # ---- SIDEBAR ----
    options = [
        ''
        , 'Example 1 - Apple - Wikipedia'
        , 'Example 2 - Tesla - Board of Directors']

    example = st.sidebar.selectbox(label = 'Examples', options = options)

    default_text = ''

    if example == 'Example 1 - Apple - Wikipedia':
        default_text, _ = utils.load_apple_example()
        
    if example == 'Example 2 - Tesla - Board of Directors':
        default_text = utils.load_tesla_example_ner()

    # sa_mod = load_sa_model()
    st.title('Named Entity Recognition')
    input_text = st.text_area('Input text', height = 500, value = default_text)

    button = st.button('Submit')
    with st.spinner('Generating answer . . .'):
        if button and input_text:
            doc = nlp(input_text)
            spacy_streamlit.visualize_ner(doc
                , labels = nlp.get_pipe('ner').labels)

    # Hide Streamlit branding
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html = True)