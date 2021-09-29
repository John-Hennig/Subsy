"""Deletes build and test artifacts."""

from pathlib import Path
from shutil import rmtree

root = Path(__file__).resolve().parent.parent

for folder in root.rglob('__pycache__'):
    rmtree(folder, ignore_errors=True)

for folder in root.rglob('.pytest_cache'):
    rmtree(folder)

for folder in ('docs', 'dist', 'coverage'):
    rmtree(root/'deploy'/folder, ignore_errors=True)
rmtree(root/'.tox', ignore_errors=True)

file = root/'deploy'/'coverage.sqlite'
if file.is_file():
    file.unlink()
