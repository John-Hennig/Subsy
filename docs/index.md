# Subsy
*Access to subtitles from various file formats*

This library is not fundamentally different from established ones, but
offers some helpful abstractions that those others don't. First and
foremost, subtitles loaded from a file are represented as a linked list.
This makes it possible to implement search patterns and sanitization
strategies that take the preceding or following subtitle into account,
for example to recognize a running sentence.

```python
>>> import subsy
>>> subtitles = subsy.load('subtitles.srt')
>>> first = subtitles[0]
>>> first.text
'How are you?'
>>> second = first.next
>>> second.text
'great, thanks.'
>>> second.text = 'Great, thanks.'
>>> subtitles.save()
```

Subtitles can be loaded from and saved to these file formats:
* Subrip (`.srt`)
* Advanced Substation Alpha (`.ass`)
* Substation Alpha (`.ssa`)
* WebVTT (`.vtt`)
* SubViewer (`.sub`)

The text encoding of input files is detected automatically.

[![license](
    https://img.shields.io/badge/License-MIT-green.svg?label=license)](
    https://github.com/john-hen/Subsy/blob/main/license.txt)
[![release](
    https://img.shields.io/pypi/v/subsy.svg?label=PyPI)](
    https://pypi.python.org/pypi/subsy)
[![source](
    https://img.shields.io/github/stars/john-hen/Subsy?label=GitHub&style=social)](
    https://github.com/john-hen/Subsy)

```{toctree}
:hidden:

installation
tutorial
api
releases
```
