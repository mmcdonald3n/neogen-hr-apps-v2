import streamlit as st
from utils.brand import header, footer
import pandas as pd

st.set_page_config(page_title="TA Spend Tracker", page_icon="📊", layout="wide")
header()

st.subheader("TA Spend Tracker")
st.caption("Track agency fees, job board costs, tooling, and internal time estimates.")

uploaded = st.file_uploader("Upload CSV/XLSX (date, category, vendor, amount, currency, notes)", type=["csv","xlsx"])

if uploaded:
    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded)
    st.dataframe(df, use_container_width=True)
    with st.expander("Summary"):
        numeric_cols = df.select_dtypes(include="number")
        if not numeric_cols.empty:
            st.write("Total (sum of numeric columns):", float(numeric_cols.sum(numeric_only=True).sum()))
        else:
            st.write("No numeric columns detected.")
else:
    st.info("Upload a file to view and summarize TA spend.")

footer()
