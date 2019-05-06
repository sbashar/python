"""Tests for py_if_else"""

from src.hackerrank.challenges import py_if_else


def test_is_wierd():
    """Tests for is_wierd"""
    # if n is odd, print Weird
    assert py_if_else.is_wierd(0) == "Weird"
    assert py_if_else.is_wierd(1) == "Weird"
    assert py_if_else.is_wierd(3) == "Weird"
    assert py_if_else.is_wierd(5) == "Weird"
    assert py_if_else.is_wierd(7) == "Weird"
    assert py_if_else.is_wierd(19) == "Weird"
    assert py_if_else.is_wierd(21) == "Weird"

    # If n is even and in the inclusive range of 2 to 5, print Not Weird
    assert py_if_else.is_wierd(2) == "Not Weird"
    assert py_if_else.is_wierd(4) == "Not Weird"

    # If n is even and in the inclusive range of 6 to 20, print Weird
    assert py_if_else.is_wierd(6) == "Weird"
    assert py_if_else.is_wierd(8) == "Weird"
    assert py_if_else.is_wierd(18) == "Weird"
    assert py_if_else.is_wierd(20) == "Weird"

    # If n is even and greater than 20, print Not Weird
    assert py_if_else.is_wierd(22) == "Not Weird"
