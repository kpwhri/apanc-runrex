import pytest
from runrex.text import Document

from apanc_nlp.algo.acute_pancreatitis import CONSISTENT_WITH, PancreatitisStatus, has_pancreatitis


@pytest.mark.parametrize('text, exp', [
    ('consistent with acute pancreatitis', True),
    ('seen to be acute pancreatitis', True),
    ('probably pancreatitis', True),
    ('not consistent with acute pancreatitis', False),
    ('likely not acute pancreatitis', False),
])
def test_consistent_with_pattern(text, exp):
    m = CONSISTENT_WITH.matches(text)
    assert bool(m) is exp


@pytest.mark.parametrize('text, flags', [
    ('consistent with acute pancreatitis',
     {PancreatitisStatus.CONSISTENT_WITH, PancreatitisStatus.ACUTE}),
    ('seen to be acute pancreatitis',
     {PancreatitisStatus.CONSISTENT_WITH, PancreatitisStatus.ACUTE}),
    ('probably pancreatitis',
     {PancreatitisStatus.CONSISTENT_WITH}),
    ('pancreatitis',
     {PancreatitisStatus.POSITIVE}),
])
def test_has_pancreatitis(text, flags):
    doc = Document(name=None, text=text)
    results = set(x[0] for x in has_pancreatitis(doc))  # get flags/enums only
    assert results == flags
