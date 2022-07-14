
from ds.stack import Stack
import pytest

@pytest.fixture
def stack():
    return Stack()

def test_constructor():
    s = Stack()
    assert isinstance(s,Stack)
    assert len(s) == 0

def test_push(stack):
    stack.push(3)
    assert len(stack) == 1
    stack.push(5)
    assert len(stack) == 2
    
