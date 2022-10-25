# cookiecutter-apton-py

<p align="center"><img alt="logo" src="docs/_static/logo.png" width="50%" /></p>

[Cookiecutter] template for an Apton Python package based on the
[Hypermodern Python] article series.

✨📚✨ [Read the full documentation][readthedocs page]

[cookiecutter]: https://github.com/audreyr/cookiecutter
[hypermodern python]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769

## Usage

The first time using this template run:

```console
$ cookiecutter gh:apton/cookiecutter-apton-py
```

Subsequently you can run:

```console
$ cookiecutter cookiecutter-apton-py
```

You can also create a `~/.cookiecutterrc` file with an abbreviation:

```
default_context:
  author: "John Didion"
  email: "John.Didion@aptonbio.com"
  github_user: "jdidion"
  version: 0.1.0
abbreviations:
    apton: https://github.com/aptonbio/cookiecutter-apton-py.git
    gh: https://github.com/{0}.git
```

And then run:

```console
$ cookiecutter apton
```

## Features

<!-- features-begin -->

- Packaging and dependency management with [Poetry]
- Test automation with [Nox]
- Linting with [pre-commit] and [Flake8]
- Continuous integration with [GitHub Actions]
- Documentation with [Sphinx] and [MyST] using the [furo] theme
- Automated uploads to [PyPI] and [TestPyPI]
- Automated release notes with [Release Drafter]
- Automated dependency updates with [Dependabot]
- Code formatting with [Black] and [Prettier]
- Import sorting with [isort]
- Testing with [pytest]
- Code coverage with [Coverage.py]
- Coverage reporting with [Codecov]
- Command-line interface with [Typer]
- Static type-checking with [mypy]
- Runtime type-checking with [Typeguard]
- Automated Python syntax upgrades with [pyupgrade]
- Security audit with [Bandit] and [Safety]
- Check documentation examples with [xdoctest]
- Generate API documentation with [autodoc] and [napoleon]
- Manage project labels with [GitHub Labeler]

The template supports Python 3.7, 3.8, 3.9, and 3.10.

[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[bandit]: https://github.com/PyCQA/bandit
[black]: https://github.com/psf/black
[codecov]: https://codecov.io/
[coverage.py]: https://coverage.readthedocs.io/
[dependabot]: https://dependabot.com/
[flake8]: http://flake8.pycqa.org
[furo]: https://pradyunsg.me/furo/
[github actions]: https://github.com/features/actions
[github labeler]: https://github.com/marketplace/actions/github-labeler
[isort]: https://pycqa.github.io/isort/
[mypy]: http://mypy-lang.org/
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[pypi]: https://pypi.org/
[pytest]: https://docs.pytest.org/en/latest/
[pyupgrade]: https://github.com/asottile/pyupgrade
[read the docs]: https://readthedocs.org/
[release drafter]: https://github.com/release-drafter/release-drafter
[safety]: https://github.com/pyupio/safety
[sphinx]: http://www.sphinx-doc.org/
[testpypi]: https://test.pypi.org/
[typeguard]: https://github.com/agronholm/typeguard
[typer]: https://github.com/tiangolo/typer
[xdoctest]: https://github.com/Erotemic/xdoctest

<!-- features-end -->
