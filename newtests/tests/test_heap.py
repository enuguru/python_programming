
# python -m pytest -v --cov

from ds.stack import Stack
import pytest

@pytest.fixture
def stack():
    return Stack()


def test_constructor():
    s = Stack()

    assert 1 == 1
    assert isinstance(s, Stack)
    assert len(s) == 0


def test_push(stack):
    stack.push(11)
    assert len(stack) == 1
    stack.push(20)
    assert len(stack) == 2
    #stack.push(33)
    #assert len(stack) == 3


def test_pop(stack):
    stack.push("beautifulpython")
    stack.push("performancepython")
    assert stack.pop() == "performancepython"
    assert stack.pop() == "beautifulpython"
    assert stack.pop() == None


