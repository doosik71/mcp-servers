# Get Datetime

- `.gemini\settings.json` 파일에 아래 내용을 추가하세요.

```json
{
  "mcpServers": {
    "get_datetime": {
      "command": "D:\\dev\\python\\mcp-servers\\.venv\\Scripts\\python.exe",
      "args": ["D:\\dev\\python\\mcp-servers\\mcp_get_datetime.py"]
    }
  }
}
```

## Tool

- `get_datetime()`
- 로컬 시스템 날짜/시간 정보를 반환
- 반환 필드: `iso_datetime`, `date`, `time`, `timezone`, `unix_timestamp`
