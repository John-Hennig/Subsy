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

[![release](
    https://img.shields.io/pypi/v/subsy.svg?label=release)](
    https://pypi.python.org/pypi/subsy)
[![documentation](
    https://readthedocs.org/projects/subsy/badge/?version=latest)](
    https://subsy.readthedocs.io/en/latest)


----


## Continuous integration

I published this library mostly to use as a demo project for continuous
integration, for me to learn how to set up and configure the various CI
services by different providers. For the small, pure-Python package that
this is, such effort is certainly overkill. But the configuration files
would not be all that different for bigger projects. And the limitations
of the CI services would be the same.

The goal for each of them: Make sure the tests pass for all supported
Python versions on all three platforms: Linux, Windows, macOS. GitHub
Actions was by far the easiest to set up. CircleCI is similarly easy,
and unlike any other provider offers terminal access to the test runner
for debugging purposes, but does not support macOS in the free plan.
Travis CI and AppVeyor are the veterans, and it shows. The configuration
syntax is clunky, less streamlined and flexible than the competition's.
Buddy is easy to use, but lacks features and macOS support. I wanted to
test Azure Pipelines, but, of late, Microsoft requires application via
email for the free plan, and I couldn't be bothered. For projects
already on GitHub, there is little reason to use anything but GitHub
Actions.

[![Travis CI](
    https://img.shields.io/travis/john-hen/Subsy?label=TravisCI)](
    https://app.travis-ci.com/john-hen/Subsy)
[![AppVeyor](
    https://img.shields.io/appveyor/build/john-hennig/Subsy?label=AppVeyor)](
    https://ci.appveyor.com/project/john-hennig/subsy)
[![CircleCI](
    https://img.shields.io/circleci/build/github/john-hen/Subsy?label=CircleCI)](
    https://circleci.com/gh/john-hen/Subsy)
[![GitHub](
    https://img.shields.io/github/workflow/status/john-hen/Subsy/Test%20commit?label=GitHub)](
    https://github.com/john-hen/Subsy/actions/workflows/test_commit.yml)
[![Buddy](
    https://app.buddy.works/jhen/subsy/pipelines/pipeline/351696/badge.svg?token=09080438c2a13e8c074ec45e5dc023682ae8c8e825ef8b6e8616aa8ee8ab2dfe)](
    https://app.buddy.works/jhen/subsy/pipelines/pipeline/351696)

[![codecov](
    https://codecov.io/gh/john-hen/Subsy/branch/main/graph/badge.svg?token=V5B66MCAFF)](
    https://codecov.io/gh/john-hen/Subsy)
[![Codacy](
    https://img.shields.io/codacy/grade/271baf9c33714b88bcf95e915532a692?label=Codacy)](
    https://www.codacy.com/gh/john-hen/Subsy)
