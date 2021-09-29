"""Measures code coverage by test suite."""

from subprocess import run
from pathlib import Path

here = Path(__file__).resolve().parent
root = here.parent
file = here/'coverage.sqlite'

print('Running test suite.')
run(['pytest', '--cov'], cwd=root)

print('Exporting coverage report.')
folder = (here/'coverage').relative_to(root)
run(['coverage', 'html', f'--directory={folder}'], cwd=root)

print('Rendering coverage badge.')
badge = root/'tests'/file.with_suffix('.svg').name
run(['coverage-badge', '-f', '-o', str(badge)], cwd=root)
