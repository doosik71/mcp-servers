from mcp.server.fastmcp import FastMCP  # type: ignore
from typing import Any, Dict, Optional
import asyncio
import httpx
import os


mcp = FastMCP("send_telegram", json_response=True)


@mcp.tool()
async def send_telegram(chat_id: str, text: str, token: Optional[str] = None) -> Dict[str, Any]:
    """
    Sends a message to a Telegram chat using the Telegram Bot API.

    Args:
        chat_id: Target chat ID (user/group/channel).
        text: Message text to send.
        token: Optional bot token. If omitted, TELEGRAM_BOT_TOKEN env var is used.

    Returns:
        Telegram API JSON response.
    """
    bot_token = token or os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        return {
            "ok": False,
            "error": "Missing bot token. Set TELEGRAM_BOT_TOKEN or pass token.",
        }

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                data={"chat_id": chat_id, "text": text},
                timeout=20.0,
            )

        try:
            return response.json()
        except ValueError:
            return {
                "ok": False,
                "error": f"Non-JSON response (status={response.status_code})",
                "text": response.text,
            }
    except httpx.RequestError as exc:
        return {
            "ok": False,
            "error": f"Request failed: {exc}",
        }


if __name__ == "__main__":
    asyncio.run(mcp.run())
