# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:13:49 2013

@author: Ashish
"""


def count_chars(s):
    """takes a string s and returns a dictionary's key"""
    result = {}
    for chars in s:
        result[chars] = s.count(chars)
    return result


def derivative(f, x, eps=1e-6):
    """computes and returns the derivative of f"""
    y = (f(x + eps / 2) - f(x - eps / 2)) / eps
    return y
