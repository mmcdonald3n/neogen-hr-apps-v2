import sys
from pathlib import Path
import streamlit as st
REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from components.layout import app_header  # noqa: E402
from apps.jd_generator.app import render as render_jd  # noqa: E402

st.set_page_config(page_title="Job Description Generator", page_icon="📝", layout="wide")
app_header("Job Description Generator")
st.caption("House Style is centrally controlled. JDs are always generated to Neogen House Style.")
render_jd(embed_mode=True)

