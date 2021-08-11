"""
Competing diagnoses
"""

from runrex.algo.pattern import Pattern
from runrex.algo.result import Status
from runrex.terms import negation
from runrex.text import Document

from apanc_nlp.algo.common import chronic


class CompetingDx(Status):
    NONE = -1
    ACUTE_APPENDICITIS = 1
    GALL_BLADDER_DISEASE = 2
    BOWEL_MOVEMENTS = 3
    COLANGITIS = 4
    CHRONIC_PAIN = 6
    STROKE = 8
    BLOOD_IN_STOOL = 9
    BLOOD_IN_VOMIT = 10


disorder = '(disease|disorder)'
gallbladder = '(biliary|gall bladder)'

ACUTE_APPENDICITIS = Pattern(
    rf'('
    rf'acute (inflamed )?appendicitis'
    rf')',
    negates=[negation]
)

GALL_BLADDER_DISEASE = Pattern(
    rf'('
    rf'{gallbladder} {disorder}'
    rf'|{disorder}( \w+){{0,3}} {gallbladder}'
    rf')',
    negates=[negation]
)

BOWEL_MOVEMENTS = Pattern(
    rf'('
    rf'bowel (movement|action|function|habit)s'
    rf'|defa?ecation'
    rf'|stool passing'
    rf'|passing stool'
    rf')',
    negates=[negation]
)

COLANGITIS = Pattern(
    rf'('
    rf'ch?olang[io]t\w+'
    rf'ch?olec[yi]sti\w+'
    rf'|(inflam|infect|swell)\w+( \w+){{0,3}} bile duct'
    rf'|bile duct (swell|inflam|infect)\w+'
    rf')',
    negates=[negation]
)

CHRONIC_PAIN = Pattern(
    rf'('
    rf'{chronic} pain'
    rf')',
    negates=[negation]
)

STROKE = Pattern(
    rf'('
    rf'stroke|apoplexy|\bcvas?\b'
    rf'|(cerebr\w+ ?)?vascular (accident|event)'
    rf'|brain attack'
    rf')',
    negates=[negation]
)

BLOOD_IN_STOOL = Pattern(
    rf'('
    rf'blood in (stool|fa?eces)'
    rf'|bloody stools?'
    rf'|(stools?|fa?eces)( \w+){{0,3}} (bloody?)'
    rf'|ha?ematochezia'
    rf')',
    negates=[negation]
)

BLOOD_IN_VOMIT = Pattern(
    rf'('
    rf'blood in (vomit|throw up)'
    rf'|bloody (vomit|throw up)'
    rf'|ha?ematemesis'
    rf'|(vomit\w*|throw\w* up)( \w+){{0,3}} (bloody?)'
    rf')',
    negates=[negation]
)


def has_competing_dx(document: Document):
    for sentence in document:
        for text, start, end in sentence.get_patterns(ACUTE_APPENDICITIS):
            yield CompetingDx.ACUTE_APPENDICITIS, text, start, end
        for text, start, end in sentence.get_patterns(GALL_BLADDER_DISEASE):
            yield CompetingDx.GALL_BLADDER_DISEASE, text, start, end
        for text, start, end in sentence.get_patterns(BOWEL_MOVEMENTS):
            yield CompetingDx.BOWEL_MOVEMENTS, text, start, end
        for text, start, end in sentence.get_patterns(CHRONIC_PAIN):
            yield CompetingDx.CHRONIC_PAIN, text, start, end
        for text, start, end in sentence.get_patterns(STROKE):
            yield CompetingDx.STROKE, text, start, end
        for text, start, end in sentence.get_patterns(BLOOD_IN_STOOL):
            yield CompetingDx.BLOOD_IN_STOOL, text, start, end
        for text, start, end in sentence.get_patterns(BLOOD_IN_VOMIT):
            yield CompetingDx.BLOOD_IN_VOMIT, text, start, end
