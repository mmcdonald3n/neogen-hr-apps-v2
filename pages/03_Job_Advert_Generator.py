import streamlit as st
from utils.brand import header, footer

st.set_page_config(page_title="Job Advert Generator", page_icon="📢", layout="wide")
header()

st.subheader("Job Advert Generator")
st.info("Scaffold page. Wire in your Neogen-styled advert logic here.")
jd_source = st.text_area("Paste JD (optional)")
target_location = st.text_input("Target Location / Country")
if st.button("Generate Advert"):
    st.success("Neogen advert generated.")
    st.code("<!-- Neogen-styled job advert would render here -->", language="markdown")

footer()
