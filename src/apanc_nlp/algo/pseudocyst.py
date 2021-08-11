"""
Pseudocyst: very specific to AP
"""

from runrex.algo.pattern import Pattern
from runrex.algo.result import Status
from runrex.terms import negation
from runrex.text import Document


class PseudocystStatus(Status):
    NONE = -1
    POSITIVE = 1
    PANCREATIC = 2


pseudocyst = '(pseudo ?cysts?)'

PSEUDOCYST = Pattern(
    rf'('
    rf'{pseudocyst}'
    rf')',
    negates=[negation]
)

PANCREATIC_PSEUDOCYST = Pattern(
    rf'('
    rf'pancreatic {pseudocyst}'
    rf'|{pseudocyst} (\w+ ){{0,3}}pancreas'
    rf')',
    negates=[negation]
)


def has_pseudocyst(document: Document):
    for sentence in document:
        found = False
        for text, start, end in sentence.get_patterns(PANCREATIC_PSEUDOCYST):
            found = True
            yield PseudocystStatus.PANCREATIC, text, start, end
        if not found:
            for text, start, end in sentence.get_patterns(PSEUDOCYST):
                yield PseudocystStatus.POSITIVE, text, start, end
