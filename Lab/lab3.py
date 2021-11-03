# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:23:23 2013

@author: at6g13
"""


def swing_time(L):
    """Computes the idealized pendulum of length L
    and returns the time T, the period of the
    oscillation"""
    g = 9.81
    import math
    return (2 * math.pi) * (L / g) ** 0.5


def range_squared(n):
    """Computes the positve integer and returns
    the square of the n-1 squared term"""
    result = []
    for k in range(n):
        result.append(k ** 2)
    return result


def count(element, seq):
    """counts and returns how often the given element element occurs
    in the given sequence seq, and returns this integer value"""
    counter = 0
    for item in seq:
        if item == element:
            counter += 1
    return counter
