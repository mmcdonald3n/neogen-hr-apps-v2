# -*- coding: utf-8 -*-
import os, streamlit as st
from utils.house_style import BRAND

st.set_page_config(page_title="Neogen — FitScore", page_icon=None, layout="wide")

left, right = st.columns([1,6])
with left:
    try:
        if os.path.exists(BRAND.logo_path) and os.path.getsize(BRAND.logo_path) > 0:
            st.image(BRAND.logo_path, width=110)
    except Exception:
        pass
with right:
    st.title("FitScore")
    st.caption("Simple rubric-driven scoring to support decisions.")

st.info("This is a placeholder wired into the Neogen Suite. We’ll iteratively replace this page with the full feature set.")
st.markdown("- Output will follow the Neogen house style.\n- Exports: DOCX / Markdown.\n- Model controls in sidebar.\n- Accessibility & inclusive language baked in.")


