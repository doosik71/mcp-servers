import asyncio
import io
import httpx
from PyPDF2 import PdfReader
from mcp.server.fastmcp import FastMCP


# Initialize the FastMCP server
mcp = FastMCP(
    name="PDFTextExtractor", json_response=True)


@mcp.tool()
async def extract_text_from_pdf_url(pdf_url: str) -> str:
    """
    Extracts all text content from a PDF document located at the given URL.

    Args:
        pdf_url (str): The URL of the PDF document.

    Returns:
        str: The concatenated text content of the PDF.

    Raises:
        httpx.RequestError: If there's an error making the HTTP request to the PDF URL.
        httpx.HTTPStatusError: If the HTTP request returns a non-2xx status code.
        Exception: For any errors during PDF parsing.
    """

    all_text = []

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(pdf_url, follow_redirects=True, timeout=30.0)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

            # Read PDF from bytes
            pdf_file = io.BytesIO(response.content)

            reader = PdfReader(pdf_file)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    all_text.append(text)

            return {text: "\n".join(all_text)}
        except httpx.RequestError as e:
            raise httpx.RequestError(
                f"Error requesting PDF from {pdf_url}: {e}")
        except httpx.HTTPStatusError as e:
            raise httpx.HTTPStatusError(
                f"HTTP error for {pdf_url}: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            raise Exception(f"Error parsing PDF from {pdf_url}: {e}")

if __name__ == "__main__":
    asyncio.run(mcp.run())
