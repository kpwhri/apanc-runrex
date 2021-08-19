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
    PEPTIC_ULCER = 11
    GASTRODUODENITIS = 12
    GERD = 13
    INTESTINAL_OBSTRUCTION = 14
    ILEUS = 15
    CONSTIPATION = 16
    MESENTERIC_ISCHEMIA = 17
    DIVERTICULOSIS = 18
    APPENDICITIS = 19
    HEPATITIS = 20
    INFLUENZA = 21
    FOOD_POISONING = 22
    ASCITES = 23
    NEPHROLITHIASIS = 24
    DKA = 25
    MYOCARDIAL_ISCHEMIA = 26
    BILIARY_CANCER = 27
    IBD = 28
    INFECTIOUS_GE = 29
    ESOPHAGITIS = 30


disorder = '(disease|disorder)'
gallbladder = '(biliary|gall bladder)'

ACUTE_APPENDICITIS = Pattern(
    rf'('
    rf'acute (inflamed )?appendicitis'
    rf')',
    negates=[negation]
)

APPENDICITIS = Pattern(
    rf'('
    rf'appendicitis'
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
    rf'|ch?olec[yi]sti\w+'  # cholecystitis
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

PEPTIC_ULCER = Pattern(
    rf'('
    rf'(peptic|gastroduodenal) ulcer'
    rf'|ulcer (of|in) (the )?gastrointest\w+'
    rf')',
    negates=[negation]
)

GASTRODUODENITIS = Pattern(
    rf'('
    rf'gastroduodenitis'
    rf'|gastritis (\w+ ){{0,3}}duodenitis'
    rf')'
)

GERD = Pattern(
    rf'('
    rf'\bgerd\b'
    rf'|gastro esophag\w+ reflux'
    rf'|gastric acid reflux'
    rf')'
)

INTESTINAL_OBSTRUCTION = Pattern(
    rf'('
    rf'(colon|intestin\w+|bowel) (occlu[sd]|obstruc|block)\w+'
    rf'|(occlusion|obstruction|blockage) of (the )?(intestine|bowel|colon)'
    rf')'
)

ILEUS = Pattern(
    rf'('
    rf'\bileus\b'
    rf'|gastro intestinal atony'
    rf')'
)

CONSTIPATION = Pattern(
    rf'('
    rf'constipat\w+'
    rf'|difficulty? (passing|def[ae]cat\w+)'
    rf'|fa?ecal retention'
    rf')'
)

MESENTERIC_ISCHEMIA = Pattern(
    rf'('
    rf'mesenteric (vascular )?(ischa?emia|insufficien\w+|angina)'
    rf')'
)

DIVERTICULOSIS = Pattern(
    rf'('
    rf'diverticulos\w+'
    rf'|diverticu\w+ (of )?intestin\w+'
    rf'|diverticul\w+ (disease|disorder)'
    rf'|enteric diverticul\w+'
    rf')'
)

HEPATITIS = Pattern(
    rf'('
    rf'hepatit\w+'
    rf'|liver inflamm?at\w+'
    rf'|inflamm?at\w+ ((disease|disorder) )?(of )?(the )?liver'
    rf')'
)

INFLUENZA = Pattern(
    rf'('
    rf'influenza|\bflu\b|\bgrip?pe\b'
    rf')'
)

FOOD_POISONING = Pattern(
    rf'('
    rf'food (poison\w*|intoxic\w+)'
    rf'|food borne? (illness|poisoning)'
    rf')'
)

ASCITES = Pattern(
    rf'('
    rf'\bascites?\b|hydro(ps)? (peritone|abdomin)\w+'
    rf')'
)

NEPHROLITHIASIS = Pattern(
    rf'('
    rf'nephrolith\w+|renal calcul\w+|(renal|kidney) (stone|lithias\w+|calcul\w+)'
    rf'|calculus of (the )?kidney'
    rf')'
)

DKA = Pattern(
    rf'('
    rf'diabetic (keto[sa]|acid)\w+'
    rf'|keto[sa]\w+ in diabetes'
    rf'|diabetes mellitus with keto[ta]\w+'
    rf'|\bdka\b'
    rf')'
)

MYOCARDIAL_ISCHEMIA = Pattern(
    rf'('
    rf'(myocardial|cardiac) ischa?emias?'
    rf'|ischa?emic heart disease'
    rf'|\bihd\b'
    rf')'
)

BILIARY_CANCER = Pattern(
    rf'('
    rf'(bill?iary( tract)?|gall bladder) (cancer|malignant|tumou?r|neoplasm)'
    rf'|(cancer|malignancy|tumou?r|neoplasm) of (the )?(bill?iary|gall bladder)'
    rf')'
)

IBD = Pattern(
    rf'('
    rf'(irrit\w+|inflam\w+|auto immune) bowel'
    rf'|\bibd\b'
    rf'|chronic enter\w+'
    rf')'
)

INFECTIOUS_GE = Pattern(
    rf'('
    rf'infecti?ous (gastro enteritis|colitis)'
    rf')'
)

ESOPHAGITIS = Pattern(
    rf'('
    rf'o?esophagit\w+'
    rf'|inflam\w+ of (the )?o?esophagus'
    rf')'
)


def has_competing_dx(document: Document):
    for sentence in document:
        for pat, res in [
            (ACUTE_APPENDICITIS, CompetingDx.ACUTE_APPENDICITIS),
            (APPENDICITIS, CompetingDx.APPENDICITIS),
            (GALL_BLADDER_DISEASE, CompetingDx.GALL_BLADDER_DISEASE),
            (BOWEL_MOVEMENTS, CompetingDx.BOWEL_MOVEMENTS),
            (CHRONIC_PAIN, CompetingDx.CHRONIC_PAIN),
            (STROKE, CompetingDx.STROKE),
            (COLANGITIS, CompetingDx.COLANGITIS),
            (BLOOD_IN_VOMIT, CompetingDx.BLOOD_IN_VOMIT),
            (BLOOD_IN_STOOL, CompetingDx.BLOOD_IN_STOOL),
            (PEPTIC_ULCER, CompetingDx.PEPTIC_ULCER),
            (GASTRODUODENITIS, CompetingDx.GASTRODUODENITIS),
            (GERD, CompetingDx.GERD),
            (INTESTINAL_OBSTRUCTION, CompetingDx.INTESTINAL_OBSTRUCTION),
            (ILEUS, CompetingDx.ILEUS),
            (CONSTIPATION, CompetingDx.CONSTIPATION),
            (MESENTERIC_ISCHEMIA, CompetingDx.MESENTERIC_ISCHEMIA),
            (DIVERTICULOSIS, CompetingDx.DIVERTICULOSIS),
            (HEPATITIS, CompetingDx.HEPATITIS),
            (INFLUENZA, CompetingDx.INFLUENZA),
            (FOOD_POISONING, CompetingDx.FOOD_POISONING),
            (ASCITES, CompetingDx.ASCITES),
            (NEPHROLITHIASIS, CompetingDx.NEPHROLITHIASIS),
            (DKA, CompetingDx.DKA),
            (MYOCARDIAL_ISCHEMIA, CompetingDx.MYOCARDIAL_ISCHEMIA),
            (BILIARY_CANCER, CompetingDx.BILIARY_CANCER),
            (IBD, CompetingDx.IBD),
            (INFECTIOUS_GE, CompetingDx.INFECTIOUS_GE),
            (ESOPHAGITIS, CompetingDx.ESOPHAGITIS),
        ]:
            for text, start, end in sentence.get_patterns(pat):
                yield res, text, start, end
