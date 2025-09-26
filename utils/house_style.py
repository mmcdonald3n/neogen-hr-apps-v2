from dataclasses import dataclass

@dataclass
class Brand:
    company_name: str = "Neogen"
    primary_hex: str = "#0073CF"  # Neogen Blue
    accent_hex: str = "#00A651"    # Neogen Green
    text_hex: str = "#1F2937"
    font_stack: str = "Inter, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    logo_path: str = "assets/neogen_logo.png"

BRAND = Brand()

HOUSE_TONE = (
    "Write in a clear, professional, and inclusive tone. Be concise but informative. "
    "Use UK/US neutral spelling, avoid jargon, and ensure accessibility."
)

JD_STRUCTURE = [
    "Role Purpose",
    "Key Responsibilities",
    "Skills & Experience",
    "Education & Certifications",
    "Ways of Working",
    "Compensation & Benefits",
    "About Neogen",
    "Equal Opportunity Statement",
]

ABOUT_NEOGEN = (
    "Neogen is a global leader in food safety and life sciences. We work to protect the food supply chain, "
    "advance animal and human health, and support our customers worldwide."
)

EEO_STATEMENT = (
    "Neogen is an Equal Opportunity Employer. We welcome applicants from all backgrounds and experiences."
)



