import asyncio
from pathlib import Path


from mcp.server.fastmcp import FastMCP  # type: ignore


mcp = FastMCP("read_file", json_response=True)


def _resolve_safe_path(file_path: str) -> Path:
    base_dir = Path.cwd().resolve()
    target_path = (base_dir / file_path).resolve()

    try:
        target_path.relative_to(base_dir)
    except ValueError as exc:
        raise PermissionError(
            "Access denied: path must be within the current directory.") from exc

    return target_path


@mcp.tool()
async def read_file(file_path: str, encoding: str = "utf-8") -> dict:
    """
    Reads a text file from the current directory or its subdirectories.

    Args:
        file_path: Relative file path to read.
        encoding: Text encoding. Defaults to utf-8.

    Returns:
        A dictionary containing the resolved path and file content.
    """
    target_path = _resolve_safe_path(file_path)

    if not target_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not target_path.is_file():
        raise IsADirectoryError(f"Path is not a file: {file_path}")

    content = target_path.read_text(encoding=encoding)

    return {
        "path": str(target_path),
        "content": content,
    }


if __name__ == "__main__":
    asyncio.run(mcp.run())
