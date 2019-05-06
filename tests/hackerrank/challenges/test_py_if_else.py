"""Tests for py_if_else"""

from src.hackerrank.challenges import py_if_else


def test_is_wierd():
    """Tests for is_wierd"""
    # if n is odd, print Wierd
    assert py_if_else.is_wierd(0) == "Wierd"
    assert py_if_else.is_wierd(1) == "Wierd"
    assert py_if_else.is_wierd(3) == "Wierd"
    assert py_if_else.is_wierd(5) == "Wierd"
    assert py_if_else.is_wierd(7) == "Wierd"
    assert py_if_else.is_wierd(19) == "Wierd"
    assert py_if_else.is_wierd(21) == "Wierd"

    # If n is even and in the inclusive range of 2 to 5, print Not Weird
    assert py_if_else.is_wierd(2) == "Not Wierd"
    assert py_if_else.is_wierd(4) == "Not Wierd"

    # If n is even and in the inclusive range of 6 to 20, print Weird
    assert py_if_else.is_wierd(6) == "Wierd"
    assert py_if_else.is_wierd(8) == "Wierd"
    assert py_if_else.is_wierd(18) == "Wierd"
    assert py_if_else.is_wierd(20) == "Wierd"

    # If n is even and greater than 20, print Not Weird
    assert py_if_else.is_wierd(22) == "Not Wierd"
