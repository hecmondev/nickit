from inspect import cleandoc
from nickit.constants import COMMAND_SUCCESS
from nickit.message import show_information_message, show_success_message
from pathlib import Path
from re import match
from subprocess import run
from typer import Typer

app = Typer()


def start_project():
    """Checking out if uv is installed"""
    command = 'uv --version'
    result = run(command, capture_output=True, text=True, shell=True)

    pattern = r'^uv \d+.\d+.\d+'
    if not match(pattern, result.stdout):
        show_information_message('uv is not found then installing...')
        # installing uv
        run(
            'powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"'
        )
        # adding uv into path on windows
        run(
            '$env:Path = "C:\\Users\\User\\.local\\bin;$env:Path"',
            capture_output=True,
            text=True,
            shell=True,
        )

    show_information_message('creating a new project using uv')
    result = run('uv init', capture_output=True, text=True, shell=True)
    if result.returncode == COMMAND_SUCCESS:
        show_success_message('project structure created')


def create_vscode_dir() -> Path:
    """Creating .vscode folder

    Returns:
        Path: including the new folder created
    """
    vscode_dir_path = Path().resolve() / '.vscode'
    vscode_dir_path.mkdir(parents=True, exist_ok=True)
    return vscode_dir_path


def create_settings_file(vscode_dir_path: Path):
    """Creating settings.json file under .vscode folder"""
    settings_file_path = vscode_dir_path / 'settings.json'
    with open(settings_file_path, 'w') as file:
        setting = """
            {
                "[python]": {
                    "editor.defaultFormatter": "charliermarsh.ruff",
                    "editor.formatOnSave": true,
                    "editor.codeActionsOnSave": {
                        "source.fixAll": "explicit",
                        "source.organizeImports": "explicit"
                    }
                },
                "editor.tabSize": 4,
            }
        """
        file.write(cleandoc(setting))
    show_success_message('.vscode/settings.json was added successfully')


def create_ruff_file():
    """Creating ruff.toml file"""
    ruff_file_path = Path().resolve() / 'ruff.toml'
    with open(ruff_file_path, 'w') as file:
        ruff = """
            # Exclude a variety of commonly ignored directories.
            exclude = [
            ".bzr",
            ".direnv",
            ".eggs",
            ".git",
            ".git-rewrite",
            ".hg",
            ".ipynb_checkpoints",
            ".mypy_cache",
            ".nox",
            ".pants.d",
            ".pyenv",
            ".pytest_cache",
            ".pytype",
            ".ruff_cache",
            ".svn",
            ".tox",
            ".venv",
            ".vscode",
            "__pypackages__",
            "_build",
            "buck-out",
            "build",
            "dist",
            "node_modules",
            "site-packages",
            "venv",
            "env"
            ]

            # Same as Black.
            line-length = 88
            indent-width = 4

            # Support Python 3.14+.
            target-version = "py314"

            [lint]
            # Enable Pyflakes (`F`) and a subset of the pycodestyle (`E`)  codes by default.
            # Unlike Flake8, Ruff doesn't enable pycodestyle warnings (`W`) or
            # McCabe complexity (`C901`) by default.
            select = ["E4", "E7", "E9", "F"]
            ignore = []

            # Allow fix for all enabled rules (when `--fix`) is provided.
            fixable = ["ALL"]
            unfixable = []

            # Allow unused variables when underscore-prefixed.
            dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

            # Custom isort settings
            [lint.isort]
            from-first = true
            no-sections = true
            order-by-type = true
            # for aliases begin
            force-wrap-aliases = true
            combine-as-imports = true
            # for aliases end

            [format]
            # Like Black, use double quotes for strings.
            quote-style = "single"

            # Like Black, indent with spaces, rather than tabs.
            indent-style = "space"

            # Like Black, respect magic trailing commas.
            skip-magic-trailing-comma = false

            # Like Black, automatically detect the appropriate line ending.
            line-ending = "auto"

            # Enable auto-formatting of code examples in docstrings. Markdown,
            # reStructuredText code/literal blocks and doctests are all supported.
            #
            # This is currently disabled by default, but it is planned for this
            # to be opt-out in the future.
            docstring-code-format = false

            # Set the line length limit used when formatting code snippets in
            # docstrings.
            #
            # This only has an effect when the `docstring-code-format` setting is
            # enabled.
            docstring-code-line-length = "dynamic"
        """
        file.write(cleandoc(ruff))


def add_fastapi():
    """Add fastapi on the project"""
    result = run(
        'uv add "fastapi[standard]"', capture_output=True, text=True, shell=True
    )

    if result.returncode == COMMAND_SUCCESS:
        show_success_message('fastapi was added successfully')


@app.command()
def project(fastapi: bool = False):
    """It's going to init some important files in the project to follow up a right structure"""
    # init project using uv
    start_project()

    # adding ruff file
    create_ruff_file()

    # adding settings file under vscode folder
    vscode_dir_path = create_vscode_dir()
    create_settings_file(vscode_dir_path)

    # adding fastapi
    if fastapi:
        add_fastapi()

    show_success_message('project has been initialized successfully')
