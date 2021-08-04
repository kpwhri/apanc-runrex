import re
from typing import Tuple

from runrex.main import process
from runrex.schema import validate_config


def main(config_file):
    conf = validate_config(config_file)
    algorithms = {
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
