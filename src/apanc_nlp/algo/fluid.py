"""
Fluid collection
"""

from runrex.algo.pattern import Pattern
from runrex.algo.result import Status
from runrex.terms import negation
from runrex.text import Document


class FluidStatus(Status):
    NONE = -1
    APFC = 1
    PANCREATIC = 2
    WALLED_OFF = 3


APFC = Pattern(
    rf'('
    rf'acute peri pancreatic fluid|\bapfc\b'
    rf')',
    negates=[negation]
)

PANCREATIC = Pattern(
    rf'('
    rf'(peri )?pancreatic fluid'
    rf')',
    negates=[negation]
)

WALLED_COLLECTION = Pattern(
    rf'('
    rf'walled off fluid'
    rf')',
    negates=[negation]
)


def has_fluid(document: Document):
    for sentence in document:
        for text, start, end in sentence.get_patterns(APFC):
            yield FluidStatus.APFC, text, start, end
        for text, start, end in sentence.get_patterns(PANCREATIC):
            yield FluidStatus.PANCREATIC, text, start, end
        for text, start, end in sentence.get_patterns(WALLED_COLLECTION):
            yield FluidStatus.WALLED_OFF, text, start, end
