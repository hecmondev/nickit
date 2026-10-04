from .init import app as init_app
from .version import get_cli_version
from .tester import add_tester
from typer import Typer, Argument
from typing import Annotated
from .model import ask

app = Typer()


@app.command()
def version():
    """To get the current cli version installed"""
    get_cli_version()


@app.command()
def tester():
    """To add a nickit tester on this project"""
    add_tester()


@app.command()
def agent(prompt: Annotated[str, Argument()]):
    """To ask something to the internal model"""
    print(ask(prompt))


app.add_typer(
    init_app,
    name='init',
    help='A set of subcommands to improve development starting a new project',
)


def run():
    app()
