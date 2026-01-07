# Arxiv Search

- `.gemini\settings.json` 파일에 아래의 내용을 추가한다.

```json
{
  "mcpServers": {
    "ArxivSearch": {
      "command": "D:\\dev\\python\\mcp-servers\\.venv\\Scripts\\python.exe",
      "args": ["D:\\dev\\python\\mcp-servers\\mcp_arxiv_server.py"]
    }
  }
}
```
