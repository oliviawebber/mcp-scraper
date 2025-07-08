import typer


def main(url: str):
    print(f"Reaching out to {url}...")


if __name__ == "__main__":
    typer.run(main())
