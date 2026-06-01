from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

SYSTEM_PROMPT = """
You are Azure Dost AI.
Explain Azure and cloud concepts to non-IT beginners in simple Hindi-English.
Use real-life examples and beginner-friendly language.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    full_prompt = SYSTEM_PROMPT + "\nUser question: " + user_message

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "user", "content": full_prompt}
            ]
        }
    )

    ai_reply = response.json()["choices"][0]["message"]["content"]

    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
