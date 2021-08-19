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


@pytest.mark.parametrize('text, matches', [
    ('intestinal obstruction', True),
    ('occlusion of the intestine', True),
])
def test_intestinal_obstruction(text, matches):
    assert bool(cdx.INTESTINAL_OBSTRUCTION.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('ileus', True),
    ('gastro-intestinal atony', True),
])
def test_ileus(text, matches):
    assert bool(cdx.ILEUS.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('constipated', True),
])
def test_constipation(text, matches):
    assert bool(cdx.CONSTIPATION.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('mesenteric ischaemia', True),
])
def test_mesentric_ischemia(text, matches):
    assert bool(cdx.MESENTERIC_ISCHEMIA.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('diverticuloses', True),
    ('enteric diverticulum', True),
])
def test_diverticulosis(text, matches):
    assert bool(cdx.DIVERTICULOSIS.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('appendicitis', True),
])
def test_appendicitis(text, matches):
    assert bool(cdx.APPENDICITIS.matches(text)) == matches
