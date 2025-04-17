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

## 功能

- **Slack 事件處理**：應用監聽 Slack 的事件，並根據事件類型進行相應的處理。
- **AI 聊天回應**：當應用被提及時，AI 服務將生成回應並發送回 Slack 頻道。

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
