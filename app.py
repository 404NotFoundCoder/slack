import logging

from flask import Flask, jsonify, request

from services.ai_chat_service import AIChatService
from services.slack_service import SlackService

app = Flask(__name__)
ai_service = AIChatService()
slack_service = SlackService()
logger = logging.getLogger(__name__)


@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.json

    if data.get("type") == "url_verification":
        return jsonify({"challenge": data.get("challenge")})

    if data.get("type") == "event_callback":
        return handle_event_callback(data)

    return jsonify({"status": "ignored", "message": "No action taken"}), 200


def handle_event_callback(data):
    event = data.get("event", {})

    if event.get("type") == "app_mention":
        try:
            user_id = event.get("user")
            channel = event.get("channel")
            mention = f"<@{user_id}>"
            user_text = event.get("text").replace(mention, "").strip()

            ai_response = ai_service.chat(user_text)
            response_text = f"{mention} {ai_response}"

            result = slack_service.send_message(channel, response_text)

            return (
                jsonify(
                    {
                        "status": "success",
                        "slack_response": result.data,
                        "original_data": data,
                    }
                ),
                200,
            )

        except Exception as e:
            logger.error("Error handling event: %s", e)
            return jsonify({"status": "error", "error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
