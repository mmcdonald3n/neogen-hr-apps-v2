import streamlit as st
from utils.brand import header, footer

st.set_page_config(page_title="Contingent Workforce Manager", page_icon="💼", layout="wide")
header()

st.subheader("Contingent Workforce Manager")
st.caption("Track and govern contractors, temps, interns — approvals, tenure, extensions, and offboarding.")

st.text_input("Worker Name")
st.selectbox("Engagement Type", ["Contractor", "Temp", "Intern", "Consultant"])
st.text_input("Manager / Department")
st.date_input("Start Date")
st.date_input("End Date")
st.text_area("Scope / Notes")

st.info("Scaffold placeholder. Replace with data model + persistence later.")

footer()
