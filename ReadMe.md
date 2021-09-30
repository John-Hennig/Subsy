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

[![documentation](
    https://readthedocs.org/projects/subsy/badge/?version=latest)](
    https://subsy.readthedocs.io/en/latest)
[![release](
    https://img.shields.io/pypi/v/subsy.svg)](
    https://pypi.python.org/pypi/subsy)
[![license](
    https://img.shields.io/badge/License-MIT-green.svg)](
    https://github.com/John-Hennig/Subsy/blob/main/license.txt)

----

# CI/CD

I published this library mostly to use as a demo project for continuous
integration, for me to learn how to set up and configure the various CI
services by different providers. For the small, pure-Python package that
this is, such effort is certainly overkill. But the configuration files
would not be all that different for big projects. And the limitations
of the CI services would be the same. The goal for each of them: Make
sure the tests pass for all supported Python versions and on the three
major platforms: Linux, Windows, macOS.

![coverage](tests/coverage.svg?raw=true)
[![Travis CI](
    https://img.shields.io/travis/John-Hennig/Subsy?label=TravisCI)](
    https://app.travis-ci.com/John-Hennig/Subsy)
[![CircleCI](
    https://img.shields.io/circleci/build/github/John-Hennig/Subsy?label=CircleCI)](
    https://circleci.com/gh/John-Hennig/Subsy)
