# textkit

Small text utilities (`slugify`, `word_count`, `truncate`, `is_palindrome`) plus a tiny CLI.
Right now this is just loose scripts. **Your job: turn it into an installable Python package.**

Try it as-is:

```bash
pip install pytest
pytest
python cli.py slug "Hello, World!"
```

## Packaging TODO

1. Create a `src/textkit/` folder and move `text_utils.py`, `helpers.py`, `cli.py` into it.
2. Add `src/textkit/__init__.py` exposing the public API and a `__version__`.
3. Fix the imports in `text_utils.py` and `cli.py` (they only work when run from this folder; use relative imports).
4. Write a `pyproject.toml` (build backend, name, version, description, `requires-python`, license, readme).
5. Add a console script entry point so `textkit slug "Hello"` works (`[project.scripts]`).
6. Move `test_text_utils.py` into `tests/` and update its imports to `from textkit import ...`.
7. Install locally with `pip install -e .` and confirm `pytest` and the `textkit` command work.
8. Build with `python -m build` and check `dist/` contains a wheel and sdist.
9. (Optional) Add a GitHub Actions workflow that runs tests, and upload to TestPyPI with `twine`.
