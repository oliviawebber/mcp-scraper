import typer

app = typer.Typer()


@app.command()
def tool(url: str):
    print(f"Reaching out to {url}...")


@app.command()
def resource(url: str):
    print("Foo")


if __name__ == "__main__":
    app()
