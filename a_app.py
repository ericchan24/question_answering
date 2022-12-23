import os
import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import choose_your_task, named_entity_recognition, question_answering, sentiment_analysis, zero_shot_classification

# Create an instance of the app 
app = MultiPage()

# Title of the main page
# st.title('NLP App')

# Add all your application here
app.add_page('', choose_your_task.app)
app.add_page('Named Entity Recognition', named_entity_recognition.app)
app.add_page('Question Answering', question_answering.app)
app.add_page('Sentiment Analysis', sentiment_analysis.app)
app.add_page('Zero Shot Classification', zero_shot_classification.app)

# The main app
app.run()