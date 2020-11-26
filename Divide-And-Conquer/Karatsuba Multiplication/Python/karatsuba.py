# Implementation of karatsuba multiplication Algorithm
import math


def karatsuba(x, y):
    """
    Karatsuba multiplication
    :param x: Any number or string
    :param y: Any number  or string
    :return: Product of two numbers x and y
    """

    if x < 10 and y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))  # length of the greatest number
    m = int(n / 2)  # Length to be divided into

    x_h = int(x / 10 ** m)  # first half of x
    x_l = int(x % 10 ** m)  # second half of x

    y_h = int(y / 10 ** m)  # first half of y
    y_l = int(y % 10 ** m)  # second half of y

    s1 = karatsuba(x_h, y_h)
    s2 = karatsuba(x_l, y_l)
    s3 = karatsuba(int(x_h + x_l), int(y_h + y_l)) - s2 - s1
    return int(s1 * 10 ** (m * 2) + (s3 * (10 ** m)) + s2)


