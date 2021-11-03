# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\at6g13\.spyder2\.temp.py
"""


def vector_product3(a, b):
    """computes and returns the product of two 3d vectors"""
    [ax, ay, az] = a
    [bx, by, bz] = b
    return [ay * bz - az * by, az * bx - ax * bz, ax * by - ay * bx]


def seq_mult_scalar(a, s):
    """computes and returns a list of numbers a and a scalar
    (i.e. a number) s. For the input
    a=[a0, a1, a2,.., an] the function
    should return [s * a0, s * a1, s * a2, ..., s * an]."""
    result = []
    for n in list(a):
        result.append(n * s)
    return result


def powers(n, k):
    """returns the list [1,n,n^2,n^3,...,n^k] where k is an integer.
    Note that there should be k+1 elements in the list."""
    result = []
    for i in range(k+1):
        result.append(n ** i)
    return result


def traffic_light(load):
    """ computes load and returns "green" for values of load below 0.7.
    "amber" for values of load equal to or greater
    than 0.7 but smaller than 0.9 .
    "red" for values of load equal to 0.9 or
    greater than 0.9"""
    p = load
    if p < 0.7:
        return 'green'
    elif 0.7 <= p < 0.9:
        return 'amber'
    elif p >= 0.9:
        return 'red'
