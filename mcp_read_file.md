# Read File

- `.gemini\settings.json` 파일에 아래 내용을 추가하세요.

```json
{
  "mcpServers": {
    "read_file": {
      "command": "D:\\dev\\python\\mcp-servers\\.venv\\Scripts\\python.exe",
      "args": ["D:\\dev\\python\\mcp-servers\\mcp_read_file.py"]
    }
  }
}
```

## Tool

- `read_file(file_path: str, encoding: str = "utf-8")`
- 현재 디렉터리 및 하위 디렉터리 파일만 읽기 가능
- 현재 디렉터리 상위 경로 접근은 차단
