# Tutorial

You can [download the subtitles file][reference] used in this tutorial
from the library's source-code repository (where it is part of the
automated test suite). If we start the Python interpreter in the same
folder as the downloaded file, it can be loaded like so:
```python
>>> import subsy
>>> subtitles = subsy.load('reference.srt')
```

The `load()` functions returns a `Subtitles` object. It is basically
a list of the individual subtitles:
```python
>>> len(subtitles)
46
>>> subtitle = subtitles[0]
>>> subtitle
Subtitle(00:00:00.000 → 00:00:01.234: "Just a single line of text.")
```

But it is a linked list. That is, it provides additional funtionality
to go from one subtitle to the next one, or back to the previous one.
```python
>>> subtitle = subtitle.next
>>> subtitle
Subtitle(00:00:02.000 → 00:00:02.900: "Text extending over", "two lines.")
>>> subtitle.previous
Subtitle(00:00:00.000 → 00:00:01.234: "Just a single line of text.")
```

This can be useful when cleaning up subtitles, for example to recognize
running sentences when correcting improper capitalization.

The individual subtitles do of course have time stamps. These can be
accessed, and also changed, in either milliseconds or in a text-based
format.

```python
>>> subtitle.start
2000
>>> subtitle.start_time
'00:00:02.000'
>>> subtitle.duration
900
>>> subtitle.end_time
'00:00:02.900'
>>> subtitle.end_time = 3000
>>> subtitle.duration
1000
>>> subtitle.start = 2500
>>> subtitle.duration
1000
>>> subtitle.end
3500
```

Note how when we set the end time, the duration changes accordingly.
But when we assign a new start time, the duration remains the same
and the end time shifts along.

Text can either be accessed as individual lines or as a `\n`-separated
string.
```python
>>> subtitle.lines
['Text extending over', 'two lines.']
>>> subtitle.text
'Text extending over\ntwo lines.'
```

Changing one also changes the other.
```python
>>> subtitle.text = subtitle.text.upper()
>>> subtitle.text
'TEXT EXTENDING OVER\nTWO LINES.'
>>> subtitle.lines
['TEXT EXTENDING OVER', 'TWO LINES.']
```

Text may contain markup, of the SubRip flavor familiar from `.srt` files.
```python
>>> subtitle = subtitles[16]
>>> subtitle.text
'<i>Two lines of text,</i>\n<i>separately in italics.</i>'
```

Sometimes we want the plain text without the markup.
```python
>>> subtitle.plain
'Two lines of text,\nseparately in italics.'
```

The character length of the plain text is also reported as the length
of the subtitle.
```python
>>> len(subtitle)
41
>>> len(subtitle.plain)
41
```

[reference]: https://github.com/John-Hennig/MPh/blob/main/tests/corpus/reference.srt
