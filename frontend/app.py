import streamlit as st
from pages import home

st.set_page_config(page_title="Manufacturing Performance Predictor", page_icon="⚙️", layout="centered")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home"])

if page == "Home":
    home.render()
