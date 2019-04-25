"""Tests for summation"""

from src.codewars.challenges import summation


def test_summation():
    """Tests for summation"""
    assert summation.summation(1) == 1
    assert summation.summation(2) == 3
    assert summation.summation(8) == 36
