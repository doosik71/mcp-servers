# mcp-servers

This repository contains several Micro-Agent Control Protocol (MCP) servers implemented in Python. These servers expose tools that can be consumed by an MCP client.

## Setup

This project uses `uv` for dependency management.

1. **Install dependencies**:

   ```bash
   uv sync
   ```

## Tool List

### Tool: `search_web`

This server provides a tool to search the web using DuckDuckGo.

- **Description**: Searches the web and returns ranked search results from DuckDuckGo.
- **Arguments**:
  - `query` (str): The search query.
  - `max_results` (int, optional): Maximum number of results to return. Default is `10`.
- **Returns**: A list of dictionaries, where each dictionary contains `title`, `url`, and `snippet`.

### Tool: `search_arxiv`

This server provides a tool to search for academic papers on arXiv based on keywords.

- **Description**: Searches arXiv for papers matching a keyword in the title or abstract.
- **Arguments**:
  - `keyword` (str): The keyword to search for.
- **Returns**: A list of dictionaries, where each dictionary represents a paper with its `title`, `authors`, `published_year`, `pdf_url`, and `summary`.

### Tool: `extract_pdf`

This server provides a tool to extract all text content from a PDF document given its URL.

- **Description**: Extracts all text content from a PDF document located at the given URL.
- **Arguments**:
  - `pdf_url` (str): The URL of the PDF document.
- **Returns**: A string containing the concatenated text content of the PDF.

### Tool: `read_file`

This server provides a tool to read text files from the current directory and its subdirectories.

- **Description**: Reads a text file while restricting access to the current directory tree.
- **Arguments**:
  - `file_path` (str): Relative path to the file.
  - `encoding` (str, optional): Text encoding. Default is `utf-8`.
- **Returns**: A dictionary containing `path` and `content`.
- **Security**: Paths above the current directory are blocked.

### Tool: `write_file`

This server provides a tool to write text files within the current directory tree.

- **Description**: Writes text content to a file with path restrictions.
- **Arguments**:
  - `file_path` (str): Relative path to the file.
  - `content` (str): Text to write.
  - `encoding` (str, optional): Text encoding. Default is `utf-8`.
  - `append` (bool, optional): If `True`, appends to the file. Default is `False`.
  - `create_dirs` (bool, optional): If `True`, creates missing parent directories. Default is `True`.
- **Returns**: A dictionary containing `path`, `mode`, and `written_chars`.
- **Security**: Paths above the current directory are blocked.

### Tool: `get_datetime`

This server provides a tool to get local system date and time information.

- **Description**: Returns current local system date/time and timezone details.
- **Arguments**: None
- **Returns**: A dictionary containing `iso_datetime`, `date`, `time`, `timezone`, and `unix_timestamp`.

### Tool: `send_telegram`

This server provides a tool to send a message to a Telegram recipient by `chat_id`.

- **Description**: Sends a Telegram message via the Telegram Bot API.
- **Arguments**:
  - `chat_id` (str): Target chat ID.
  - `text` (str): Message text.
  - `token` (str, optional): Bot token. If omitted, `TELEGRAM_BOT_TOKEN` is used.
- **Returns**: Telegram API JSON response as a dictionary.
