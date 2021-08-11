"""
Necrosis and pancreatis necrosis.
"""

from runrex.algo.pattern import Pattern
from runrex.algo.result import Status
from runrex.terms import negation
from runrex.text import Document


class NecrosisStatus(Status):
    NONE = -1
    POSITIVE = 1
    PANCREATITIS = 2
    PERIPANCREATIC = 4
    ACUTE_COLLECTION = 5


necrosis = '(necros[ie]s|necrotic|necroti[zs]ing' \
           '|tissue death|tissue devitalization)'

NECROSIS = Pattern(
    rf'('
    rf'{necrosis}'
    rf')',
    negates=[negation]
)

PANCREATITIS_NECROSIS = Pattern(
    rf'\b('
    rf'{necrosis} (\w+ ){{0,3}}pancrea\w+'
    rf'pancrea\w+ {necrosis}'
    rf')\b',
    negates=[negation]
)

PERIPANCREATIC_NECROSIS = Pattern(
    rf'('
    rf'peri ?pancreatic {necrosis}'
    rf')',
    negates=[negation]
)

ACUTE_NECROTIC_COLLECTION = Pattern(
    rf'('
    rf'acute {necrosis} collection|\banc\b'
    rf')',
    negates=[negation]
)

WALLED_OFF_NECROSIS = Pattern(
    rf'('
    rf'walled ?off {necrosis}|\bwon\w'
    rf')',
    negates=[negation]
)


def has_necrosis(document: Document):
    for sentence in document:
        found = False
        for text, start, end in sentence.get_patterns(PANCREATITIS_NECROSIS):
            found = True
            yield NecrosisStatus.PANCREATITIS, text, start, end
        for text, start, end in sentence.get_patterns(PERIPANCREATIC_NECROSIS):
            found = True
            yield NecrosisStatus.PERIPANCREATIC, text, start, end
        for text, start, end in sentence.get_patterns(ACUTE_NECROTIC_COLLECTION):
            found = True
            yield NecrosisStatus.ACUTE_COLLECTION, text, start, end
        if not found:
            for text, start, end in sentence.get_patterns(NECROSIS):
                yield NecrosisStatus.POSITIVE, text, start, end
