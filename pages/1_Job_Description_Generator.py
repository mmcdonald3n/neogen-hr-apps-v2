import streamlit as st
from shared.branding import show_logo_and_title, model_selector
from shared.house_style import section_box
from shared.utils import generate_text
from shared.prompts import JD_SYSTEM_PROMPT

st.set_page_config(page_title="JD Generator – Neogen", page_icon="??", layout="wide")
show_logo_and_title("Job Description Generator")

model = model_selector()

with st.form("jd_form"):
    role_title = st.text_input("Role title*", placeholder="e.g., Senior Microbiologist")
    location = st.text_input("Location", placeholder="e.g., Lansing, MI (Hybrid)")
    department = st.text_input("Department", placeholder="e.g., Food Safety")
    level = st.selectbox("Seniority", ["Entry", "Intermediate", "Senior", "Manager", "Director", "VP"], index=2)
    inputs = st.text_area("Key inputs / notes", placeholder="Paste any bullets, legacy job specs, or requirements…", height=180)
    submitted = st.form_submit_button("Generate JD")

if submitted:
    if not role_title.strip():
        st.error("Please provide a Role title.")
        st.stop()

    user_prompt = f"""
Role Title: {role_title}
Location: {location}
Department: {department}
Seniority: {level}

Notes:
{inputs}
"""
    with st.spinner("Generating your Neogen-style JD…"):
        jd_text = generate_text(model=model, system=JD_SYSTEM_PROMPT, user=user_prompt, max_tokens=1400)

    section_box("Neogen Job Description", jd_text, downloadable_name=f"{role_title.replace(' ','_')}_JD.md")
