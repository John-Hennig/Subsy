"""Tests the `readers` module."""

from subsy import readers
import fixtures
import pytest
import re
from pathlib import Path


def test_detect_encoding():
    corpus = Path(__file__).parent/'corpus'
    for file in corpus.glob('encoding_*.*'):
        encoding = re.match(r'encoding_(.+)', file.stem).group(1)
        assert readers.detect_encoding(file) == encoding


def test_read_srt():
    corpus = Path(__file__).parent/'corpus'
    file = corpus/'reference.srt'
    subtitles = readers.read_srt(file, 'UTF-8-sig')
    assert subtitles.source == {'file': file, 'encoding': 'UTF-8-sig'}
    previous = None
    for subtitle in subtitles:
        assert subtitle.previous == previous
        if previous:
            assert previous.next == subtitle
        previous = subtitle
    assert not subtitles[-1].next
    assert subtitles == fixtures.reference()
    newlines = [readers.read_srt(file, 'UTF-8-sig')
                for file in corpus.glob('newlines_*.srt')]
    assert newlines[1:] == newlines[:-1]


def test_read_ass():
    corpus = Path(__file__).parent/'corpus'
    file = corpus/'reference.ass'
    subtitles = readers.read_ass(file, 'UTF-8-sig')
    assert subtitles.source == {'file': file, 'encoding': 'UTF-8-sig'}
    previous = None
    for subtitle in subtitles:
        assert subtitle.previous == previous
        if previous:
            assert previous.next == subtitle
        previous = subtitle
    assert not subtitles[-1].next
    assert subtitles == fixtures.reference()


def test_read_ssa():
    corpus = Path(__file__).parent/'corpus'
    file = corpus/'reference.ssa'
    subtitles = readers.read_ssa(file, 'UTF-8-sig')
    assert subtitles.source == {'file': file, 'encoding': 'UTF-8-sig'}
    previous = None
    for subtitle in subtitles:
        assert subtitle.previous == previous
        if previous:
            assert previous.next == subtitle
        previous = subtitle
    assert not subtitles[-1].next
    assert subtitles == fixtures.reference()


def test_read_vtt():
    corpus = Path(__file__).parent/'corpus'
    file = corpus/'reference.vtt'
    subtitles = readers.read_vtt(file, 'UTF-8-sig')
    assert subtitles.source == {'file': file, 'encoding': 'UTF-8-sig'}
    previous = None
    for subtitle in subtitles:
        assert subtitle.previous == previous
        if previous:
            assert previous.next == subtitle
        previous = subtitle
    assert not subtitles[-1].next
    assert subtitles == fixtures.reference()


def test_read_sub():
    corpus = Path(__file__).parent/'corpus'
    file = corpus/'reference.sub'
    subtitles = readers.read_sub(file, 'UTF-8-sig')
    assert subtitles.source == {'file': file, 'encoding': 'UTF-8-sig'}
    previous = None
    for subtitle in subtitles:
        assert subtitle.previous == previous
        if previous:
            assert previous.next == subtitle
        previous = subtitle
    assert not subtitles[-1].next
    assert subtitles == fixtures.reference()


def test_load():
    corpus = Path(__file__).parent/'corpus'
    file = corpus/'reference.srt'
    subtitles = readers.load(file)
    assert subtitles.source == {'file': file, 'encoding': 'UTF-8-sig'}
    assert subtitles == fixtures.reference()
    with pytest.raises(ValueError):
        readers.load(file.with_suffix('.invalid'))
    with pytest.raises(ValueError):
        readers.load(file, format='invalid')


def test_read():
    assert readers.read is readers.load
