import requests

# Replace this with your actual OpenRouter API key
OPENROUTER_API_KEY = "sk-..."  # ← Replace with your real key

# Set up headers
headers = {
    "Authorization": f"Bearer {"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"}",
    "Content-Type": "application/json",
}

# Prepare the prompt and payload
prompt = "Generate a quiz on the topic 'Physics' with 3 questions. Provide each question as a JSON object with keys: 'question', 'options', and 'answer'. Return a JSON array."
payload = {
    "model": "mistralai/mistral-7b-instruct",  # You can try "mistralai/mistral-7b-instruct" if unsure
    "messages": [{"role": "user", "content": prompt}]
}

# Send POST request to OpenRouter
try:
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=20
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response Text:\n{response.text}")
    print(f"Headers Sent: {headers}")
    print(f"Payload Sent: {payload}")

    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        print("\nLLM Response Content:\n", content)
    else:
        print(f"\nError occurred: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    print(f"RequestException: {str(e)}")
