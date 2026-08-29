from pathlib import Path


def add_tester():
    pyproject_file_path = Path().resolve() / 'pyproject.toml'

    # TODO: figure out how to get project path of the nickit repo locally
    with open(pyproject_file_path, 'a') as file:
        file.write('')
        file.write('[tool.uv.sources]')
        file.write(
            'nickit = { path = "../../source/repos/pythings/nickit", editable = true }'
        )
