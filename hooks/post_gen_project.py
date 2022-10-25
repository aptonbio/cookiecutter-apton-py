#!/usr/bin/env python
import json
import os
from pathlib import Path


REMOVE_PATHS = [
    '{% if cookiecutter.project_type != "bin" -%} src/{{ cookiecutter.package_name }}/__main__.py {%- endif -%}',
]


def remove_optional_paths():
    for path_str in REMOVE_PATHS:
        path_str = path_str.strip()
        if path_str:
            path = Path(path_str)
            if path.exists():
                if path.is_dir():
                    os.rmdir(path)
                else:
                    path.unlink()


def reindent_cookiecutter_json():
    """Indent .cookiecutter.json using two spaces.

    The jsonify extension distributed with Cookiecutter uses an indentation
    width of four spaces. This conflicts with the default indentation width of
    Prettier for JSON files. Prettier is run as a pre-commit hook in CI.
    """
    path = Path(".cookiecutter.json")

    with path.open() as io:
        data = json.load(io)

    with path.open(mode="w") as io:
        json.dump(data, io, sort_keys=True, indent=2)
        io.write("\n")


if __name__ == "__main__":
    remove_optional_paths()
    reindent_cookiecutter_json()
