import sys
from pathlib import Path
import streamlit as st

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from components.layout import app_header  # noqa: E402

st.set_page_config(page_title="Neogen Suite", page_icon="🧪", layout="wide")

app_header("Neogen Suite")
st.write("Welcome to the Neogen Suite. Use the sidebar or the tiles below.")

st.subheader("Tools")

def tile(title, desc):
    with st.container(border=True):
        st.caption("Tool")
        st.subheader(title)
        st.write(desc)
        st.button("Open →", disabled=True, use_container_width=True)

c1, c2, c3 = st.columns(3)
with c1: tile("Job Description Generator", "Produce Neogen house-style JDs from options.")
with c2: tile("Job Advert Generator", "Convert a JD + options into a branded advert.")
with c3: tile("Interview Guide Generator", "Structured interview guide templates.")

c1, c2, c3 = st.columns(3)
with c1: tile("Interview Question Generator", "Tailored questions + scoring rubrics.")
with c2: tile("Hiring Manager Toolkit", "Playbooks, onboarding steps, expectations.")
with c3: tile("Interview Feedback Collector", "Capture interview outcomes.")

c1, c2, _ = st.columns(3)
with c1: tile("Shortlisting Summary Tool", "JD + up to five CVs → executive comparison.")

