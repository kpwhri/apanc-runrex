import re
from typing import Tuple

from runrex.main import process
from runrex.schema import validate_config

from apanc_nlp.algo.abd_pain import has_abdominal_pain
from apanc_nlp.algo.acute_pancreatitis import has_pancreatitis
from apanc_nlp.algo.competing_dx import has_competing_dx
from apanc_nlp.algo.fluid import has_fluid
from apanc_nlp.algo.nausea import has_nausea
from apanc_nlp.algo.necrosis import has_necrosis
from apanc_nlp.algo.pseudocyst import has_pseudocyst
from apanc_nlp.utils import algo_to_result


def main(config_file):
    conf = validate_config(config_file)
    algorithms = {
        'acute_pancreatitis': lambda d, e: algo_to_result(has_pancreatitis, d, e),
        'abdominal_pain': lambda d, e: algo_to_result(has_abdominal_pain, d, e),
        'competing_dx': lambda d, e: algo_to_result(has_competing_dx, d, e),
        'nausea': lambda d, e: algo_to_result(has_nausea, d, e),
        'fluid': lambda d, e: algo_to_result(has_fluid, d, e),
        'necrosis': lambda d, e: algo_to_result(has_necrosis, d, e),
        'pseudocyst': lambda d, e: algo_to_result(has_pseudocyst, d, e),
    }
    process(**conf, algorithms=algorithms, ssplit=ssplit)


def subsplit(sentence: str, start: int, pattern) -> Tuple[str, int, int]:
    curr_start = 0
    for sm in pattern.finditer(sentence):
        yield sentence[curr_start: sm.start()], start + curr_start, start + sm.start()
        curr_start = sm.start()
    yield sentence[curr_start:], start + curr_start, start + len(sentence)


def ssplit(text: str) -> Tuple[str, int, int]:
    text = ' '.join(text.split('\n'))  # join broken lines
    sub_pat = re.compile(r'[*•-]')
    start = 0
    for m in re.finditer(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!|\*)\s', text):
        yield from subsplit(text[start: m.start()], start, sub_pat)
        start = m.start()
    yield from subsplit(text[start:], start, sub_pat)


if __name__ == '__main__':
    import sys

    try:
        main(sys.argv[1])
    except IndexError:
        raise AttributeError('Missing configuration file: Usage: run.py file.(json|yaml|py)')
