# marks/test_marks.py
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_smoke():
    pass

@pytest.mark.regression
def test_more():
    pass
