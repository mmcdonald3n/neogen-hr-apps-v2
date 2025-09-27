import streamlit as st
from pathlib import Path

NEOGEN_TITLE = "Neogen Suite"
NEOGEN_SUB = "HR Tools • Talent Acquisition • Automation"
LOGO_PATH = Path("assets/neogen-logo.png")  # Drop your real logo here

def header():
    cols = st.columns([1,8])
    with cols[0]:
        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), use_column_width=True)
    with cols[1]:
        st.markdown(f"# {NEOGEN_TITLE}")
        st.caption(NEOGEN_SUB)
    st.divider()

def footer():
    st.divider()
    st.caption("© Neogen • Internal HR Tools")
