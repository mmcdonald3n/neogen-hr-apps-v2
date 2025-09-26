import streamlit as st
from pathlib import Path

ASSETS = Path(__file__).parent / "assets"

def show_logo_and_title(title: str) -> None:
    cols = st.columns([1, 6, 1])
    with cols[1]:
        logo_path = ASSETS / "neogen_logo.png"
        if logo_path.exists():
            st.image(str(logo_path), width=140)
        st.markdown("### " + title)

def model_selector() -> str:
    # Keep IDs simple ASCII to avoid parsing issues on some hosts
    model_map = {
        "GPT-4.1 Mini (recommended)": "gpt-4.1-mini",
        "GPT-4o Mini": "gpt-4o-mini",
        "GPT-4.1": "gpt-4.1",
        "o3-mini (reasoning)": "o3-mini",
    }
    choice = st.selectbox(
        "Model",
        list(model_map.keys()) + ["Custom..."],
        index=0,
        help="Model is applied to this page only."
    )
    if choice == "Custom...":
        return st.text_input("Enter model id", value="gpt-4.1-mini")
    return model_map[choice]




