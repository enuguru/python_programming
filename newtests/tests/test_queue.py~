
# python -m pytest -v --cov

from ds.queue import Queue
import pytest

@pytest.fixture
def queue():
    return Queue()


def test_constructor():
    s = Queue()

    assert 1 == 1
    assert isinstance(s, Queue)
    assert len(s) == 0


def test_enqueue(queue):
    queue.enqueue(11)
    assert len(queue) == 1
    queue.enqueue(20)
    assert len(queue) == 2
    queue.enqueue(33)
    assert len(queue) == 3


def test_dequeue(queue):
    queue.enqueue("beautifulpython")
    queue.enqueue("performancepython")
    assert queue.dequeue() == "beautifulpython"
    assert queue.dequeue() == "performancepython"
    assert queue.dequeue() == None
