# Send Telegram

- `.gemini\settings.json` 파일에 아래 내용을 추가하세요.

```json
{
  "mcpServers": {
    "send_telegram": {
      "command": "D:\\dev\\python\\mcp-servers\\.venv\\Scripts\\python.exe",
      "args": ["D:\\dev\\python\\mcp-servers\\mcp_send_telegram.py"]
    }
  }
}
```

## Tool

- `send_telegram(chat_id: str, text: str, token: str | None = None)`
- `chat_id`로 지정된 Telegram 수신자에게 메시지를 전송
- `token` 미지정 시 환경변수 `TELEGRAM_BOT_TOKEN` 사용
- 반환값: Telegram Bot API JSON 응답
