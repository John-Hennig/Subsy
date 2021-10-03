"""Tests the `subtitles` module."""

import parent # noqa F401
from subsy import Subtitles
from subsy import Subtitle
import fixtures
import pytest
from pathlib import Path


def test_init():
    with pytest.raises(TypeError):
        Subtitles(subtitles='string')
    with pytest.raises(TypeError):
        Subtitles(subtitles=['string'])
    source = {'file': 'test.srt'}
    subtitles = Subtitles(source=source)
    assert subtitles.source == source
    reference = [Subtitle(text.split('|'), start, duration)
                 for (start, duration, text) in fixtures.reference_data]
    subtitles = Subtitles(reference)
    assert subtitles.subtitles == reference
    assert subtitles.source == {}
    previous = None
    index    = 0
    for subtitle in subtitles:
        index += 1
        assert subtitle.parent == subtitles
        assert subtitle.index == index
        assert subtitle.previous == previous
        if subtitle.previous:
            assert subtitle.previous.next == subtitle
        previous = subtitle
    assert subtitles[0].previous is None
    assert subtitles[-1].next    is None


def test_iter():
    subtitle1 = Subtitle(['line'])
    subtitle2 = Subtitle(['line1', 'line2'])
    subtitles = Subtitles([subtitle1, subtitle2])
    n = 0
    for _ in subtitles:
        n += 1
    assert n == 2


def test_len():
    subtitle1 = Subtitle(['line'])
    subtitle2 = Subtitle(['line1', 'line2'])
    subtitles = Subtitles([subtitle1, subtitle2])
    assert len(subtitles) == 2


def test_contains():
    subtitle1 = Subtitle(['line'])
    subtitle2 = Subtitle(['line1', 'line2'])
    subtitles = Subtitles([subtitle1, subtitle2])
    number = 1
    assert subtitle1 in subtitles
    assert subtitle2 in subtitles
    assert 'line' in subtitles
    assert 'line1' in subtitles
    assert 'line2' in subtitles
    assert number not in subtitles


def test_getitem():
    subtitle1 = Subtitle(['line'])
    subtitle2 = Subtitle(['line1', 'line2'])
    subtitles = Subtitles([subtitle1, subtitle2])
    assert subtitles[0] == subtitle1
    assert subtitles[1] == subtitle2


def test_setitem():
    subtitle1 = Subtitle(['line'])
    subtitle2 = Subtitle(['line1', 'line2'])
    subtitles = Subtitles([subtitle1, subtitle2])
    subtitles[0] = subtitle2
    number = 1
    assert subtitles[0] == subtitle2
    subtitles[0] = 'other line'
    assert subtitles[0] == 'other line'
    subtitles[0] = ['other', 'lines']
    assert subtitles[0] == ['other', 'lines']
    with pytest.raises(TypeError):
        subtitles[0] = number


def test_eq():
    reference = fixtures.reference()
    ref_copy  = Subtitles([Subtitle(text.split('|'), start, duration)
                           for (start, duration, text)
                           in fixtures.reference_data])
    different = Subtitles([Subtitle(['line']), Subtitle(['line1', 'line2'])])
    number = 1
    assert reference == ref_copy
    assert reference != different
    assert different != ref_copy
    assert number != reference


def test_str():
    subtitle1 = Subtitle(['line'])
    subtitle2 = Subtitle(['line1', 'line2'])
    subtitles = Subtitles([subtitle1, subtitle2])
    assert str(subtitles) == '<unnamed>'
    subtitles.source['file'] = Path('test.srt')
    assert str(subtitles) == 'test'


def test_repr():
    subtitle1 = Subtitle(['line'])
    subtitle2 = Subtitle(['line1', 'line2'])
    subtitles = Subtitles([subtitle1, subtitle2])
    assert repr(subtitles) == 'Subtitles(<unnamed>)'
    subtitles.source['file'] = Path('test.srt')
    assert repr(subtitles) == 'Subtitles(test.srt)'


def test_save():
    reference = fixtures.reference()
    here = Path(__file__).parent
    file = here/'temp.srt'
    if file.exists():
        file.unlink()
    with pytest.raises(ValueError):
        reference.save()
    reference.save(file)
    assert file.is_file()
    file.unlink()
