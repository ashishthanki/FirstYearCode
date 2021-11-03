# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:50:04 2013

@author: Ashish
"""

import math


def f1(x):
    """computes and returns a function"""
    return math.cos(2 * math.pi * x) * math.exp(- x ** 2)


def f2(x):
    """computes and returns a function"""
    return math.log(x + 2.1)


def positive_places(f, xs):
    """computes and returns the values of x for which f(x) is positive"""
    return filter(lambda x: f(x) > 0, xs)


def reverse_dic(d):
    """takes a dictionary d as the input argument and returns a dictionary
    r.if d[k] = v then r[v] = k"""
    result = {}
    for key in d.keys():
        result[d[key]] = key
    return result
