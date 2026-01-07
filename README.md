# mcp-servers

This repository contains two Micro-Agent Control Protocol (MCP) servers implemented in Python: one for searching arXiv and another for extracting text from PDF documents via URL. These servers expose tools that can be consumed by an MCP client.

## Setup

This project uses `uv` for dependency management.

1. **Install dependencies**:

   ```bash
   uv sync
   ```

## 1. arXiv Search Server (`mcp_arxiv_server.py`)

This server provides a tool to search for academic papers on arXiv based on keywords.

### Tool: `search_arxiv`

- **Description**: Searches arXiv for papers matching a keyword in the title or abstract.
- **Arguments**:
  - `keyword` (str): The keyword to search for.
- **Returns**: A list of dictionaries, where each dictionary represents a paper with its `title`, `authors`, `published_year`, `pdf_url`, and `summary`.

## 2. PDF Text Extraction Server (`mcp_pdf_server.py`)

This server provides a tool to extract all text content from a PDF document given its URL.

### Tool: `extract_text_from_pdf_url`

- **Description**: Extracts all text content from a PDF document located at the given URL.
- **Arguments**:
  - `pdf_url` (str): The URL of the PDF document.
- **Returns**: A string containing the concatenated text content of the PDF.
