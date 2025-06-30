# 必要なのは自分でインストールしてね
import requests
import os
from dotenv import load_dotenv

# apikeyは自分で入れる
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 適当にllmに聞きたいこと入れてね
prompt = "今日の献立考えて"

payload = {
    "model": "meta-llama/llama-4-scout:free",
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

response = requests.post(API_URL, headers=headers, json=payload)

if response.status_code == 200:
    reply = response.json()["choices"][0]["message"]["content"]
    print("Llama-4-Scoutの応答:\n", reply)
else:
    print("Error:", response.status_code, response.text)
