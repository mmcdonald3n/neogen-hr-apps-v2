from pathlib import Path
import sys, streamlit as st
REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path: sys.path.insert(0, str(REPO_ROOT))
from components.layout import app_header
st.set_page_config(page_title="Interview Guide Generator", page_icon="📄", layout="wide")
app_header("Interview Guide Generator")
st.info("Structured interview guides aligned to the JD. Exports DOCX/PDF.")

