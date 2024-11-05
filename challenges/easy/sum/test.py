import pytest
from .solution import sum

"""
Challenge: Sum Two Numbers

Difficulty: Easy
Description:
    Write a function that takes two integers as input and returns their sum.

Examples:
    add_numbers(1, 2) -> 3
    add_numbers(-1, 1) -> 0
    add_numbers(0, 0) -> 0

Requirements:
    - Function should be named 'add_numbers'
    - Function should take two parameters: a and b
    - Parameters and return value should be integers
"""


def test_add_positive_numbers():
    assert sum(1, 2) == 3
    assert sum(10, 20) == 30


def test_add_negative_numebrs():
    assert sum(-1, -2) == -3
    assert sum(-10, -20) == -30


def test_add_mixed_numbers():
    assert sum(-1, 1) == 0
    assert sum(10, 5) == 5


def test_add_zero():
    assert sum(0, 0) == 0
    assert sum(5, 0) == 5
    assert sum(0, 5) == 5
