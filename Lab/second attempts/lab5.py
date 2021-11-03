# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:54:36 2013

@author: Ashish
"""


def vector_product3(a, b):
    """takes two sequences of numbers of three elements and returns a list
    which contains the vector product"""
    [ax, ay, az] = a
    [bx, by, bz] = b
    return [ay * bz - az * by, az * bx - ax * bz, ax * by - ay * bx]


def seq_mult_scalar(a, s):
    """takes a list of numbers a and multiplies each number on the list
    by the scalar s and returns another list"""
    result = []
    for x in a:
        result.append(s * x)
    return result


def powers(n, k):
    """computes and returns the list [1, .... n ^k]"""
    result = []
    for x in range(k + 1):
        result.append(n ** x)
    return result


def traffic_light(load):
    """takes a floating point number and should return the string
    "green" for <0.7 , "amber" for 0.9=>0.7 and "red" for =>0.9"""
    if load < 0.7:
        return 'green'
    if 0.9 > load >= 0.7:
        return 'amber'
    if load >= 0.9:
        return 'red'
