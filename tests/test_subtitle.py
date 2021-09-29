"""Tests the `subtitle` module."""

import parent # noqa F401
from subsy import Subtitle


def test_init():
    (lines, start, duration) = (['line1', 'line2'], 0, 1)
    subtitle = Subtitle(lines, start, duration)
    assert subtitle.lines    == lines
    assert subtitle.start    == start
    assert subtitle.duration == duration
    assert subtitle.parent   is None
    assert subtitle.index    is None
    assert subtitle.next     is None
    assert subtitle.previous is None


def test_iter():
    lines = ['line1', 'line2']
    subtitle = Subtitle(lines)
    for (item, line) in zip(subtitle, lines):
        assert item == line


def test_len():
    subtitle = Subtitle(['line'])
    assert len(subtitle) == 4
    subtitle = Subtitle(['line1', 'line2'])
    assert len(subtitle) == 11
    subtitle = Subtitle(['Line <i>with</i> markup.'])
    assert len(subtitle) == 17


def test_contains():
    subtitle = Subtitle(['line1', 'line2'])
    number = 1
    assert 'line1' in subtitle
    assert 'line2' in subtitle
    assert number not in subtitle


def test_eq():
    line = ['line']
    subtitle1 = Subtitle(line)
    lines = ['line1', 'line2']
    subtitle2 = Subtitle(lines)
    number = 1
    assert subtitle1 == subtitle1
    assert subtitle1 == line
    assert subtitle1 == 'line'
    assert subtitle1 != number
    assert subtitle2 == subtitle2
    assert subtitle2 == lines
    assert subtitle2 == 'line1\nline2'
    assert subtitle1 != subtitle2
    assert subtitle2 != number


def test_str():
    subtitle = Subtitle(['line1', 'line2'], 1000, 2000)
    assert str(subtitle) == 'line1|line2'


def test_repr():
    subtitle = Subtitle(['line1', 'line2'], 1000, 1234)
    assert repr(subtitle) == ('Subtitle(00:00:01.000 → 00:00:02.234: '
                              '"line1", "line2")')


def test_prev():
    subtitle1 = Subtitle(['line'])
    subtitle2 = Subtitle(['line1', 'line2'])
    subtitle2.previous = subtitle1
    assert subtitle2.prev is subtitle1
    subtitle2.prev = subtitle2
    assert subtitle2.prev is subtitle2


def test_end():
    subtitle = Subtitle(['line1', 'line2'], 0, 1234)
    assert subtitle.end == 1234
    assert subtitle.duration == 1234
    subtitle.end = 2000
    assert subtitle.end == 2000
    assert subtitle.duration == 2000


def test_start_time():
    subtitle = Subtitle(['line1', 'line2'], 0, 1234)
    assert subtitle.start_time == '00:00:00.000'
    assert subtitle.duration == 1234
    subtitle.start_time = '00:00:01.000'
    assert subtitle.start_time == '00:00:01.000'
    assert subtitle.duration == 1234


def test_end_time():
    subtitle = Subtitle(['line1', 'line2'], 0, 1234)
    assert subtitle.end_time == '00:00:01.234'
    assert subtitle.duration == 1234
    subtitle.end_time = '00:00:02.000'
    assert subtitle.end_time == '00:00:02.000'
    assert subtitle.duration == 2000


def test_text():
    subtitle = Subtitle(['line'])
    assert subtitle.text == 'line'
    assert len(subtitle.lines) == 1
    subtitle.text = 'other'
    assert subtitle.text == 'other'
    assert len(subtitle.lines) == 1
    subtitle.text = 'line1\nline2'
    assert subtitle.text == 'line1\nline2'
    assert len(subtitle.lines) == 2
    subtitle = Subtitle(['line1', 'line2'])
    assert subtitle.text == 'line1\nline2'
    assert len(subtitle.lines) == 2


def test_plain():
    subtitle = Subtitle()
    subtitle.text = 'Text with <b>bold</b> tag.'
    assert subtitle.plain == 'Text with bold tag.'
    subtitle.text = 'Text with <i>italics</i> tag.'
    assert subtitle.plain == 'Text with italics tag.'
    subtitle.text = 'Text with <u>underline</u> tag.'
    assert subtitle.plain == 'Text with underline tag.'
    subtitle.text = 'Text with <color=#RRGGBB>color</color> tag.'
    assert subtitle.plain == 'Text with color tag.'
    subtitle.text = 'Text with <font="DejaVu Sans">font</font> tag.'
    assert subtitle.plain == 'Text with font tag.'
    subtitle.text = 'Text with <size=24>size</size> tag.'
    assert subtitle.plain == 'Text with size tag.'
    subtitle.text = '<i>An entire line in italics.</i>'
    assert subtitle.plain == 'An entire line in italics.'
    subtitle.text = 'Only <i>part of</i> line in italics.'
    assert subtitle.plain == 'Only part of line in italics.'
    subtitle.text = '– <i>Italics behind dialog dash.</i>'
    assert subtitle.plain == '– Italics behind dialog dash.'
    subtitle.text = 'Only <i>one markup tag.'
    assert subtitle.plain == 'Only one markup tag.'
    subtitle.text = 'Two <i>opening<i> tags.'
    assert subtitle.plain == 'Two opening tags.'
