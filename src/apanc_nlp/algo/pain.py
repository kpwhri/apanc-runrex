"""
Abdominal pain.
"""
import re

from loguru import logger

from runrex.algo.pattern import Pattern
from runrex.algo.result import Status
from runrex.terms import negation
from runrex.text import Document

from apanc_nlp.algo.common import chronic


class AbdPain(Status):
    NONE = -1
    ABD_PAIN = 1
    RADIATING_TO_BACK = 2
    ACUTE = 3
    EPIGASTRIC = 4
    CHEST = 5
    CHRONIC = 6
    RECENT = 7
    VERY_RECENT = 8
    LONG_AGO = 9
    SUDDEN_ONSET = 10
    WORSENING = 11
    UNKNOWN_DURATION = 12


PAIN = Pattern(
    rf'pain',
    negates=[negation]
)

CHRONIC = Pattern(
    rf'{chronic} ((abd?(ominal)?|luq|llq|rlq|ruq|flank|uq|lq|quadrant) )?pain',
    negates=[negation]
)

ABD_PAIN = Pattern(
    rf'('
    rf'(abd?(ominal)?|luq|llq|rlq|ruq|flank|uq|lq|quadrant) pain'
    rf'|pain site abd(omen)?'
    rf'|pain in (the )?abd(omen)?'
    rf')',
    negates=[negation]
)

EPIGASTRIC_PAIN = Pattern(
    rf'('
    rf'epigastr\w+ pain|pain site epigrast\w+|pain in (the )?epigast\w+'
    rf')',
    negates=[negation]
)

CHEST_PAIN = Pattern(
    rf'('
    rf'chest pain|pain site chest|pain in (the )?chest'
    rf')',
    negates=[negation]
)

RADIATING_TO_BACK = Pattern(
    rf'('
    rf'radiat\w+ ((in)?to|toward)( the)? back'
    rf'|radiat\w+ back'
    rf')',
    negates=[negation]
)

SEVERITY = Pattern(
    rf'('
    rf'severe|burning|intense|stabbing'
    rf')',
    negates=[negation]
)

SUDDEN_ONSET = Pattern(
    rf'(sudden onset'
    rf'|onset ((late|early) )?(this|yesterday|last) (morning|evening|afternoon)'
    rf')'
)

DURATION = Pattern(
    rf'(?P<val>\d+ (day|wk|week|d|month|mon|m|year|yr))s?\b',
    negates=[r'\bht\b', r'every\b'],
)

WORSENING = Pattern(
    rf'worsening|increasing|(getting|gotten) worse'
)

duration_pat = re.compile(r'(?P<num>\d+)\W*(?P<unit>day|wk|week|d|month|mon|m)s?\b',
                          re.I)


def is_close_to_pain(text, start, end, window):
    return bool(PAIN.matches(text[max(0, start - window): end + window]))


def extract_duration(text):
    m = duration_pat.match(text)
    if m is None:  # error handling
        logger.error(f'Duration Pattern failed to match "{text}".')
        return AbdPain.UNKNOWN_DURATION
    num = m.group('num')
    unit = m.group('unit').lower()
    if unit in {'day', 'd'}:
        return AbdPain.VERY_RECENT
    elif unit in {'week', 'w', 'wk'}:
        return AbdPain.RECENT
    elif unit in {'month', 'm', 'mon'}:
        return AbdPain.LONG_AGO
    elif unit in {'year', 'yr'}:
        return AbdPain.LONG_AGO


def has_abdominal_pain(document: Document, window=30):
    for sentence in document.select_sentences_with_patterns(PAIN):
        for text, start, end in sentence.get_patterns(CHRONIC):
            yield AbdPain.CHRONIC, text, start, end
        for text, start, end in sentence.get_patterns(ABD_PAIN):
            yield AbdPain.ABD_PAIN, text, start, end
        for text, start, end in sentence.get_patterns(EPIGASTRIC_PAIN):
            yield AbdPain.EPIGASTRIC, text, start, end
        for text, start, end in sentence.get_patterns(CHEST_PAIN):
            yield AbdPain.CHEST, text, start, end
        for text, start, end in sentence.get_patterns(RADIATING_TO_BACK):
            yield AbdPain.RADIATING_TO_BACK, text, start, end
        for text, start, end in sentence.get_patterns(SEVERITY):
            if is_close_to_pain(sentence.text, start, end, window=window):
                yield AbdPain.ACUTE, text, start, end
        for text, start, end in sentence.get_patterns(SUDDEN_ONSET):
            if is_close_to_pain(sentence.text, start, end, window=window):
                yield AbdPain.SUDDEN_ONSET, text, start, end
        for text, start, end in sentence.get_patterns(DURATION, index='val'):
            if is_close_to_pain(sentence.text, start, end, window=window):
                yield extract_duration(text), text, start, end
        for text, start, end in sentence.get_patterns(WORSENING):
            if is_close_to_pain(sentence.text, start, end, window=window):
                yield AbdPain.WORSENING, text, start, end
