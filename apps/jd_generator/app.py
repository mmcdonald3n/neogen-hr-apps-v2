import sys
from pathlib import Path
from datetime import date
import traceback, tempfile
import streamlit as st

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from services.jd_service import JDModel, render_markdown  # noqa: E402
from exporters.docx_export import export_jd_to_docx  # noqa: E402
from exporters.pdf_export import export_jd_to_pdf  # noqa: E402
from exporters.branding import DEFAULT_BRANDING  # noqa: E402

LOGS_DIR = REPO_ROOT / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)

def _log(ctx: str, ex: Exception):
    with open(LOGS_DIR / f"error_{ctx}.log", "a", encoding="utf-8") as f:
        f.write("=== Exception ===\n")
        f.write(f"Context: {ctx}\nType: {type(ex).__name__}\nMessage: {ex}\n")
        f.write("Traceback:\n" + "".join(traceback.format_exc()) + "\n\n")

def _textarea_list(label: str, help_text: str) -> list[str]:
    raw = st.text_area(label, value="", help=help_text, height=120, placeholder="- Bullet 1\n- Bullet 2")
    out: list[str] = []
    for line in raw.splitlines():
        line = line.strip()
        if not line: continue
        if line.startswith("- "): line = line[2:].strip()
        out.append(line)
    return out

def render(embed_mode: bool = False):
    if not embed_mode:
        st.set_page_config(page_title="Job Description Generator", page_icon="📝", layout="wide")

    with st.form("jd_form", clear_on_submit=False):
        st.subheader("Core Details")
        c1, c2, c3 = st.columns(3)
        with c1:
            requisition_id = st.text_input("Requisition ID *", "REQ-0001")
            job_title = st.text_input("Job Title *", "Senior Data Analyst")
            department = st.text_input("Department *", "Global Talent Acquisition")
        with c2:
            location = st.text_input("Location *", "Lansing, MI (Hybrid)")
            employment_type = st.selectbox("Employment Type *", ["Full-time", "Part-time", "Contract"], 0)
            grade = st.text_input("Grade / Band", "M2")
        with c3:
            hiring_manager = st.text_input("Hiring Manager *", "Alex Morgan")
            compensation_range = st.text_input("Compensation Range", "$120,000–$140,000")
            posting_date = st.date_input("Posting Date *", value=date(2025,1,1))

        st.subheader("Content")
        summary = st.text_area("Summary *",
            "We are seeking a Senior Data Analyst to drive insights across our HR function.",
            help="2–4 sentences.")
        responsibilities = _textarea_list("Key Responsibilities *", "One bullet per line.")
        qualifications  = _textarea_list("Qualifications *", "Required skills/experience.")
        benefits        = _textarea_list("Benefits", "Optional.")

        submitted = st.form_submit_button("Generate Preview")

    if not submitted:
        return

    try:
        jd = JDModel(
            requisition_id=requisition_id.strip(),
            job_title=job_title.strip(),
            department=department.strip(),
            location=location.strip(),
            employment_type=employment_type.strip(),
            grade=grade.strip(),
            hiring_manager=hiring_manager.strip(),
            summary=summary.strip(),
            responsibilities=responsibilities,
            qualifications=qualifications,
            benefits=benefits,
            compensation_range=compensation_range.strip(),
            posting_date=posting_date,
        )
    except Exception as ex:
        _log("validation", ex); st.error("Validation failed."); return

    st.subheader("Preview")
    st.markdown(render_markdown(jd))

    st.subheader("Export")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Export to DOCX"):
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
                    export_jd_to_docx(jd, tmp.name, DEFAULT_BRANDING)
                    path = tmp.name
                with open(path, "rb") as f:
                    st.download_button("Download JD (DOCX)", data=f,
                        file_name=f"JD_{jd.job_title.replace(' ','_')}.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                st.success("DOCX generated.")
            except Exception as ex:
                _log("docx_export", ex); st.error("DOCX export failed. See logs/.")
    with col2:
        if st.button("Export to PDF"):
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    export_jd_to_pdf(jd, tmp.name, DEFAULT_BRANDING)
                    path = tmp.name
                with open(path, "rb") as f:
                    st.download_button("Download JD (PDF)", data=f,
                        file_name=f"JD_{jd.job_title.replace(' ','_')}.pdf", mime="application/pdf")
                st.success("PDF generated.")
            except Exception as ex:
                _log("pdf_export", ex); st.error("PDF export failed. See logs/.")

if __name__ == "__main__":
    render(embed_mode=False)
