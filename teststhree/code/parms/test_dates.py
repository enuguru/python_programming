# parms/test_dates.py
import pytest
from datetime import datetime, timedelta

data = [
    (datetime(2012, 12, 21), datetime(2012, 12, 20), timedelta(1)), 
    (datetime(2012, 12, 20), datetime(2012, 12, 21), timedelta(1)), 
]

@pytest.mark.parametrize("a,b,expected", data)
def test_delta(a, b, expected):
    diff = a - b
    assert diff == expected
