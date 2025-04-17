import os

from dotenv import load_dotenv

load_dotenv()

# 配置變量
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
MODEL_NAME = "deepseek-r1-distill-llama-70b"
TEMPERATURE = 0.8
