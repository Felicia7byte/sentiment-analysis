import streamlit as st
from transformers import pipeline

st.title("Sentiment Analysis (English only)")

sentiment = pipeline("sentiment-analysis")

text = st.text_input("Enter your text:")

if text:
    result = sentiment(text)

    st.write("Result:")
    st.write(result)
