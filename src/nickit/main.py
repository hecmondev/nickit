from .init import app as init_app
from .model import ask
from .tester import app as tester_app
from .upgrade import upgrade_cli
from .version import get_cli_version
from typer import Argument, Typer
from typing import Annotated

app = Typer()


@app.command()
def version():
    """get the current cli version installed"""
    get_cli_version()


@app.command()
def agent(prompt: Annotated[str, Argument()]):
    """ask something to the internal model"""
    print(ask(prompt))


@app.command()
def upgrade():
    """upgrade package globally"""
    upgrade_cli()


app.add_typer(
    init_app,
    name='init',
    help='set of subcommands to improve development starting a new project',
)

app.add_typer(
    tester_app, name='tester', help='set of subcommands to test building features'
)


def run():
    app()
