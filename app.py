"""
Traffic Congestion Explainable AI
Powered by Langflow + Astra DB + IBM watsonx.ai
"""

import subprocess

def run_langflow():
    subprocess.run([
        "langflow",
        "run",
        "--host", "0.0.0.0",
        "--port", "7860"
    ])

if __name__ == "__main__":
    run_langflow()
