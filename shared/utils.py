import streamlit as st
from typing import Optional

def _get_client():
    try:
        from openai import OpenAI
        return OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    except Exception as e:
        st.error("OpenAI client failed to initialize. Ensure `OPENAI_API_KEY` is set in Secrets.")
        raise e

def generate_text(model: str, system: str, user: str, max_tokens: int = 1200) -> str:
    client = _get_client()
    try:
        resp = client.responses.create(
            model=model,
            input=[{"role": "system", "content": system},
                   {"role": "user", "content": user}],
            max_output_tokens=max_tokens,
        )
        for out in resp.output:
            if out.type == "message":
                return "".join(c.text for c in out.content if c.type == "output_text")
        return resp.output_text
    except Exception:
        try:
            import openai  # type: ignore
            openai.api_key = st.secrets["OPENAI_API_KEY"]
            chat = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "system", "content": system},
                          {"role": "user", "content": user}],
                temperature=0.3,
                max_tokens=max_tokens,
            )
            return chat.choices[0].message["content"]
        except Exception as e:
            st.error(f"Generation failed: {e}")
            return "?? Generation failed. Please check your API key, model name, or logs."
