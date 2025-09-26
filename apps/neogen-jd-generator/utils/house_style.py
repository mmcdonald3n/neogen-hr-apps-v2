from dataclasses import dataclass
@dataclass(frozen=True)
class HouseStyle:
    sections = ["Role Summary","Key Responsibilities","Required Qualifications","Preferred Qualifications","Core Competencies","Stakeholders","Work Location & Travel","Compensation & Benefits","Equal Opportunity Statement","How to Apply",]
    equal_opportunity_text = ("Neogen is an Equal Opportunity Employer. We consider all qualified applicants "
        "for employment without regard to race, color, religion, sex, sexual orientation, "
        "gender identity, national origin, disability, veteran status, or any other protected characteristic.")
    tone_default = "professional, clear, concise, no hype; avoid emojis"
HOUSE_STYLE = HouseStyle()

