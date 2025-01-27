from flask import Flask, request, jsonify
from flask_cors import CORS
from llm_handler import get_llm_response

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests for the frontend


@app.route("/")
def home():
    return "Flask backend is running!"


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    history = data.get("history", "")
    question = data.get("question", "")
    try:
        # print test 
        print("test ehsan")
        response = get_llm_response(history, question)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 5001


if __name__ == "__main__":
    app.run(debug=True)
