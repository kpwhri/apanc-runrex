"""
Identify general mentions of acute pancreatitis.
"""

from runrex.algo.pattern import Pattern
from runrex.algo.result import Status
from runrex.text import Document

from apanc_nlp.algo.common import chronic


class PancreatitisStatus(Status):
    NONE = -1
    POSITIVE = 1
    ACUTE = 2
    CHRONIC = 3
    INFLAMMATION = 4


PANCREATITIS = Pattern(
    rf'('
    rf'pancreatitis'
    rf')',
)

ACUTE_PANCREATITIS = Pattern(
    rf'('
    rf'acute pancreatitis'
    rf')',
)

INFLAMMATION_PANCREAS = Pattern(
    rf'('
    rf'inflam\w+ pancrea\w+'
    rf'|pancea\w+ (\w+ ){{0,3}}inflam\w+'
    rf')',
)

CHRONIC_PANCREATITIS = Pattern(
    rf'('
    rf'{chronic} pancreatitis'
    rf')',
)


def has_pancreatitis(document: Document):
    for sentence in document:
        found = False
        for text, start, end in sentence.get_patterns(ACUTE_PANCREATITIS):
            found = True
            yield PancreatitisStatus.ACUTE, text, start, end
        for text, start, end in sentence.get_patterns(CHRONIC_PANCREATITIS):
            found = True
            yield PancreatitisStatus.CHRONIC, text, start, end
        for text, start, end in sentence.get_patterns(INFLAMMATION_PANCREAS):
            found = True
            yield PancreatitisStatus.INFLAMMATION, text, start, end
        if not found:
            for text, start, end in sentence.get_patterns(PANCREATITIS):
                yield PancreatitisStatus.POSITIVE, text, start, end
