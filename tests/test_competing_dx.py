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


@pytest.mark.parametrize('text, matches', [
    ('hepatitis', True),
    ('inflamation of the liver', True),
])
def test_hepatitis(text, matches):
    assert bool(cdx.HEPATITIS.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('i have the flu', True),
    ('afluent', False),
])
def test_influenza(text, matches):
    assert bool(cdx.INFLUENZA.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('foodborne illness', True),
    ('food poisoning', True),
])
def test_food_poisoning(text, matches):
    assert bool(cdx.FOOD_POISONING.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('hydrops abdominis', True),
    ('hydroperitoneum', True),
])
def test_ascites(text, matches):
    assert bool(cdx.ASCITES.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('nephrolithiasis', True),
    ('renal calculi', True),
])
def test_nephrolithiasis(text, matches):
    assert bool(cdx.NEPHROLITHIASIS.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('dka', True),
    ('diabetic ketoacidosis', True),
])
def test_dka(text, matches):
    assert bool(cdx.DKA.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('myocardial ischemia', True),
    ('ihd', True),
    ('ischaemic heart disease', True),
])
def test_myocardial_ischemia(text, matches):
    assert bool(cdx.MYOCARDIAL_ISCHEMIA.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('biliary cancer', True),
    ('malignant tumour of biliary tract', True),
])
def test_biliary_cancer(text, matches):
    assert bool(cdx.BILIARY_CANCER.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('ibd', True),
    ('inflammatory bowel disease', True),
])
def test_ibd(text, matches):
    assert bool(cdx.IBD.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('infectious gastro-enteritis', True),
    ('infectous colitis', True),
])
def test_infectious_ge(text, matches):
    assert bool(cdx.INFECTIOUS_GE.matches(text)) == matches


@pytest.mark.parametrize('text, matches', [
    ('esophagitis', True),
    ('esophagitides', True),
])
def test_esophagitis(text, matches):
    assert bool(cdx.ESOPHAGITIS.matches(text)) == matches
