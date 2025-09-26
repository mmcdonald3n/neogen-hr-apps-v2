from pydantic import BaseModel, Field
from typing import List, Optional
class JDInputs(BaseModel):
    job_title: str; department: str
    business_unit: Optional[str] = None; hiring_manager: Optional[str] = None
    location: str; work_model: str = Field(description="Onsite / Hybrid / Remote")
    region: str = Field(description="e.g., USA, Canada, EMEA, LATAM, APAC")
    grade_level: Optional[str] = None; comp_band: Optional[str] = None; travel: Optional[str] = None
    summary_points: List[str] = []; must_have: List[str] = []; nice_to_have: List[str] = []
    competencies: List[str] = []; stakeholders: List[str] = []; additional_notes: Optional[str] = None
SYSTEM_PROMPT = ("You are a senior Talent Acquisition partner writing a Job Description in the Neogen house style. "
    "Write in crisp UK/US business English depending on region. Avoid marketing fluff. "
    "Output clean Markdown with section headings exactly as requested.")
USER_TEMPLATE = """
Write a Job Description for **{job_title}** in **{department}**{bu_clause}.
**Region:** {region} | **Location:** {location} | **Work model:** {work_model}
{grade_clause}{travel_clause}
**Role Summary**
- {'
- '.join(summary_points) if summary_points else 'Summarise the role in 3-4 bullets.'}
**Key Responsibilities**
- Provide 8â€“12 responsibility bullets focused on outcomes.
**Required Qualifications**
- {'
- '.join(must_have) if must_have else 'List 6â€“10 must-have requirements.'}
**Preferred Qualifications**
- {'
- '.join(nice_to_have) if nice_to_have else 'List 3â€“6 nice-to-have requirements.'}
**Core Competencies**
- {'
- '.join(competencies) if competencies else 'List 5â€“8 competencies (e.g., collaboration, problem-solving).'}
**Stakeholders**
- {'
- '.join(stakeholders) if stakeholders else 'List typical cross-functional partners.'}
**Work Location & Travel**
- {travel_text}
**Compensation & Benefits**
- {comp_text}
**Equal Opportunity Statement**
- {eoe_text}
**How to Apply**
- Provide the application method consistent with Neogenâ€™s standard process.
"""
def render_user_prompt(data: JDInputs, eoe_text: str) -> str:
    bu_clause = f" within {data.business_unit}" if data.business_unit else ""
    grade_clause = f"**Grade/Level:** {data.grade_level}
" if data.grade_level else ""
    travel_text = data.travel or "Travel requirements depend on business needs; typically minimal to moderate."
    travel_clause = f"**Travel:** {data.travel}
" if data.travel else ""
    comp_text = data.comp_band or "Compensation is competitive and commensurate with experience; benefits include health, retirement, paid time off, and other region-appropriate programs."
    return USER_TEMPLATE.format(job_title=data.job_title, department=data.department, bu_clause=bu_clause,
        region=data.region, location=data.location, work_model=data.work_model, grade_clause=grade_clause,
        travel_clause=travel_clause, summary_points=data.summary_points, must_have=data.must_have,
        nice_to_have=data.nice_to_have, competencies=data.competencies, stakeholders=data.stakeholders,
        travel_text=travel_text, comp_text=comp_text, eoe_text=eoe_text)


