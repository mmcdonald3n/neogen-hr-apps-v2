# -*- coding: utf-8 -*-
import streamlit as st
from utils.house_style import BRAND

st.set_page_config(page_title="Neogen Suite", page_icon=None, layout="wide")

st.title("Neogen Suite")
col1, col2 = st.columns([1,4])
with col1:
    try:
        import os
        if os.path.exists(BRAND.logo_path) and os.path.getsize(BRAND.logo_path) > 0:
            st.image(BRAND.logo_path, width=120)
    except Exception:
        pass
with col2:
    st.markdown("""
Welcome to the Neogen Suite. Use the sidebar to open tools.
- Job Description Generator
- Interview Question Generator
- Policy Generator (beta)
""")

st.sidebar.header("Apps")
st.sidebar.page_link("app.py", label="Home")



