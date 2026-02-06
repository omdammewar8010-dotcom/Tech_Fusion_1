from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple FAQ database (Level 1)
FAQS = {
    "admission process": "You can apply online through the official website.",
    "fees structure": "The fees structure is available on the official website.",
    "office hours": "The office is open from 9 AM to 5 PM, Monday to Friday.",
    "contact details": "You can contact us at support@institution.edu",
}

@app.route("/")
def home():
    return "AI Customer Support Assistant is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    for question, answer in FAQS.items():
        if question in user_message:
            return jsonify({"reply": answer})

    return jsonify({
        "reply": "Sorry, I couldn’t find an answer. Please contact the administration."
    })

if __name__ == "__main__":
    app.run(debug=True)
