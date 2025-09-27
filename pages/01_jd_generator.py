import streamlit as st
from utils.brand import header, footer

st.set_page_config(page_title="JD Generator", page_icon="📄", layout="wide")
header()

st.subheader("Job Description Generator")
st.info("This is a scaffold. Replace this section with your full JD generator logic when ready.")
role_title = st.text_input("Role Title")
dept = st.text_input("Department")
location = st.text_input("Location")
seniority = st.selectbox("Seniority Level", ["Entry", "Mid", "Senior", "Director", "VP"])
if st.button("Generate JD"):
    st.success(f"Generated JD for **{role_title}** ({seniority}) in **{dept}**, {location}.")
    st.code("<!-- Neogen-styled JD would render here -->", language="markdown")

footer()
