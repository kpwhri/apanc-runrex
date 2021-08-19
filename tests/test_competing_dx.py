import pytest

from apanc_nlp.algo.competing_dx import GASTRODUODENITIS


@pytest.mark.parametrize('text, matches', [
    ('Gastritis and duodenitis', True),
    ('Gastritis', False),
])
def test_gastroduodenitis(text, matches):
    assert bool(GASTRODUODENITIS.matches(text)) == matches
