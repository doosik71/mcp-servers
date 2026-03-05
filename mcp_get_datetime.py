from datetime import datetime
from mcp.server.fastmcp import FastMCP  # type: ignore
import asyncio


mcp = FastMCP("get_datetime", json_response=True)


@mcp.tool()
async def get_datetime() -> dict:
    """
    Returns local system date and time information.

    Returns:
        A dictionary containing ISO datetime, date, time, timezone, and unix timestamp.
    """
    now = datetime.now().astimezone()

    return {
        "iso_datetime": now.isoformat(),
        "date": now.date().isoformat(),
        "time": now.time().isoformat(timespec="seconds"),
        "timezone": str(now.tzinfo),
        "unix_timestamp": now.timestamp(),
    }


if __name__ == "__main__":
    asyncio.run(mcp.run())
