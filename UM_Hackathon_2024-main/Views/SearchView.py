# This is the view for the search page. It is responsible for rendering the search page and handling the search form.
# pip install streamlit
#import streamlit as st

import streamlit as st
from Utils import ChatGPTAPI, NewsAPI
import streamlit as st
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def search_view():
    st.title("News Search and Sentiment Analysis")
    search_term = st.text_input("Enter search term:", "Bitcoin")
    response = NewsAPI.get_news(search_term, pipeline=sentiment_pipeline)
    search_button = st.button("Search")
    if search_button:
        # Use st.markdown to change text color
        st.markdown(f"<p style='color: green;'>Positive: {response['positive']:.2f}%</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: red;'>Negative: {response['negative']:.2f}%</p>", unsafe_allow_html=True)


        
