import streamlit as st
from utils.brand import header, footer

st.set_page_config(page_title="IVQ Generator", page_icon="📝", layout="wide")
header()

st.subheader("Interview Question Generator")
st.info("Scaffold page. Wire in your neogen-ivq-generator logic here.")
job_family = st.selectbox("Job Family", ["Sales", "Engineering", "Manufacturing", "Quality", "HR", "Finance", "IT"])
competencies = st.text_area("Key Competencies (comma-separated)")
if st.button("Generate Interview Pack"):
    st.success("Neogen interview question pack generated.")
    st.code("<!-- Neogen-styled IVQ pack would render here -->", language="markdown")

footer()
