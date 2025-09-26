import streamlit as st
from shared.branding import show_logo_and_title
from shared.house_style import hero_card

st.set_page_config(page_title="Neogen HR Suite", page_icon="🧪", layout="wide")

show_logo_and_title("Neogen HR Suite")

st.write(
    "Welcome to the Neogen HR Suite. Choose a tool below. You can plug in your House Styles later; "
    "placeholders are ready for Policy Generator, Hiring Manager Toolkit, Interview Feedback Collector, and FitScore."
)

col1, col2, col3 = st.columns(3)
with col1:
    hero_card("📄 Job Description Generator",
              "Create well-structured JDs in Neogen style.",
              page="1_Job_Description_Generator.py")
with col2:
    hero_card("❓ Interview Question Generator",
              "Competency, role-specific and scenario questions.",
              page="2_Interview_Question_Generator.py")
with col3:
    hero_card("📢 Job Advert Generator",
              "Concise, inclusive adverts with bold sections and bullets.",
              page="3_Job_Advert_Generator.py")

col4, col5, col6 = st.columns(3)
with col4:
    hero_card("📚 Policy Generator (coming soon)",
              "Multi-jurisdictional policies in your house style.",
              page="4_Policy_Generator_placeholder.py")
with col5:
    hero_card("🧰 Hiring Manager Toolkit (coming soon)",
              "Guides, rubrics, onboarding checklists.",
              page="5_Hiring_Manager_Toolkit_placeholder.py")
with col6:
    hero_card("📝 Interview Feedback Collector (coming soon)",
              "Structured scorecards; export to PDF/CSV.",
              page="6_Interview_Feedback_Collector_placeholder.py")

st.markdown("---")
st.caption("Model selection is set per page. Set your API key in Secrets as OPENAI_API_KEY.")
