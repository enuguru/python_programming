# fixtures/test_fixture.py
import pytest

@pytest.fixture
def sequence():
    return [1, 2, 3]

def test_sum(sequence):
    assert sum(sequence) == 6

def test_max(sequence):
    assert max(sequence) == 3
