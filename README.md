# 專案名稱

這是一個基於 Flask 的應用程式，整合了 Slack 和 AI 聊天服務。

## 目錄結構

- `app.py`: 主應用程式文件，處理 Slack 事件並調用 AI 聊天服務。
- `services/ai_chat_service.py`: AI 聊天服務的實現。
- `services/slack_service.py`: 與 Slack API 交互的服務。
- `config.py`: 配置文件，從環境變量中加載 API 密鑰和其他配置。
- `.env`: 環境變量文件，存儲敏感信息如 API 密鑰。
- `requirements.txt`: Python 依賴包列表。

## 環境設置

1. **克隆此專案**：

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **創建虛擬環境並安裝依賴**：

   ```bash
   python -m venv venv
   source venv/bin/activate  # 對於Windows使用者，使用 `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **配置環境變量**：
   - 填寫 `.env` 文件中的 `SLACK_BOT_TOKEN` 和 `GROQ_API_KEY`。

## 運行應用

啟動 Flask 應用：

```bash
python app.py
```

應用將在 `http://localhost:5000` 運行。

## 功能簡介

這是一個整合了 Slack、AI 模型與圖像辨識的智慧聊天應用，讓你可以直接在 Slack 裡與一位「溫暖、貼心、會看圖說話」的 AI 好朋友互動 😊

---

### 🎯 支援功能

- **Slack 事件處理**

  - 即時接收並處理 Slack 上的訊息事件
  - 自動識別是否被 @mention，並啟動 AI 回應流程
  - 避免重複處理、過濾機器人自己的訊息，保持互動流暢

- **辛普森家庭圖片辨識 + 對話理解**

  - 當你傳入圖片時，系統會進行圖像辨識
  - 辨識出辛普森家庭角色（如：Bart、Lisa、Homer、marge 等）
  - 接著你可以針對圖片中的人物提問，例如：
    - 幫我介紹一下他
    - 他個性怎麼樣？
    - 他喜歡什麼？

- **日常聊天功能**
  - 就算沒有傳圖片，也能直接聊天
  - 你可以分享情緒、提問、討論生活瑣事，AI 會根據語氣與情境回應
  - 風格像朋友，帶點貼心、有點可愛，不會像客服一樣死板 ❣️

---

### 📦 使用情境範例

- 📷 上傳一張 Bart 的圖片 + 問「他是誰？」→ AI 幫你介紹他
- 💬 直接問「我今天心情有點低落」→ AI 溫柔陪伴你

## 配置

- **GROQ_API_KEY**: 用於 AI 聊天服務的 API 密鑰。
- **SLACK_BOT_TOKEN**: 用於與 Slack API 交互的機器人令牌。
- **MODEL_NAME**: 使用的 AI 模型名稱。
- **TEMPERATURE**: AI 生成文本的溫度設置，影響生成文本的隨機性。

## 依賴

- Flask
- python-dotenv
- requests
- slack-sdk
- groq

## 貢獻

歡迎提交問題和請求合併。請遵循標準的 Git 工作流程。
