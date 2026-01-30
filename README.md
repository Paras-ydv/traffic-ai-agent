# 🚦 Traffic Congestion Explainable AI (Agentic System)

## Overview
This project demonstrates an **Agentic AI system** that explains urban traffic congestion patterns using
real-world structured data stored in **DataStax Astra DB**, orchestrated via **Langflow**, and reasoned
using **IBM watsonx.ai (Granite models)**.

## Architecture
- Langflow: Visual orchestration of agents
- Astra DB: Vector database for traffic records
- IBM watsonx.ai: LLM reasoning and explanation
- RAG-style pipeline with explainability

## Langflow Components Used
- Chat Input
- Astra DB Vector Search
- Data-to-Message Converter
- Prompt Template
- IBM watsonx.ai (Granite-3-8B)
- Chat Output

## How It Works
1. User asks a natural language question
2. Query is vector-searched in Astra DB
3. Retrieved records are converted to text
4. Prompt Template injects structured context
5. IBM Granite model generates explanation
6. Output is shown to the user

## How to Run
```bash
pip install -r requirements.txt
python app.py
