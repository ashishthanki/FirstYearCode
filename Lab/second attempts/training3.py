# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:11:48 2013

@author: Ashish
"""

import math


def degree(x):
    """computes x as radians and returns in degrees"""
    return x * (180 / math.pi)


def min_max(xs):
    """computes the minimum value xmin of the elements in the list xs, and
    the maximum value xmax of the elements in the list and returns
    a tuple(xmin, xmax)"""
    return (min(xs), max(xs))


def geometric_mean(xs):
    """computes and returns the geometric mean of numbers"""
    y = 1
    for x in xs:
        y *= x #y = y * x
    return y ** (1. / (len(xs)))
