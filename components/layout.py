from pathlib import Path
import streamlit as st
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[1]
ASSETS = REPO_ROOT / "assets"

def _load_logo():
    p = ASSETS / "neogen_logo.png"
    try:
        return Image.open(p) if p.exists() else None
    except Exception:
        return None

def app_header(title: str):
    logo = _load_logo()
    c1, c2 = st.columns([6, 1], vertical_alignment="center")
    with c1:
        st.title(title)
        st.caption("HR Tools • Talent Acquisition • Automation")
    with c2:
        if logo is not None:
            st.image(logo, use_column_width=True)
