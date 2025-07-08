import asyncio

import typer

from mcp_scraper.tools import _tools

app = typer.Typer()


@app.command()
def tools(url: str):
    asyncio.run(_tools(url))


@app.command()
def resource(url: str):
    print("Foo")


if __name__ == "__main__":
    app()
