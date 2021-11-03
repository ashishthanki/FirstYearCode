# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 15:44:24 2013

@author: Ashish
"""

import numpy as n


def f(x):
    """computes and returns a function"""
    l = (n.exp(- x ** 2)) / (x ** 2 + 1)
    r = 2 * (n.cos(x) ** 2) / (1 + (x - 4) ** 2)
    return r + l


def make_multiplier(factor):
    """returns a function which takes an argument x and returns factor * x"""
    return lambda x: x * factor
