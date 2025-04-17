import logging

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import config

logger = logging.getLogger(__name__)


class SlackService:
    def __init__(self):
        self.client = WebClient(token=config.SLACK_BOT_TOKEN)

    def send_message(self, channel: str, text: str):
        """
        Send a message to a Slack channel.
        :param channel: The Slack channel ID to send the message to.
        :param text: The message text to send.
        :return: The response from the Slack API.
        """
        try:
            result = self.client.chat_postMessage(channel=channel, text=text)
            logger.info("Message posted: %s", result)
            return result
        except SlackApiError as e:
            logger.error("Error posting message: %s", e)
            raise
