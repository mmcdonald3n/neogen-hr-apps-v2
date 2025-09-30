from pathlib import Path
import sys, streamlit as st
REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path: sys.path.insert(0, str(REPO_ROOT))
from components.layout import app_header
st.set_page_config(page_title="Hiring Manager Toolkit", page_icon="🧰", layout="wide")
app_header("Hiring Manager Toolkit")
st.info("Playbooks, onboarding steps, templates. Recommendations welcome.")

