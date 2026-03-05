# Web Search

- `.gemini\settings.json` 파일에 아래 내용을 추가하세요.

```json
{
  "mcpServers": {
    "WebSearch": {
      "command": "D:\\dev\\python\\mcp-servers\\.venv\\Scripts\\python.exe",
      "args": ["D:\\dev\\python\\mcp-servers\\mcp_search_web.py"]
    }
  }
}
```

## Tool

- `search_web(query: str, max_results: int = 10)`
- 검색 엔진: DuckDuckGo (Lite)
- 반환값: `title`, `url`, `snippet` 필드를 가진 결과 목록
