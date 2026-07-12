from .version import get_cli_version
import typer

app = typer.Typer()


@app.command()
def version():
    """To get the current cli version installed"""
    get_cli_version()


@app.command()
def greet(name: str, twice: bool = False):
    """
    A simple greeting CLI utility using Typer.
    """
    greeting = f'Hello, {name}!'
    typer.echo(greeting)
    if twice:
        typer.echo(greeting)


@app.command()
def goodbye(name: str):
    """
    Bid farewell to someone.
    """
    typer.echo(f'Goodbye, {name}!')


def run():
    app()
