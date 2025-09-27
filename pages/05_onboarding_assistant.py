import streamlit as st
from utils.brand import header, footer

st.set_page_config(page_title="Onboarding Assistant", page_icon="✨", layout="wide")
header()

st.subheader("Onboarding Assistant")
st.caption("Reminders & checklists for manager and new hire.")

hire_name = st.text_input("New Hire Name")
start_date = st.date_input("Start Date")
site = st.text_input("Site / Remote")
if st.button("Create Onboarding Checklist"):
    st.success(f"Onboarding checklist created for {hire_name} starting {start_date}.")
    st.code("""
**Manager Tasks**
- Laptop & systems access (Workday, DocuSign, Calendly).
- Buddy assigned; team intro scheduled.

**New Hire Tasks**
- Compliance docs; training modules; benefits enrollment.

**Week 1 Milestones**
- Role immersion; safety; SOP review.
""", language="markdown")

footer()
