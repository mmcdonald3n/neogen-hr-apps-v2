import streamlit as st
from utils.brand import header, footer

st.set_page_config(page_title="Neogen Suite", page_icon="🧭", layout="wide")
header()

st.markdown("Welcome to the Neogen Suite. Use the sidebar or the tiles below.")
st.markdown("## Tools")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### Job Description Generator")
    st.page_link("pages/01_jd_generator.py", label="Open JD Generator", icon=":page_facing_up:")
with col2:
    st.markdown("### Interview Question Generator")
    st.page_link("pages/02_ivq_generator.py", label="Open IVQ Generator", icon=":page_facing_up:")
with col3:
    st.markdown("### Job Advert Generator")
    st.page_link("pages/03_job_advert_generator.py", label="Open Advert Generator", icon=":pushpin:")

st.markdown("---")

col4, col5, col6 = st.columns(3)
with col4:
    st.markdown("### Hiring Manager Guidance")
    st.page_link("pages/04_hiring_manager_guidance.py", label="Open Guidance", icon=":books:")
with col5:
    st.markdown("### Onboarding Assistant")
    st.page_link("pages/05_onboarding_assistant.py", label="Open Onboarding", icon=":sparkles:")
with col6:
    st.markdown("### TA Spend Tracker")
    st.page_link("pages/06_ta_spend_tracker.py", label="Open Spend Tracker", icon=":bar_chart:")

st.markdown("---")
st.markdown("### Contingent Workforce Manager")
st.page_link("pages/07_contingent_workforce_manager.py", label="Open CWM", icon=":briefcase:")

footer()
