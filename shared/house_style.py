import streamlit as st
from io import BytesIO

def hero_card(title: str, desc: str, page: str):
    with st.container(border=True):
        st.markdown(f"**{title}**")
        st.caption(desc)
        st.page_link(f"pages/{page}", label="Open", icon="?")

def section_box(heading: str, body_md: str, downloadable_name: str = "output.md"):
    with st.container(border=True):
        st.markdown(f"**{heading}**")
        st.markdown(body_md)
        buf = BytesIO(body_md.encode("utf-8"))
        st.download_button("Download (.md)", buf, file_name=downloadable_name, mime="text/markdown")
