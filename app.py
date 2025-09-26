import streamlit as st
from utils.house_style import BRAND

st.set_page_config(page_title="Neogen Suite", page_icon="🧭", layout="wide")

st.title("Neogen Suite")
col1, col2 = st.columns([1,4])
with col1:
    try:
        st.image(BRAND.logo_path, width=120)
    except Exception:
        st.write("")
with col2:
    st.markdown("""
Welcome to the Neogen Suite. Use the sidebar to open tools.
- Job Description Generator
- Interview Question Generator
- Policy Generator (beta)
""")

st.sidebar.header("Apps")
st.sidebar.page_link("app.py", label="🏠 Home")
