import asyncio
import re
from html import unescape
from typing import Any, Dict, List
from urllib.parse import quote_plus
from mcp.server.fastmcp import FastMCP  # type: ignore
import httpx


mcp = FastMCP("WebSearch", json_response=True)


def _strip_tags(value: str) -> str:
    return re.sub(r"<[^>]+>", "", value)


@mcp.tool()
async def search_web(query: str, max_results: int = 10) -> List[Dict[str, Any]]:
    """
    Searches the web using DuckDuckGo and returns ranked results.

    Args:
        query: Search query string.
        max_results: Number of results to return (1-50).

    Returns:
        A list of dictionaries containing title, url, and snippet.
    """
    if not query.strip():
        return []

    max_results = max(1, min(max_results, 50))
    encoded_query = quote_plus(query)
    search_url = f"https://lite.duckduckgo.com/lite/?q={encoded_query}"

    async with httpx.AsyncClient() as client:
        response = await client.get(
            search_url,
            follow_redirects=True,
            timeout=30.0,
            headers={
                "User-Agent": "Mozilla/5.0 (compatible; MCPWebSearch/1.0)"},
        )
        response.raise_for_status()

    html = response.text

    # DuckDuckGo lite results generally include anchor rows and optional snippet rows.
    link_pattern = re.compile(
        r'<a rel="nofollow" href="(?P<url>[^"]+)"[^>]*>(?P<title>.*?)</a>',
        re.IGNORECASE | re.DOTALL,
    )
    snippet_pattern = re.compile(
        r'<td class="result-snippet">(?P<snippet>.*?)</td>', re.IGNORECASE | re.DOTALL)

    links = list(link_pattern.finditer(html))
    snippets = [m.group("snippet") for m in snippet_pattern.finditer(html)]

    results: List[Dict[str, Any]] = []
    for idx, link in enumerate(links):
        if len(results) >= max_results:
            break

        title = unescape(_strip_tags(link.group("title"))).strip()
        url = unescape(link.group("url")).strip()

        snippet = ""
        if idx < len(snippets):
            snippet = unescape(_strip_tags(snippets[idx])).strip()

        if title and url:
            results.append(
                {
                    "title": title,
                    "url": url,
                    "snippet": snippet,
                }
            )

    return results


if __name__ == "__main__":
    asyncio.run(mcp.run())
