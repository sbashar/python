"""
Solution for Codewars problem: https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
"""


def summation(num):
    """
    A program that finds the summation of every number from 1 to num.
    The number will always be positive integer greater than 0.
    Returns:
        [int]: [returns sum of every number from 1 to n]
    """
    total_sum = 0
    for i in range(1, num + 1):
        total_sum += i
    return total_sum
