import streamlit as st
from io import BytesIO

def hero_card(title: str, desc: str, page: str) -> None:
    with st.container(border=True):
        st.markdown("**" + title + "**")
        st.caption(desc)
        # No icon arg (avoids validation issues); arrow is part of the label text
        st.page_link("pages/" + page, label="Open →")

def section_box(heading: str, body_md: str, downloadable_name: str = "output.md") -> None:
    with st.container(border=True):
        st.markdown("**" + heading + "**")
        st.markdown(body_md)
        buf = BytesIO(body_md.encode("utf-8"))
        st.download_button("Download (.md)", buf, file_name=downloadable_name, mime="text/markdown")



