"""
Identify nausea-related conditions (symptom of acute pancreatitis)
"""

from runrex.algo.pattern import Pattern
from runrex.algo.result import Status
from runrex.terms import negation
from runrex.text import Document


class NauseaStatus(Status):
    NONE = -1
    VOMITING = 1
    NAUSEA = 2


VOMITING = Pattern(  # only in sentences with epi mention
    rf'('
    rf'vomit\w*'
    rf'|emesis'
    rf'|dry heav\w+'
    rf'|throw\w* up'
    rf')',
    negates=[negation]
)

NAUSEA = Pattern(
    rf'('
    rf'nause\w+|queasy|bilious'
    rf')',
    negates=[negation]
)


def has_nausea(document: Document):
    for sentence in document:
        for text, start, end in sentence.get_patterns(VOMITING):
            yield NauseaStatus.VOMITING, text, start, end
        for text, start, end in sentence.get_patterns(NAUSEA):
            yield NauseaStatus.NAUSEA, text, start, end
