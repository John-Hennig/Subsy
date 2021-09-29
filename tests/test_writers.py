"""Tests the `writers` module."""

import parent # noqa F401
from subsy import writers
import fixtures
import pytest
from pathlib import Path


def test_write_srt():
    here = Path(__file__).parent
    file = here/'temp.srt'
    if file.exists():
        file.unlink()
    reference = fixtures.reference()
    writers.write_srt(reference, file, 'UTF-8-sig')
    assert file.is_file()
    content = (here/'corpus'/'reference.srt').read_text(encoding='UTF-8-sig')
    assert file.read_text(encoding='UTF-8-sig') == content
    file.unlink()


def test_write_ass():
    here = Path(__file__).parent
    file = here/'temp.ass'
    if file.exists():
        file.unlink()
    reference = fixtures.reference()
    writers.write_ass(reference, file, 'UTF-8-sig')
    assert file.is_file()
    content = (here/'corpus'/'reference.ass').read_text(encoding='UTF-8-sig')
    assert file.read_text(encoding='UTF-8-sig') == content
    file.unlink()


def test_write_ssa():
    here = Path(__file__).parent
    file = here/'temp.ssa'
    if file.exists():
        file.unlink()
    reference = fixtures.reference()
    writers.write_ssa(reference, file, 'UTF-8-sig')
    assert file.is_file()
    content = (here/'corpus'/'reference.ssa').read_text(encoding='UTF-8-sig')
    assert file.read_text(encoding='UTF-8-sig') == content
    file.unlink()


def test_write_vtt():
    here = Path(__file__).parent
    file = here/'temp.vtt'
    if file.exists():
        file.unlink()
    reference = fixtures.reference()
    writers.write_vtt(reference, file, 'UTF-8-sig')
    assert file.is_file()
    content = (here/'corpus'/'reference.vtt').read_text(encoding='UTF-8-sig')
    assert file.read_text(encoding='UTF-8-sig') == content
    file.unlink()


def test_write_sub():
    here = Path(__file__).parent
    file = here/'temp.sub'
    if file.exists():
        file.unlink()
    reference = fixtures.reference()
    writers.write_sub(reference, file, 'UTF-8-sig')
    assert file.is_file()
    content = (here/'corpus'/'reference.sub').read_text(encoding='UTF-8-sig')
    assert file.read_text(encoding='UTF-8-sig') == content
    file.unlink()


def test_save():
    here = Path(__file__).parent
    file = here/'temp.srt'
    if file.exists():
        file.unlink()
    reference = fixtures.reference()
    with pytest.raises(ValueError):
        writers.save(reference, file.with_suffix('.invalid'))
    with pytest.raises(ValueError):
        writers.save(reference, file, format='invalid')
    writers.save(reference, file)
    assert file.is_file()
    content = (here/'corpus'/'reference.srt').read_text(encoding='UTF-8-sig')
    assert file.read_text(encoding='UTF-8-sig') == content
    file.unlink()


def test_write():
    assert writers.write is writers.save
