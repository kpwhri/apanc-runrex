import pytest

from apanc_nlp.algo.abd_pain import AbdPain, extract_duration, RADIATING_TO_BACK


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
