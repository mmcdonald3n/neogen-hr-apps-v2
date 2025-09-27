import streamlit as st
from utils.brand import header, footer

st.set_page_config(page_title="Hiring Manager Guidance", page_icon="📚", layout="wide")
header()

st.subheader("Hiring Manager Guidance")
st.caption("Automated, Neogen house-style guidance after a requisition is opened (process, timelines, stakeholders).")

req_id = st.text_input("Requisition ID (optional)")
seniority = st.selectbox("Seniority", ["Entry", "Mid", "Senior", "Director", "VP"])
region = st.selectbox("Region", ["USA", "Canada", "EMEA", "LATAM", "APAC"])

if st.button("Generate Guidance"):
    st.success("Hiring Manager guidance generated.")
    st.code(f"""
**Kickoff & Role Alignment**
- Confirm success profile and decision team.
- Timeline baseline: 6–8 weeks (region: {region}, seniority: {seniority}).

**Sourcing & Screening**
- Standard Neogen channels + referrals.
- Structured screening aligned to competencies.

**Interview Panel & Rubrics**
- Panel mix to reduce bias; use shared rubric pack.

**Offer & Approvals**
- Route via Workday; comp guardrails applied.

**Onboarding Handover**
- Trigger Onboarding Assistant and IT access.
""", language="markdown")

footer()
