import streamlit as st

st.set_page_config(page_title="Nuz Crochet", layout="wide")

st.components.v1.iframe(
    "https://nuz-crochet.netlify.app/",
    height=1000,
    scrolling=True
)
