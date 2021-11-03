# -*- coding: utf-8 -*-
"""
Created on Thu Nov 07 15:37:22 2013

@author: Ashish
"""


def eval_f(f, xs):
    """ takes a function f = f(x) and a list xs of values that
    should be used as arguments for f. The function eval_f should
    apply the function f subsequently to every value x in xs,
    and return a list fs of function values."""
    result = []
    for x in xs:
        p = f(x)
        result.append(p)
    return result


def sum_f(f, xs):
    """computes and returns the sum
    of the funcion value of f"""
    p = 0
    for x in xs:
        p = p + f(x)
    return p


def box_volume_UPS(a=13, b=11, c=2):
    """computes and returns the volume of a box
    The standard dimensions of the UPS express box
    (small) are a=13 inch, b=11 inch and c=2 inch, unless
    others are provided"""
    return a * b * c
