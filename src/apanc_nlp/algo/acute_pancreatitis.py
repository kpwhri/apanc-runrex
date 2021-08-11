"""
Identify general mentions of acute pancreatitis.
"""

from runrex.algo.pattern import Pattern
from runrex.algo.result import Status, Result
from runrex.text import Document

negation = r'((does|wo|has)n t\b|refuses?|\bnot\b|den(y|ies)|\bnor\b|neither)'
instructions = r'(instruct(ions?|ed)?|do not|discussed)'
hypothetical = r'(should|ought|\bif\b|please|\bmay\b|shall|\bcall\b)'


class AcutePancreatitisStatus(Status):
    NONE = -1
    POSITIVE = 1


epinephrine = rf'(acute pancreatitis)'

ACUTE_PANCREATITIS = Pattern(  # only in sentences with epi mention
    rf'('
    rf'acute pancreatitis'
    rf')',
)


def has_acute_pancreatitis(document: Document):
    for sentence in document:
        for text, start, end in sentence.get_patterns(ACUTE_PANCREATITIS):
            yield AcutePancreatitisStatus.POSITIVE, text, start, end
