# PDF to Text

- `.gemini\settings.json` 파일에 아래의 내용을 추가한다.

```json
{
  "mcpServers": {
    "PDFTextExtractor": {
      "command": "D:\\dev\\python\\mcp-servers\\.venv\\Scripts\\python.exe",
      "args": ["D:\\dev\\python\\mcp-servers\\mcp_pdf_server.py"]
    }
  }
}
```
