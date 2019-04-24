"""Tests for py_hello_world"""

from src.hackerrank.challenges import py_hello_world


def test_say_hello_world():
    """Tests for say_hello_world"""
    assert py_hello_world.say_hello_world() == "Hello, World!"
