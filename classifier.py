import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables!")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def classify_query(user_query: str) -> str:
    """
    Classify the user query as Relevant or Irrelevant.
    """
    prompt = f"""
You are a classifier.
You must decide whether the following question is related to company sales data analysis.
Company sales data includes any questions about:
- revenue
- units sold
- sales performance
- product sales
- customer purchases
- comparisons of sales metrics
-opportunities

If yes, respond exactly with: Relevant
If no, respond exactly with: Irrelevant

Question: {user_query.strip()}
    """.strip()

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.0,  
            "top_p": 1,
            "max_output_tokens": 10
        }
    )

    text = response.text.strip()
    return text

if __name__ == "__main__":
    test_queries = [
        "what are opportunities last week",

        "waht is the weather like today?",
        "show me closed opportunities in 2024",
        "how many units of product X were sold last month?"
    ]

    for q in test_queries:
        label = classify_query(q)
        print(f"Query: {q}")
        print(f"Classification: {label}")
        print("---")
