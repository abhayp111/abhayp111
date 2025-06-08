import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Replace this with your OpenRouter API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  

def call_llm(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "mistralai/mistral-7b-instruct",  # Use free models from https://openrouter.ai
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"
