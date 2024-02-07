# https://macpaw.com/how-to/install-pip-mac
# https://chat.openai.com/
# https://platform.openai.com/api-keys

import requests

API_KEY = "API_KEY_FROM_https://platform.openai.com/api-keys"
API_ENDPOINT = "https://api.openai.com/v1/engines/davinci-002/completions"

def chat_with_gpt(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post(API_ENDPOINT, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return f"Error: {response.text}"

# Example usage
prompt = "How does Bitcoin work?"
response = chat_with_gpt(prompt)
print("ChatGPT:", response)









