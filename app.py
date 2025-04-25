import logging

import requests
from flask import Flask, jsonify, request

import config
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
        event = data.get("event", {})
        if event.get("type") == "app_mention":
            try:
                user_id = event.get("user")
                channel = event.get("channel")
                mention = f"<@{user_id}>"
                user_text = event.get("text").replace(mention, "").strip()

                # 檢查是否有圖片
                files = event.get("files", [])
                if files and "url_private" in files[0]:
                    try:
                        img_url = files[0]["url_private"]
                        response = requests.post(
                            "https://healthy-escargot-pure.ngrok-free.app/predict",
                            json={"url": img_url},
                            headers={"Content-Type": "application/json"},
                            timeout=40,
                        )
                        result = response.json()  # 把回傳內容轉成 JSON 字典
                        prediction = result.get("prediction")
                        user_text = f"這是我從圖片中得到的資訊：{prediction}，然後我想說：{user_text}"
                        response_text = ai_service.chat(user_text)

                    except Exception as e:
                        logger.error("Error processing image: %s", e)
                else:
                    response_text = ai_service.chat(user_text)

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

    return jsonify({"status": "ignored", "message": "No action taken"}), 200


if __name__ == "__main__":
    app.run(debug=True)
