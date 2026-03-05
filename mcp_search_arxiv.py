import arxiv  # type: ignore
from mcp.server.fastmcp import FastMCP  # type: ignore
from typing import List, Dict, Any


mcp = FastMCP("search_arxiv", json_response=True)


@mcp.tool()
async def search_arxiv(keyword: str) -> List[Dict[str, Any]]:
    """
    Searches arXiv for papers matching the keyword in the title or abstract.

    Args:
        keyword: The keyword to search for.

    Returns:
        A list of dictionaries, where each dictionary represents a paper with its title, authors, and publication year.
    """
    search = arxiv.Search(
        query=f'ti:"{keyword}" OR abs:"{keyword}"',
        max_results=100,
        sort_by=arxiv.SortCriterion.Relevance,
    )

    results: List[Dict[str, Any]] = []
    for r in search.results():
        authors = [author.name for author in r.authors]
        results.append(
            {
                "title": r.title,
                "authors": authors,
                "published_year": r.published.year,
                "pdf_url": r.pdf_url,
                "summary": r.summary
            }
        )

    return results

if __name__ == "__main__":
    mcp.run()
