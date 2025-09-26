import streamlit as st
from shared.branding import show_logo_and_title, model_selector
from shared.house_style import section_box
from shared.utils import generate_text
from shared.prompts import IVQ_SYSTEM_PROMPT

st.set_page_config(page_title="Interview Question Generator – Neogen", page_icon="?", layout="wide")
show_logo_and_title("Interview Question Generator")

model = model_selector()

with st.form("ivq_form"):
    pasted_jd = st.text_area("Paste the relevant JD or summary*", height=220, placeholder="Paste the JD or a concise summary of responsibilities and requirements…")
    seniority = st.selectbox("Target Level", ["Entry", "Intermediate", "Senior", "Manager", "Director", "VP"], index=2)
    focus = st.multiselect("Emphasis (choose any)", ["Technical depth","Leadership","Stakeholder mgmt","Regulatory/QA","Data/BI","Culture & values","Problem-solving","Communication"])
    submitted = st.form_submit_button("Generate Questions")

if submitted:
    if not pasted_jd.strip():
        st.error("Please paste the JD or a short summary.")
        st.stop()

    user_prompt = f"""
Seniority: {seniority}
Focus Areas: {', '.join(focus) if focus else 'General'}
JD/Summary:
{pasted_jd}
"""
    with st.spinner("Creating tailored interview questions…"):
        ivq_text = generate_text(model=model, system=IVQ_SYSTEM_PROMPT, user=user_prompt, max_tokens=1200)

    section_box("Neogen Interview Question Set", ivq_text, downloadable_name="Interview_Questions.md")
