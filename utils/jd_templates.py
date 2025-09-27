from typing import Dict
from .house_style import BRAND, JD_STRUCTURE, ABOUT_NEOGEN, EEO_STATEMENT

BASE_SYSTEM_PROMPT = f"""
You are an expert HR content writer generating Job Descriptions that match the Neogen house style.
- Use the sections: {', '.join(JD_STRUCTURE)}
- Keep tone: clear, inclusive, professional. Avoid excessive hype.
- Use bullet points for responsibilities and skills.
- Keep line spacing friendly for ATS parsing (no weird characters).
- Return clean Markdown with proper headings (## for sections).
"""

def build_user_prompt(inputs: Dict[str, str]) -> str:
    lines = []
    ap = lines.append
    ap(f"Company: {BRAND.company_name}")
    ap(f"Job Title: {inputs.get('title','')}")
    ap(f"Department/Team: {inputs.get('department','')}")
    ap(f"Location: {inputs.get('location','')}")
    ap(f"Ways of Working: {inputs.get('work_pattern','')}")
    ap(f"Employment Type: {inputs.get('emp_type','')}")
    ap(f"Seniority Level: {inputs.get('seniority','')}")
    ap(f"Compensation Range: {inputs.get('comp_range','')}")
    ap(f"Reports To: {inputs.get('reports_to','')}")
    ap(f"Direct Reports: {inputs.get('direct_reports','')}")
    ap(f"Role Purpose (hints): {inputs.get('role_purpose','')}")
    ap(f"Key Responsibilities (hints): {inputs.get('responsibilities','')}")
    ap(f"Skills & Experience (hints): {inputs.get('skills','')}")
    ap(f"Education/Certifications (hints): {inputs.get('education','')}")
    ap(f"Benefits (hints): {inputs.get('benefits','')}")
    ap(f"Compliance/Fine Print: {inputs.get('compliance','')}")
    ap(f"House Style tone guidance: {inputs.get('tone','')}")
    return "\n".join(lines)

ADVERT_PROMPT = (
    "Create a short job advert (150–220 words) in Neogen's voice. Include a punchy opener, "
    "3–5 bullet highlights (impact, tech/skills, team, growth), and a clear call to action."
)

HM_GUIDE_PROMPT = (
    "Draft concise hiring manager guidance for interviewing this role: 6–8 targeted questions, "
    "what good looks like, typical red flags, and suggested brief case exercise if appropriate."
)








