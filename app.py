from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests, os
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGFLOW_SKIP_AUTH_AUTO_LOGIN"] = "true"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

LANGFLOW_API_URL = os.getenv("LANGFLOW_API_URL")
FLOW_ID = os.getenv("LANGFLOW_FLOW_ID")

def extract_answer(resp):
    try:
        return resp["outputs"][0]["outputs"][0]["messages"][0]["content"]
    except:
        return f"Raw response:\n{resp}"

@app.post("/ask")
def ask_agent(payload: dict):
    question = payload["question"]

    body = {
        "input_value": question,
        "input_type": "chat",
        "output_type": "chat"
    }

    r = requests.post(
        f"{LANGFLOW_API_URL}/{FLOW_ID}",
        json=body,
        timeout=120
    )

    data = r.json()
    answer = extract_answer(data)

    return {"answer": answer}
