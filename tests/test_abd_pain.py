import pytest
from runrex.text import Document

from apanc_nlp.algo.pain import AbdPain, extract_duration, RADIATING_TO_BACK, CHRONIC, CHEST_PAIN, DURATION, \
    is_close_to_pain, has_abdominal_pain


@pytest.mark.parametrize('exp, text', [
    (AbdPain.RECENT, '1 week'),
    (AbdPain.VERY_RECENT, '2 days'),
    (AbdPain.VERY_RECENT, '2 d'),
    (AbdPain.LONG_AGO, '2 mons'),
    (AbdPain.LONG_AGO, '2mons'),
    (AbdPain.LONG_AGO, '2.mons'),
    (AbdPain.RECENT, '2 WEEKS'),
    (AbdPain.RECENT, '1 Week'),
])
def test_extract_duration(exp, text):
    assert extract_duration(text) == exp


def test_radiate_to_back():
    assert RADIATING_TO_BACK.matches('radiates to back')


@pytest.mark.parametrize('text, exp', [
    ('chronic opioid use for pain', False),
    ('recurrent depression', False),
    ('chronic pain', True),
    ('chronic abd pain', True),
])
def test_chronic(text, exp):
    assert bool(CHRONIC.matches(text)) is exp


@pytest.mark.parametrize('text, exp', [
    ('negative for chest pain', False),
    ('chest pain', True),
])
def test_chest(text, exp):
    assert bool(CHEST_PAIN.matches(text)) is exp


@pytest.mark.parametrize('text, exp', [
    ('pain for 1 week', True),
    ('pain at night for 1 week', True),  # ensure 'ht' not picked up here
    ('pain blah blah blah ht. 1.78m', False),
])
def test_duration(text, exp):
    assert bool(DURATION.matches(text)) is exp


@pytest.mark.parametrize('text, start, end, window, exp', [
    ('pain for 1 week', 9, 15, 20, True),
    ('1 week of acute pain', 0, 6, 20, True),
    ('pain blah blah blah blah blah 1 week', 30, 36, 20, False),
    ('1 week of joy and happiness blah blah blah blah blah pain', 0, 6, 20, False),
])
def test_is_close_to_pain(text, start, end, window, exp):
    assert is_close_to_pain(text, start, end, window) == exp


@pytest.mark.parametrize('text, exp', [
    ('pain for 1 week', AbdPain.RECENT),
    ('1 week of acute pain', AbdPain.RECENT),
    ('pain blah blah blah blah blah 1 week', None),
    ('1 week of joy and happiness blah blah blah blah blah pain', None),
])
def test_has_abdominal_pain(text, exp):
    doc = Document('noname', text=text)
    lst = list(has_abdominal_pain(doc, window=20))
    if len(lst) == 0:
        assert exp is None
    else:
        result, text, start, end = lst[0]
        assert result == exp
