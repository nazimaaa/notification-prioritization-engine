from flask import Flask, request, jsonify
from decision_engine import NotificationEngine

app = Flask(__name__)
engine = NotificationEngine()


@app.route("/notification", methods=["POST"])
def handle_notification():

    event = request.json

    if not event or "user_id" not in event or "event_type" not in event:
        return jsonify({"error": "Invalid input"}), 400

    decision, explanation = engine.classify(event)

    return jsonify({
        "decision": decision,
        "explanation": explanation
    })


if __name__ == "__main__":
    app.run(debug=True)