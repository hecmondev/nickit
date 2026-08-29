from .init import app as init_app
from .version import get_cli_version
from .tester import add_tester
import typer

app = typer.Typer()


@app.command()
def version():
    """To get the current cli version installed"""
    get_cli_version()


@app.command()
def tester():
    """To add a nickit tester on this project"""
    add_tester()


app.add_typer(
    init_app,
    name='init',
    help='A set of subcommands to improve development starting a new project',
)


def run():
    app()
