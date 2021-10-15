Steps to take when releasing a new version:
* Bump version number and enter current date in `meta.py`.
* Add the release notes to `docs/releases.md`.
* Add a dedicated commit for the version bump.
* Tag the commit with the version number, for example: `git tag 1.0.1`.
* Push to GitHub: `git push origin main`.
* Check that documentation built successfully on Read-the-Docs.
* Publish to PyPI by running `deploy/publish.py`.
* Check that meta information is correct on PyPI.
* Then push the tag: `git push --tags`.
