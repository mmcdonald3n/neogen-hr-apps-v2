# -*- coding: utf-8 -*-
import os
import streamlit as st
from utils.house_style import BRAND, HOUSE_TONE
from utils.openai_client import generate_markdown
from utils.exporters import export_docx, export_markdown

st.set_page_config(page_title="Neogen — Interview Question Generator", page_icon=None, layout="wide")

left, right = st.columns([1,6])
with left:
    try:
        if os.path.exists(BRAND.logo_path) and os.path.getsize(BRAND.logo_path) > 0:
            st.image(BRAND.logo_path, width=110)
    except Exception:
        pass
with right:
    st.title("Interview Question Generator")
    st.caption("Generate structured interview questions and what-good-looks-like in Neogen style")

st.sidebar.subheader("Model")
model = st.sidebar.selectbox("Chat Model", ["gpt-4.1-mini", "gpt-4o-mini", "gpt-4.1"], index=0)

with st.form("ivq_form"):
    st.markdown("### Inputs")
    role_title = st.text_input("Job Title", "Senior Data Analyst")
    seniority = st.selectbox("Seniority Level", ["Entry","Associate","Mid","Senior","Lead","Manager","Director"], index=3)
    competencies = st.text_area(
        "Key Competencies (bullets)",
        "• Stakeholder communication\n• Problem solving\n• Data storytelling\n• Power BI & SQL",
    )
    must_haves = st.text_area(
        "Must-haves (bullets)",
        "• 3+ years with Power BI\n• SQL for data wrangling\n• Experience partnering with business stakeholders",
    )
    nice_to_haves = st.text_area(
        "Nice-to-haves (bullets)",
        "• Python for analysis\n• Exposure to life sciences / manufacturing",
    )
    jd_context = st.text_area(
        "Optional JD/context paste (improves relevance)",
        "",
        height=130
    )
    submitted = st.form_submit_button("Generate Questions", use_container_width=True)

if submitted:
    with st.spinner("Generating interview questions..."):
        sys = (
            "You are an expert talent assessor for Neogen. Create structured interview materials:\n"
            "- 8–12 questions grouped by competency\n"
            "- For each question: what good looks like (bullet points), and red flags\n"
            "- Include 1 short case/mini-exercise suggestion\n"
            "- Keep the tone professional, inclusive, and concise.\n"
            f"House tone: {HOUSE_TONE}\n"
        )
        user = f"""Role: {role_title}
Seniority: {seniority}
Competencies:
{competencies}

Must-haves:
{must_haves}

Nice-to-haves:
{nice_to_haves}

JD/Context (optional):
{jd_context}
"""

        ivq_md = generate_markdown(
            [{"role": "system", "content": sys},
             {"role": "user", "content": user}],
            model=model
        )

        st.success("Interview pack ready.")
        st.markdown(ivq_md)

        st.divider()
        st.subheader("Export")
        col1, col2 = st.columns(2)
        with col1:
            docx_buf = export_docx(f"{role_title} — Interview Pack", ivq_md)
            st.download_button(
                "Download Pack (DOCX)",
                data=docx_buf,
                file_name=f"{role_title.replace(' ', '_')}_Interview_Pack.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        with col2:
            md_buf = export_markdown(ivq_md)
            st.download_button(
                "Download Pack (Markdown)",
                data=md_buf,
                file_name=f"{role_title.replace(' ', '_')}_Interview_Pack.md",
                mime="text/markdown"
            )








