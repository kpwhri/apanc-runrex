"""
Utilities that should be added to runrex.
"""
from runrex.algo.result import Result
from runrex.text import Document


def algo_to_result(func, document: Document, expected=None):
    for status, text, start, end in func(document):
        yield Result(status, status.value, expected=expected,
                     text=text, start=start, end=end)
