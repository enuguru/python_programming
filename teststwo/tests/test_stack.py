# python -m pytest -v --cov

from ds.stack import Stack
import pytest


def test_constructor():
    s = Stack()

    assert 1 == 1
    assert isinstance(s, Stack)
    assert len(s) == 0

