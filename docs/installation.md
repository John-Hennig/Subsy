# Installation

Subsy is [available on PyPI][pypi] and can be readily installed via
```none
pip install subsy
```

Pip will automatically install the following dependencies:
* [Srt3][srt3] — For reading subtitles in the SubRip format.
* [Aeidon][aeidon] — For reading and writing various other formats.
* [Chardet][chardet] — To detect text encoding of input files.

Run `pip uninstall subsy` in order to remove the package from your system,
though note that this will not uninstall the dependencies.


[pypi]:    https://pypi.python.org/pypi/subsy
[srt3]:    https://pypi.org/project/srt3
[aeidon]:  https://pypi.org/project/aeidon
[chardet]: https://pypi.org/project/chardet
