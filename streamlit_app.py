import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

LANGFLOW_API_URL = os.getenv("LANGFLOW_API_URL")
FLOW_ID = os.getenv("LANGFLOW_FLOW_ID")
LANGFLOW_API_KEY = os.getenv("LANGFLOW_API_KEY")

st.set_page_config(
    page_title="Explainable Traffic AI Agent",
    layout="centered"
)

st.title("🚦 Explainable Traffic AI Agent")
st.caption("Agentic AI using Langflow + IBM Granite + Astra DB")

question = st.text_area(
    "Ask a traffic-related question",
    "Why is Silk Board congested during office hours?"
)

def extract_text(resp):
    """
    Robust extractor for Langflow v1.5+
    Works for ChatOutput + IBM Granite + Astra DB
    """
    try:
        # ✅ BEST: top-level messages (most stable)
        if "messages" in resp and len(resp["messages"]) > 0:
            msg = resp["messages"][0]
            if isinstance(msg, dict):
                return msg.get("message") or msg.get("text")

        # ✅ Fallback: artifacts message
        outputs = resp.get("outputs", [])
        for block in outputs:
            artifacts = block.get("artifacts", {})
            if "message" in artifacts:
                return artifacts["message"]

        # ✅ Fallback: deep results tree
        for block in outputs:
            for out in block.get("outputs", []):
                results = out.get("results", {})
                message = results.get("message", {})
                data = message.get("data", {})
                if "text" in data:
                    return data["text"]

        return "⚠️ No explanation text found."

    except Exception as e:
        return f"❌ Parsing error: {e}\n\nRaw response:\n{resp}"


if st.button("Analyze Traffic"):
    with st.spinner("Analyzing traffic data..."):
        payload = {
            "input_value": question,
            "input_type": "chat",
            "output_type": "chat"
        }

        headers = {
            "x-api-key": LANGFLOW_API_KEY
        }

        r = requests.post(
            f"{LANGFLOW_API_URL}/{FLOW_ID}",
            json=payload,
            headers=headers,
            timeout=120
        )

        result = r.json()
        answer = extract_text(result)

        st.subheader("🧠 AI Explanation")
        st.write(answer)
