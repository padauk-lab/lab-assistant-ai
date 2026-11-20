"""Frontend entry point. Pages call the backend API only, never the database."""

import os

import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Lab Assistant", page_icon="🧪")
st.title("Lab Assistant")
st.caption(f"Backend: {API_URL}")
st.write("Pages for progress, equipment, Q&A, library and chat will be added here.")
