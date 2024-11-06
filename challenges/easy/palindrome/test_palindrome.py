import pytest
from .solution import palindrome

"""
Challenge: Palindrome

Difficulty: Easy
Description:
    Write a function that takes a string and determines if it is a palindrome.
    A palindrome is a string that spells the same word forwards and backwards.
    Ignore whitespace and punctuation.

Examples:
    palindrome('racecar') -> true
    palindrome('kayak') -> true
    palindrome('python) -> false

Requirements:
    - Function should be names 'palindrome'
    - Function should take one parameter: s
    - Parameter should be a string, return value should be boolean
"""


def test_palindrome_small_word_palindrome():
    assert palindrome('racecar')
    assert palindrome('kayak')
    assert palindrome('python') is False


def test_palindrome_sentence_palindrome():
    assert palindrome('Never odd or even.')
    assert palindrome('Won’t lovers revolt now?')
    assert palindrome('A man, a plan, a canal, Panama!')
    assert palindrome('This isnt a palindrome') is False
