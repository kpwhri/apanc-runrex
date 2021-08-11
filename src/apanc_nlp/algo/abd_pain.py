"""
Abdominal pain.
"""

from runrex.algo.pattern import Pattern
from runrex.algo.result import Status, Result
from runrex.text import Document


class AbdPain(Status):
    NONE = -1
    PAIN = 1
    RADIATING_TO_BACK = 2
    ACUTE = 3
    EPIGASTRIC = 4
    CHEST = 5


PAIN = Pattern(
    rf'pain'
)

ABD_PAIN = Pattern(
    rf'('
    rf'(abd?(ominal)?|luq|llq|rlq|ruq|flank|uq|lq|quadrant) pain'
    rf'|pain site abd(omen)?'
    rf'|pain in (the )?abd(omen)?'
    rf')'
)

EPIGASTRIC_PAIN = Pattern(
    rf'('
    rf'epigastr\w+ pain|pain site epigrast\w+|pain in (the )?epigast\w+'
    rf')'
)

CHEST_PAIN = Pattern(
    rf'('
    rf'chest pain|pain site chest|pain in (the )?chest'
    rf')'
)

RADIATING_TO_BACK = Pattern(
    rf'('
    rf'radiating to back'
    rf')'
)

SEVERITY = Pattern(
    rf'('
    rf'sudden onset|severe|burning|intense|stabbing'
    rf')'
)


def has_abdominal_pain(document: Document):
    for sentence in document.select_sentences_with_patterns(PAIN):
        for text, start, end in sentence.get_patterns(ABD_PAIN):
            yield AbdPain.PAIN, text, start, end
        for text, start, end in sentence.get_patterns(EPIGASTRIC_PAIN):
            yield AbdPain.EPIGASTRIC, text, start, end
        for text, start, end in sentence.get_patterns(CHEST_PAIN):
            yield AbdPain.CHEST, text, start, end
        for text, start, end in sentence.get_patterns(RADIATING_TO_BACK):
            yield AbdPain.RADIATING_TO_BACK, text, start, end
        for text, start, end in sentence.get_patterns(SEVERITY):
            yield AbdPain.ACUTE, text, start, end
