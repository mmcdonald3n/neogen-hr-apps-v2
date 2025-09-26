# -*- coding: utf-8 -*-
import streamlit as st
from utils.house_style import BRAND
from pathlib import Path

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
    st.write("Welcome to the Neogen Suite. Use the sidebar or the tiles below.")

st.divider()
st.subheader("Tools")

# Tiles with page links (use script paths relative to repo root)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("### Job Description Generator")
    st.page_link("pages/12_JD_Generator.py", label="Open JD Generator", icon="📄")
with c2:
    st.markdown("### Interview Question Generator")
    st.page_link("pages/2_Interview_Question_Generator.py", label="Open IVQ Generator", icon="🗒️")
with c3:
    st.markdown("### Job Advert Generator")
    st.page_link("pages/3_Job_Advert_Generator.py", label="Open Advert Generator", icon="📢")

st.sidebar.header("Apps")
st.sidebar.page_link("app.py", label="Home")
st.sidebar.page_link("pages/12_JD_Generator.py", label="Job Description Generator")
st.sidebar.page_link("pages/2_Interview_Question_Generator.py", label="Interview Question Generator")
st.sidebar.page_link("pages/3_Job_Advert_Generator.py", label="Job Advert Generator")
