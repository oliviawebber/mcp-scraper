from rich import print as rich_print

from mcp_scraper.client import get_client


async def _tools(url: str):
    async with get_client(url) as client:
        tools_result = await client.list_tools()
        for tool in tools_result.tools:
            rich_print(tool)
