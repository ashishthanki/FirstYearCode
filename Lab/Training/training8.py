# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\at6g13\.spyder2\.temp.py
"""


def f1(x):
    """computes and returns the value of f(x)"""
    import math
    p = math.pi
    c = math.cos(2 * p * x)
    d = math.exp(-x ** 2)
    e = c * d
    return e


def f2(x):
    """accepts the number x as input and computes and returns f2(x)"""
    import math
    l = math.log(x + 2.1)
    return l


def positive_places(f, xs):
    """take a function f and a list of number xs and returns a list of
    those-only-those elements x of xs for which f(x) is strictly greater
    than zero"""
    #return [f(x) for x in xs if f(x) > 0]
    return filter(lambda x: f(x) > 0, xs)


def reverse_dic(d):
    """takes a dictionary d as the input argument
    and returns a dictionary r"""
    e = {}
    for i in d.keys():
        e[d[i]] = i
    return e
