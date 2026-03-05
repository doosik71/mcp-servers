from mcp.server.fastmcp import FastMCP  # type: ignore
from pathlib import Path
import asyncio


mcp = FastMCP("write_file", json_response=True)


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
async def write_file(
    file_path: str,
    content: str,
    encoding: str = "utf-8",
    append: bool = False,
    create_dirs: bool = True,
) -> dict:
    """
    Writes text content to a file in the current directory tree.

    Args:
        file_path: Relative file path to write.
        content: Text content to write.
        encoding: Text encoding. Defaults to utf-8.
        append: If True, appends instead of overwriting.
        create_dirs: If True, creates missing parent directories.

    Returns:
        A dictionary containing path, mode, and written length.
    """
    target_path = _resolve_safe_path(file_path)

    if target_path.exists() and not target_path.is_file():
        raise IsADirectoryError(f"Path is not a file: {file_path}")

    if create_dirs:
        target_path.parent.mkdir(parents=True, exist_ok=True)

    mode = "a" if append else "w"
    with target_path.open(mode=mode, encoding=encoding) as f:
        f.write(content)

    return {
        "path": str(target_path),
        "mode": "append" if append else "write",
        "written_chars": len(content),
    }


if __name__ == "__main__":
    asyncio.run(mcp.run())
