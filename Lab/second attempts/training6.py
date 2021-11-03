# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:35:49 2013

@author: Ashish
"""


def positive_places(f, xs):
    """takes a function f and a list xs and returns a list of values
    which are positive when they are in the function f"""
    result = []
    for x in xs:
        if f(x) > 0:
            result.append(x)
    return result


def eval_f_0123(f):
    """takes a function and returns a list of f(x = 1,2,3,4)"""
    xs = range(4)
    result = []
    for x in xs:
        result.append(f(x))
    return result
