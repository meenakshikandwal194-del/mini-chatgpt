app.run(debug=True)app.run(host="0.0.0.0", port=5000)
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": user_message,
            "stream": False
        }
    )

    ai_reply = response.json()["response"]
    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    app.run(debug=True)
