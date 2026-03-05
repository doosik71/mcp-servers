# Write File

- `.gemini\settings.json` 파일에 아래 내용을 추가하세요.

```json
{
  "mcpServers": {
    "write_file": {
      "command": "D:\\dev\\python\\mcp-servers\\.venv\\Scripts\\python.exe",
      "args": ["D:\\dev\\python\\mcp-servers\\mcp_write_file.py"]
    }
  }
}
```

## Tool

- `write_file(file_path: str, content: str, encoding: str = "utf-8", append: bool = False, create_dirs: bool = True)`
- 현재 디렉터리 및 하위 디렉터리 파일만 쓰기 가능
- 현재 디렉터리 상위 경로 접근은 차단
- 반환값: `path`, `mode`, `written_chars`
