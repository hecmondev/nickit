from rich import print
from typer import colors, echo, style


def show_success_message(message: str, bold=False, background=False):
    if bold:
        template = '[bold green]%s[/]'
        template %= message
        print(template)
    elif background:
        styled = style(message, bg=colors.GREEN)
        echo(styled)
    else:
        styled = style(message, fg=colors.GREEN)
        echo(styled)
