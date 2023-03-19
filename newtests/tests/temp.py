
# python -m pytest -v --cov

from ds.stack import Stack

def test_constructor():
    s = Stack()

    assert 1 == 1
    assert isinstance(s, Stack)
    assert len(s) == 0


def test_push(stack):
    s = Stack()
    s.push(11)
    assert len(s) == 1
    s.push(20)
    assert len(s) == 2
    #s.push(33)
    #assert len(s) == 3


def test_pop(stack):
    s.push("beautifulpython")
    s.push("performancepython")
    assert s.pop() == "performancepython"
    assert s.pop() == "beautifulpython"
    assert s.pop() == None


