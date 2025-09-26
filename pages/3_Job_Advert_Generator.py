# -*- coding: utf-8 -*-
import os
import streamlit as st
from utils.house_style import BRAND, HOUSE_TONE
from utils.jd_templates import BASE_SYSTEM_PROMPT
from utils.openai_client import generate_markdown
from utils.exporters import export_docx, export_markdown

st.set_page_config(page_title="Neogen — Job Advert Generator", page_icon=None, layout="wide")

left, right = st.columns([1,6])
with left:
    try:
        if os.path.exists(BRAND.logo_path) and os.path.getsize(BRAND.logo_path) > 0:
            st.image(BRAND.logo_path, width=110)
    except Exception:
        pass
with right:
    st.title("Job Advert Generator")
    st.caption("Generate a short, compelling advert in Neogen house style")

st.sidebar.subheader("Model")
model = st.sidebar.selectbox("Chat Model", ["gpt-4.1-mini", "gpt-4o-mini", "gpt-4.1"], index=0)

with st.form("advert_form"):
    st.markdown("### Role Details")
    title = st.text_input("Job Title", "Senior Data Analyst")
    location = st.text_input("Location", "Lansing, MI (Hybrid)")
    department = st.text_input("Department", "Analytics")
    summary = st.text_area("Summary of role", "We are looking for a data-driven professional...")

    submitted = st.form_submit_button("Generate Advert", use_container_width=True)

if submitted:
    with st.spinner("Generating advert..."):
        prompt = f"""Write a concise job advert for the role below, in Neogen house style.

Title: {title}
Location: {location}
Department: {department}
Summary: {summary}

Tone: {HOUSE_TONE}
"""
        advert_md = generate_markdown(
            [{"role": "system", "content": BASE_SYSTEM_PROMPT},
             {"role": "user", "content": prompt}],
            model=model
        )
        st.success("Advert ready.")
        st.markdown(advert_md)

        st.divider()
        st.subheader("Export")
        col_a, col_b = st.columns(2)
        with col_a:
            docx_buf = export_docx(title, advert_md)
            st.download_button("Download Advert (DOCX)", data=docx_buf, file_name=f"{title.replace(' ', '_')}_Advert.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        with col_b:
            md_buf = export_markdown(advert_md)
            st.download_button("Download Advert (Markdown)", data=md_buf, file_name=f"{title.replace(' ', '_')}_Advert.md", mime="text/markdown")



