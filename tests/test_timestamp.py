"""Tests the `timestamp` module."""

from subsy import timestamp
import pytest


def test_format():
    assert timestamp.format(1234) == '00:00:01.234'
    assert timestamp.format(1234, format='SubRip') == '00:00:01,234'
    with pytest.raises(ValueError):
        timestamp.format(1000, format='invalid')


def test_parse():
    assert timestamp.parse('00:00:01.234') == 1234
    assert timestamp.parse('00:00:01,234', format='SubRip') == 1234
    with pytest.raises(ValueError):
        timestamp.parse('00:00:01,234', format='invalid')
