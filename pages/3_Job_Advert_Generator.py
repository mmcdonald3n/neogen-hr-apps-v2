import streamlit as st
from shared.branding import show_logo_and_title, model_selector
from shared.house_style import section_box
from shared.utils import generate_text
from shared.prompts import AD_SYSTEM_PROMPT

st.set_page_config(page_title="Job Advert Generator – Neogen", page_icon="??", layout="wide")
show_logo_and_title("Job Advert Generator")

model = model_selector()

with st.form("ad_form"):
    role_title = st.text_input("Role title*", placeholder="e.g., Senior Microbiologist")
    location = st.text_input("Location", placeholder="e.g., Lansing, MI (Hybrid)")
    pasted_jd = st.text_area("Paste the JD or key bullets*", height=220)
    inclusive_checks = st.checkbox("Ensure inclusive, non-exclusionary language", value=True)
    call_to_action = st.text_input("Call to action", value="Apply today to help protect the world’s food supply.")
    submitted = st.form_submit_button("Generate Job Advert")

if submitted:
    if not role_title.strip() or not pasted_jd.strip():
        st.error("Please provide Role title and JD/bullets.")
        st.stop()

    user_prompt = f"""
Role Title: {role_title}
Location: {location}
Inclusive Language: {"Yes" if inclusive_checks else "No"}
Call to Action: {call_to_action}

JD/Bullets:
{pasted_jd}
"""
    with st.spinner("Drafting a concise, compelling advert…"):
        ad_text = generate_text(model=model, system=AD_SYSTEM_PROMPT, user=user_prompt, max_tokens=1000)

    section_box("Neogen Job Advert", ad_text, downloadable_name=f"{role_title.replace(' ','_')}_Advert.md")
