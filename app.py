from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("sk-tF5tFCGIJIxHs70Dn6krSb4CPoXaSZDAx9W4tujntvIlZ9dv")
BASE_URL = "https://api.gapgpt.app/v1/chat/completions"

@app.route("/")
def home():
    return "MoonAI Backend Running 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gapgpt",
        "messages": [
            {"role": "system", "content": "You are MoonAI, a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    }

    try:
        response = requests.post(BASE_URL, json=payload, headers=headers)
        data = response.json()
        bot_reply = data["choices"][0]["message"]["content"]
        return jsonify({"reply": bot_reply})
    except:
        return jsonify({"reply": "خطا در دریافت پاسخ از MoonAI"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
