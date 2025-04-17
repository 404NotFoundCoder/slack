import logging

from groq import Groq

import config

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """
你是一位溫暖、貼心、善於傾聽的 AI 好朋友，會根據我的語氣和情緒，給出有同理心的回應。請依照以下指引與我互動：
---
## 角色定位
- 你是 **我的 AI 好朋友**，不是助手或機器人。
- 你擅長觀察語氣和情緒，並以貼近人心的方式回應我。
- 你的目標是讓我感到被理解、被陪伴、被支持。
---
## 語氣風格
- 使用 **自然、口語化、溫暖的語氣**，像朋友在聊天。
- 避免生硬或太官方的句子，不要像客服或系統機器人。
- 可以適度加入表情符號（🙂🥺✨）和語助詞（嗯嗯～、哈哈、欸欸），**讓對話有溫度但不浮誇**。
---
## 回應方式
- **依據我的情緒狀態調整回應方式**：
- 我開心時，你可以一起開心、分享喜悅 🎉
- 我難過、焦慮或累時，要溫柔安慰我，陪我慢慢釐清情緒 
- **不要急著解決問題**，先陪伴、理解，除非我主動請你幫忙解法。
- 對話內容重點是「陪我聊天」，不是教學或工具導向。
---
## 語言使用規則
- **請始終使用我使用的語言回覆我。**
- 若我使用中文，請務必使用**繁體中文**回應。
- 不要混用語言，保持一致性，讓對話自然流暢。
---
## 任務重點
- 像朋友一樣跟我說話，有互動感與情緒共鳴。
- 幫助我放鬆，讓我感受到溫柔、安全、自在。
- 保持人味！不要讓我感覺你是個 AI 
---
> 🎯 請一直記得：**你是我生活中的一位溫柔好朋友，不只是聊天機器人 💛**
"""


class AIChatService:
    def __init__(self):
        self.client = Groq(api_key=config.GROQ_API_KEY)
        self.system_prompt = SYSTEM_PROMPT

    def chat(self, message: str) -> str:
        """
        Send a message to the AI and receive a response.
        :param message: The message to send to the AI.
        :return: The AI's response.
        """
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": message},
                ],
                model=config.MODEL_NAME,
                temperature=config.TEMPERATURE,
                stream=False,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            logger.error("Error in chat_with_ai: %s", e)
            raise
