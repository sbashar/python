"""
Solution for Hackerrank problem: https://www.hackerrank.com/challenges/py-if-else/problem
"""


def is_wierd(number):
    """
    If n is odd, print Weird
    If n is even and in the inclusive range of 2 to 5, print Not Weird
    If n is even and in the inclusive range of 6 to 20, print Weird
    If n is even and greater than 20, print Not Weird
    Returns:
        [str]: [returns Wierd if number is Wierd otherwise returns Not Wierd]
    """

    result = "Wierd"

    if number % 2 == 0:
        if 2 <= number <= 5 or number > 20:
            return "Not Wierd"

    return result
