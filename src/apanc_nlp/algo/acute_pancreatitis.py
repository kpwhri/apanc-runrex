"""
Identify general mentions of acute pancreatitis.
"""

from runrex.algo.pattern import Pattern
from runrex.algo.result import Status
from runrex.terms import negation
from runrex.text import Document

from apanc_nlp.algo.common import chronic


class PancreatitisStatus(Status):
    NONE = -1
    POSITIVE = 1
    ACUTE = 2
    CHRONIC = 3
    INFLAMMATION = 4
    INTERSTITIAL = 5
    PERI_INFLAMMATION = 6


PANCREATITIS = Pattern(
    rf'('
    rf'pancreatitis'
    rf')',
    negates=[negation]
)

ACUTE_PANCREATITIS = Pattern(
    rf'('
    rf'acute pancreatitis'
    rf')',
    negates=[negation]
)

INFLAMMATION_PANCREAS = Pattern(
    rf'('
    rf'(inflam|swell|enlarg)\w+ (\w+ ){{0,3}}pancrea\w+'
    rf'|pancrea\w+ (\w+ ){{0,3}}(inflam|swell|enlarg)\w+'
    rf')',
    negates=[negation]
)

INFLAMMATION_PERIPANCREAS = Pattern(
    rf'('
    rf'(inflam|swell|enlarg)\w+ (\w+ ){{0,3}}peri pancrea\w+'
    rf'|peri pancrea\w+ (\w+ ){{0,3}}(inflam|swell|enlarg)\w+'
    rf')',
    negates=[negation]
)

CHRONIC_PANCREATITIS = Pattern(
    rf'('
    rf'{chronic} pancreatitis'
    rf')',
    negates=[negation]
)

INTERSTITIAL_PANCREATITIS = Pattern(
    rf'('
    rf'interstitial (o?edematous )?pancreatitis'
    rf')',
    negates=[negation]
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
        for text, start, end in sentence.get_patterns(INFLAMMATION_PERIPANCREAS):
            found = True
            yield PancreatitisStatus.PERI_INFLAMMATION, text, start, end
        for text, start, end in sentence.get_patterns(INTERSTITIAL_PANCREATITIS):
            found = True
            yield PancreatitisStatus.INTERSTITIAL, text, start, end
        if not found:
            for text, start, end in sentence.get_patterns(PANCREATITIS):
                yield PancreatitisStatus.POSITIVE, text, start, end
