import os
from typing import List
from openai import OpenAI

_client = None

def get_client() -> OpenAI:
    global _client
    if _client is None:
        api_key = os.environ.get("OPENAI_API_KEY") or _get_from_secrets()
        _client = OpenAI(api_key=api_key)
    return _client

def _get_from_secrets():
    try:
        import streamlit as st
        return st.secrets.get("OPENAI_API_KEY")
    except Exception:
        return None

def generate_markdown(messages: List[dict], model: str = "gpt-4.1-mini") -> str:
    client = get_client()
    resp = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.4,
    )
    return resp.choices[0].message.content.strip()



