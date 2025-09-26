# -*- coding: utf-8 -*-
import os
import streamlit as st
from utils.house_style import BRAND, HOUSE_TONE
from utils.jd_templates import BASE_SYSTEM_PROMPT, build_user_prompt, ADVERT_PROMPT, HM_GUIDE_PROMPT
from utils.openai_client import generate_markdown
from utils.exporters import export_docx, export_markdown

st.set_page_config(page_title="Neogen — JD Generator", page_icon=None, layout="wide")

left, right = st.columns([1,6])
with left:
    try:
        if os.path.exists(BRAND.logo_path) and os.path.getsize(BRAND.logo_path) > 0:
            st.image(BRAND.logo_path, width=110)
    except Exception:
        pass
with right:
    st.title("Job Description Generator")
    st.caption("Neogen-branded output with consistent house style and exports")

st.sidebar.subheader("Model")
model = st.sidebar.selectbox("Chat Model", ["gpt-4.1-mini", "gpt-4o-mini", "gpt-4.1"], index=0)

st.sidebar.subheader("Output")
produce_advert = st.sidebar.checkbox("Include short Job Advert", value=True)
produce_hmguide = st.sidebar.checkbox("Include Hiring Manager guidance", value=True)

with st.form("jd_form"):
    st.markdown("### Role Details")
    col1, col2, col3 = st.columns(3)
    with col1:
        title = st.text_input("Job Title", "Senior Data Analyst")
        department = st.text_input("Department/Team", "Analytics")
        seniority = st.selectbox("Seniority Level", ["Entry","Associate","Mid","Senior","Lead","Manager","Director"], index=3)
    with col2:
        location = st.text_input("Location", "Lansing, MI (Hybrid)")
        work_pattern = st.selectbox("Ways of Working", ["Onsite","Hybrid","Remote"], index=1)
        emp_type = st.selectbox("Employment Type", ["Full-time","Part-time","Fixed Term","Contractor"], index=0)
    with col3:
        comp_range = st.text_input("Compensation Range (optional)", "")
        reports_to = st.text_input("Reports To (optional)", "")
        direct_reports = st.text_input("Direct Reports (optional)", "")

    st.markdown("### Content Hints (optional)")
    role_purpose = st.text_area("Role Purpose", "Drive trusted analytics that inform decisions across Operations and Commercial teams.")
    responsibilities = st.text_area("Key Responsibilities (bullets)", "• Build and maintain Power BI dashboards\n• Partner with stakeholders to define metrics\n• Ensure data quality and governance")
    skills = st.text_area("Skills & Experience (bullets)", "• Power BI, SQL, Python\n• Stakeholder management\n• Strong communication")
    education = st.text_area("Education/Certifications", "Bachelor's degree in a quantitative field or equivalent experience")
    benefits = st.text_area("Benefits (optional)", "Comprehensive health plan, retirement savings, paid time off, learning stipend")
    compliance = st.text_area("Compliance/Other (optional)", "Background checks managed via approved vendors; right to work required")

    tone = st.text_area("Tone guidance (kept subtle)", HOUSE_TONE)

    submitted = st.form_submit_button("Generate JD", use_container_width=True)

if submitted:
    with st.spinner("Generating Neogen-styled content..."):
        inputs = {
            "title": title,
            "department": department,
            "location": location,
            "work_pattern": work_pattern,
            "emp_type": emp_type,
            "seniority": seniority,
            "comp_range": comp_range,
            "reports_to": reports_to,
            "direct_reports": direct_reports,
            "role_purpose": role_purpose,
            "responsibilities": responsibilities,
            "skills": skills,
            "education": education,
            "benefits": benefits,
            "compliance": compliance,
            "tone": tone,
        }

        jd_md = generate_markdown(
            [{"role": "system", "content": BASE_SYSTEM_PROMPT},
             {"role": "user", "content": build_user_prompt(inputs)}],
            model=model
        )
        st.success("Full JD ready.")
        st.markdown(jd_md)

        if produce_advert:
            advert_md = generate_markdown(
                [{"role": "system", "content": BASE_SYSTEM_PROMPT},
                 {"role": "user", "content": build_user_prompt(inputs) + "\n\n" + ADVERT_PROMPT}],
                model=model
            )
            st.divider()
            st.subheader("Short Job Advert")
            st.markdown(advert_md)

        if produce_hmguide:
            hm_md = generate_markdown(
                [{"role": "system", "content": BASE_SYSTEM_PROMPT},
                 {"role": "user", "content": build_user_prompt(inputs) + "\n\n" + HM_GUIDE_PROMPT}],
                model=model
            )
            st.divider()
            st.subheader("Hiring Manager Guidance")
            st.markdown(hm_md)

        st.divider()
        st.subheader("Export")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            docx_buf = export_docx(title, jd_md)
            st.download_button("Download JD (DOCX)", data=docx_buf, file_name=f"{title.replace(' ', '_')}_JD.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        with col_b:
            md_buf = export_markdown(jd_md)
            st.download_button("Download JD (Markdown)", data=md_buf, file_name=f"{title.replace(' ', '_')}_JD.md", mime="text/markdown")
        with col_c:
            st.caption("PDF export available on request.")


