# LLM-Hallucination-Prevention
A lightweight Python service that classifies user queries as Relevant or Irrelevant to company sales data before they reach your Large Language Model (LLM) SQL generation pipeline.

This project leverages Google Gemini Flash to prevent hallucinated SQL queries on irrelevant inputs.

 Why you have to  Use This?
LLMs are powerful but often produce invalid or hallucinated structured outputs when users ask questions outside your data domain (e.g., weather, politics).

For example:

 “Who is the Prime Minister of India?” → Irrelevant

 “How many units of Product A were sold in Q1?” → Relevant

This classifier acts as a first line of defense, ensuring your pipeline only processes sales-related questions.

 Features
- Zero-shot classification with Gemini 2.0 Flash
- Deterministic outputs (Relevant or Irrelevant)
- Simple Python interface (classify_query())
- Easily integratable into any data workflow
- Configurable prompt definitions
