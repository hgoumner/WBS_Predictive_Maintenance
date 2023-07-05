import streamlit as st

with open(r'./data/report.html', 'r') as f:
    html = f.read()

st.components.v1.html(html=html, height=2000, scrolling=True)