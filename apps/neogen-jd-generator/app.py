import os, json
from pathlib import Path
import streamlit as st
from pydantic import ValidationError
from utils.branding import BRAND
from utils.house_style import HOUSE_STYLE
from utils.prompts import JDInputs, render_user_prompt, SYSTEM_PROMPT
from utils.export_docx import export_docx
from utils.export_pdf import export_pdf
def get_openai_key():
    return st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
MODELS = ["gpt-4.1-mini","gpt-4o-mini","gpt-4.1"]
def llm_complete(system_prompt: str, user_prompt: str, model: str) -> str:
    import requests
    api_key = get_openai_key()
    if not api_key:
        st.error("OPENAI_API_KEY not set in secrets."); st.stop()
    url = "https://api.openai.com/v1/responses"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    body = {"model": model, "input": [{"role":"system","content":SYSTEM_PROMPT},{"role":"user","content":user_prompt}]}
    r = requests.post(url, headers=headers, data=json.dumps(body), timeout=120); r.raise_for_status()
    data = r.json()
    return (data.get("output",{}).get("text")
        or (data.get("choices") or [{}])[0].get("message",{}).get("content")
        or (data.get("choices") or [{}])[0].get("text") or "")
st.set_page_config(page_title="Neogen • Job Description Generator", page_icon="📄", layout="wide")
left, right = st.columns([1,5])
with left: st.image(BRAND.logo_path, width=140)
with right:
    st.markdown(f"""<div style='text-align:right;'>
            <span style='font-size:14px;color:{BRAND.muted};'>Neogen HR Applications Suite</span>
            <h1 style='margin:0;color:{BRAND.text};'>Job Description Generator</h1>
        </div>""", unsafe_allow_html=True)
with st.sidebar:
    st.header("Settings")
    default_model = os.getenv("DEFAULT_LLM_MODEL", st.secrets.get("DEFAULT_LLM_MODEL", "gpt-4.1-mini"))
    model = st.selectbox("Model", MODELS, index=MODELS.index(default_model) if default_model in MODELS else 0)
    include_icons = st.toggle("Include icons in UI (not in exports)", value=False)
    st.caption("Exports are Neogen-branded, clean, no emojis.")
st.divider()
with st.form("jd_form"):
    st.subheader("Role details")
    c1,c2,c3 = st.columns(3)
    with c1:
        job_title = st.text_input("Job Title", placeholder="Senior Data Engineer")
        department = st.text_input("Department", placeholder="Technology / Data")
        business_unit = st.text_input("Business Unit (optional)")
        grade_level = st.text_input("Grade/Level (optional)")
    with c2:
        location = st.text_input("Primary Location", placeholder="Lansing, MI (or Remote)")
        work_model = st.selectbox("Work model", ["Onsite","Hybrid","Remote"], index=1)
        region = st.selectbox("Region", ["USA","Canada","EMEA","LATAM","APAC"], index=0)
        travel = st.text_input("Travel (optional)", placeholder="Up to 10%")
    with c3:
        comp_band = st.text_input("Comp band (optional)", placeholder="e.g., M2 band, – base")
        hiring_manager = st.text_input("Hiring Manager (optional)")
    st.markdown("### Key points (optional)")
    summary_points = st.tags_input("Role summary bullets", suggestions=["Own data pipelines","Partner with Product","Enable analytics at scale"])  # type: ignore
    must_have = st.tags_input("Must-have requirements", suggestions=["5+ years Python","Cloud data stack","Workday experience"])  # type: ignore
    nice_to_have = st.tags_input("Nice-to-have requirements", suggestions=["Spark","DBT","Power BI"])  # type: ignore
    competencies = st.tags_input("Core competencies", suggestions=["Collaboration","Problem-solving","Stakeholder management"])  # type: ignore
    stakeholders = st.tags_input("Stakeholders", suggestions=["Engineering","Product","HR","Finance"])  # type: ignore
    st.markdown("### Optional: refine with an existing JD")
    existing_jd = st.text_area("Paste an existing JD (optional)", height=180, placeholder="Paste text to incorporate tone/points…")
    additional_notes = st.text_area("Any other notes (optional)", height=120)
    submitted = st.form_submit_button("Generate JD", use_container_width=True)
jd_md = ""
if submitted:
    try:
        inputs = JDInputs(job_title=job_title.strip(), department=department.strip(),
            business_unit=(business_unit.strip() or None), hiring_manager=(hiring_manager.strip() or None),
            location=location.strip(), work_model=work_model, region=region, grade_level=(grade_level.strip() or None),
            comp_band=(comp_band.strip() or None), travel=(travel.strip() or None),
            summary_points=summary_points or [], must_have=must_have or [], nice_to_have=nice_to_have or [],
            competencies=competencies or [], stakeholders=stakeholders or [], additional_notes=(additional_notes or None))
    except ValidationError as e:
        st.error(f"Input validation error: {e}"); st.stop()
    user_prompt = render_user_prompt(inputs, HOUSE_STYLE.equal_opportunity_text)
    if existing_jd: user_prompt += "\n\nIncorporate relevant strengths from the following existing JD while keeping the requested structure and tone:\n" + existing_jd
    if additional_notes: user_prompt += "\n\nAdditional notes from TA/HM to respect:\n" + additional_notes
    with st.status("Generating…", expanded=True) as status:
        st.write("Contacting model…")
        jd_md = llm_complete(SYSTEM_PROMPT, user_prompt, model=model)
        if not jd_md.strip(): st.error("No content returned from the model."); st.stop()
        status.update(label="Generation complete", state="complete")
if jd_md:
    st.success("Draft ready. Review below, then export.")
    if include_icons: st.markdown(":page_facing_up: **Preview**")
    st.markdown(jd_md)
    c1,c2,c3 = st.columns(3)
    with c1:
        if st.button("Copy Markdown", use_container_width=True):
            st.code(jd_md, language="markdown"); st.toast("Scroll to copy the Markdown block.")
    with c2:
        if st.button("Export DOCX", use_container_width=True):
            out = export_docx(jd_md, title=f"Job Description — {job_title}", out_path=Path("_out")/"jd.docx")
            with open(out, "rb") as f: st.download_button("Download .docx", f, file_name=f"Neogen_JD_{job_title.replace(' ','_')}.docx", use_container_width=True)
    with c3:
        if st.button("Export PDF", use_container_width=True):
            out = export_pdf(jd_md, title=f"Job Description — {job_title}", out_path=Path("_out")/"jd.pdf")
            with open(out, "rb") as f: st.download_button("Download .pdf", f, file_name=f"Neogen_JD_{job_title.replace(' ','_')}.pdf", use_container_width=True)
st.caption("© Neogen — internal TA tooling. Output intended for hiring workflows.")