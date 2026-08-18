import streamlit as st

st.set_page_config(page_title="Nuz Crochet", layout="wide")

st.title("Nuz Crochet")
st.write("Nuz Crochet ki live website dekhne ke liye neeche button dabao:")

st.link_button("🌐 Visit Nuz Crochet Website", "https://nuz-crochet.netlify.app/")

st.markdown("---")

# Try embedding too - works only if the target site allows framing
st.write("Agar neeche preview load ho jaye toh theek, warna upar wala button use karo:")
st.components.v1.iframe(
    "https://nuz-crochet.netlify.app/",
    height=800,
    scrolling=True
)
