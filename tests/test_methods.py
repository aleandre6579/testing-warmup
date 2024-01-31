import pytest

from testing_warmup.app import is_palindrome, fibonacci


@pytest.mark.parametrize('word, answer', [
    ("racecar", True), ("nope", False), ("hellolleh", True), ("almostapalindromemordnilaapatsomla", False), ("thisisapalindromeemordnilapasisiht", True)
])
def test_palindrome(word, answer):
    assert is_palindrome(word) is answer


@pytest.mark.parametrize('x, y', [
    (1, 1), (2, 1), (3, 2), (19, 4181)
])
def test_fibonacci(x, y):
    assert fibonacci(x) == y