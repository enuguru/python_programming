# parms/test_parms.py

import pytest
from palindrome import is_palindrome

@pytest.mark.parametrize("palindrome", [
    "", 
    "a", 
    "Bob", 
    "Never odd or even", 
])
def test_palindrome(palindrome):
    assert is_palindrome(palindrome)


@pytest.mark.parametrize("palindrome", [
    "abc", 
    "abab", 
])
def test_not_palindrome(palindrome):
    assert not is_palindrome(palindrome)
