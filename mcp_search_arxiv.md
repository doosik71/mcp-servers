# Arxiv Search

- `.gemini\settings.json` 파일에 아래 내용을 추가하세요.

```json
{
  "mcpServers": {
    "search_arxiv": {
      "command": "D:\\dev\\python\\mcp-servers\\.venv\\Scripts\\python.exe",
      "args": ["D:\\dev\\python\\mcp-servers\\mcp_search_arxiv.py"]
    }
  }
}
```
