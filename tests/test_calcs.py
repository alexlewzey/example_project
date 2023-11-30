import pytest

from src.calcs import add, sub


def test_add():
    assert add(1, 1) == 2
    assert add(1, 3) == 4


def test_sub():
    assert sub(2, 1) == 1
