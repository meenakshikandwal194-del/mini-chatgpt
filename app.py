from flask import Flask, request, jsonify, render_template
from google import genai
import os

app = Flask(__name__)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

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

    prompt = SYSTEM_PROMPT + "\nUser question: " + user_message

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
