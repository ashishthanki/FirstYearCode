# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 13:59:18 2013

@author: Ashish
"""

import math


def swing_time(L):
    """computes and return the time needed for an idealized pendulum of length
    L to complete a single oscillation"""
    g = 9.81
    t = 2 * math.pi * (L / g) ** 0.5
    return t


def range_squared(n):
    """computes a non-negative integer value n and returns a list of the
    square of the range"""
    result = []
    xs = range(n)
    for x in xs:
        result.append(x ** 2)
    return result


def count(element, seq):
    """counts how often a given element occurs in a sequence seq and returns
    this integer value"""
    p = 0
    for item in seq:
        if item == element:
            p += 1
    return p
