# parms/test_palindrome.py

from palindrome import is_palindrome

def test_empty():
    assert is_palindrome("")

def test_single():
    assert is_palindrome("a")

def test_mixed_casing():
    assert is_palindrome("Bob")

def test_spaces():
    assert is_palindrome("Never odd or even")

def test_not_palindrome():
    assert not is_palindrome("abc")

def test_almost():
    assert not is_palindrome("abab")
