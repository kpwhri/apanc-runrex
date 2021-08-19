import pytest

from apanc_nlp.algo import competing_dx as cdx


@pytest.mark.parametrize('text, matches', [
    ('Gastritis and duodenitis', True),
    ('Gastritis', False),
])
def test_gastroduodenitis(text, matches):
    assert bool(cdx.GASTRODUODENITIS.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('gastroesophageal reflux', True),
    ('gerd', True),
    ('gerdo', False),
])
def test_gerd(text, matches):
    assert bool(cdx.GERD.matches(text)) == matches
