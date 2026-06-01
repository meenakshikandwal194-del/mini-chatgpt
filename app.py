from flask import Flask, request, jsonify, render_template
from groq import Groq
import os

app = Flask(__name__)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    ai_reply = completion.choices[0].message.content

    return jsonify({
        "reply": ai_reply
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
