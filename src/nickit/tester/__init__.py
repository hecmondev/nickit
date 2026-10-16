from .commands import app as tester_app
from typer import Typer

app = Typer()

app.add_typer(tester_app)
