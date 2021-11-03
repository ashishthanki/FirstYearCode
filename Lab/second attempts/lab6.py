# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:33:18 2013

@author: Ashish
"""


def eval_f(f, xs):
    """takes a function f = f(x) and a list xs and returns another list
    of f(x) of each value in xs"""
    result = []
    for x in xs:
        result.append(f(x))
    return result


def sum_f(f, xs):
    """computes and returns the sum of the function values f"""
    result = 0
    for x in xs:
        result += f(x)
    return result


def SUM_f(f, xs):
    y = []
    for x in xs:
        y.append(f(x))
    return sum(y)


def box_volume_UPS(a=13, b=11, c=2):
    """computes and returns the volume of a box with edge lengths a,b and c"""
    return a * b * c
