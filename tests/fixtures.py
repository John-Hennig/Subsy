"""Fixtures used throughout the test suite."""

from subsy import Subtitles
from subsy import Subtitle


reference_data = (
    (    0, 1234, 'Just a single line of text.'),
    ( 2000,  900, 'Text extending over|two lines.'),
    ( 3000,  900, 'Text extending|over|three lines.'),
    ( 4000,  900, 'Line does not end with a period'),
    ( 5000,  900, 'because the sentence continues.'),
    (10000,  900, '...line starting with dot-dot-dot.'),
    (11000,  900, '…line starting with ellipsis.'),
    (12000,  900, 'Line ending with dot-dot-dot...'),
    (13000,  900, 'Line ending with ellipsis…'),
    (14000,  900, 'Line ending with four dots....'),
    (15000,  900, 'Line ending with ellipsis and a dot.'),
    (16000,  900, 'Line that has: a colon.'),
    (17000,  900, 'Line ends with number 1'),
    (18000,  900, '1 number starts the line'),
    (20000,  900, '<i>Entire line in italics.</i>'),
    (21000,  900, 'Only <i>part of line</i> in italics.'),
    (22000,  900, '<i>Two lines of text,</i>|<i>separately in italics.</i>'),
    (23000,  900, '<i>Italics extending over|multiple lines.</i>'),
    (30000,  900, '- Dialog marked with minus sign.|- Different speaker.'),
    (31000,  900, '– Dialog marked with en-dash.|– Different speaker.'),
    (32000,  900, '— Dialog marked with em-dash.|— Different speaker.'),
    (33000,  900, '- <i>Dialog line in italics.</i>|- Or <i>part</i> of it.'),
    (34000,  900, '– <i>First line in italics.</i>|– Second not.'),
    (35000,  900, '— First line regular.|— <i>Second in italics.</i>'),
    (40000,  900, '♪ Song lyrics ♪'),
    (41000,  900, '♪ <i>Lyrics in italics</i> ♪'),
    (42000,  900, '♪ Lyrics <i>partly</i> in italics ♪'),
    (43000,  900, '♪ Lyrics on two ♪|♪ separate lines ♪'),
    (44000,  900, '♪ Lyrics extending over|two lines ♪'),
    (45000,  900, '♪ – Dialog with en-dash ♪|♪ – Second singer ♪'),
    (46000,  900, '♪ — Dialog with em-dash ♪|♪ — Second singer ♪'),
    (50000,  900, 'SPEAKER: Just a single line.'),
    (51000,  900, 'SPEAKER: Text extending|over two lines.'),
    (52000,  900, 'SPEAKER: But line has: a colon.'),
    (53000,  900, 'SPEAKER: But first line:|ends with a colon.'),
    (54000,  900, 'SPEAKER: <i>Text in italics.</i>'),
    (55000,  900, 'SPEAKER: <i>Two lines|in italics.</i>'),
    (56000,  900, 'SPEAKER: <i>Two lines</i>|<i>separately in italics.</i>'),
    (60000,  900, 'PAUL: Speaker 1 says.|MARY: Speaker 2 says.'),
    (61000,  900, 'PAUL: Is on-screen.|MARY: <i>Is off-screen.</i>'),
    (62000,  900, 'PAUL: Says something|MARY: Emphasizes <i>this</i> word.'),
    (63000,  900, 'PAUL & MARY: Two people speak.'),
    (64000,  900, 'PAUL & MARY:|Two people speak on new line.'),
    (65000,  900, 'SPEAKER: Says off-screen.|- On-screen person replies.'),
    (66000,  900, 'someone continues.|SPEAKER: New person says.'),
    (67000,  900, '- Person speaks on-screen.|SPEAKER: Replies off-screen.'),
)


def reference():
    return Subtitles([Subtitle(text.split('|'), start, duration)
                      for (start, duration, text) in reference_data])
