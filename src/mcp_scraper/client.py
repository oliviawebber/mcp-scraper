from contextlib import asynccontextmanager

from mcp import ClientSession
from mcp.client.sse import sse_client


@asynccontextmanager
async def get_client(url: str):
    async with sse_client(url) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            yield session
