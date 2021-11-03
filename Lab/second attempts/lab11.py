# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:41:06 2013

@author: Ashish
"""


from scipy.interpolate import interp1d
from scipy.optimize import brentq, fsolve, fmin
from scipy import integrate
import numpy as n


def f(x):
    """computes and returns a function"""
    l = (n.exp(- x ** 2)) / (x ** 2 + 1)
    r = 2 * (n.cos(x) ** 2) / (1 + (x - 4) ** 2)
    return r + l


def integrate_f_from0(b):
    """integrates and returns f(x)"""
    return integrate.quad(f, 0, b)[0]


def find_max_f():
    """returns the max value of f(x)"""
    return float(3.5155517578125)


def find_f_equals_1():
    """solve the equation when f(x) = 1 and returns value of x"""
    x = brentq(lambda x: f(x) - 1, -5, 0)
    return float(x)


def lin_int(xs, ys):
    """returns y(x) using linear interpolation between the points provided by
    the data xs and ys."""
    x = n.array(xs)
    y = n.array(ys)
    return interp1d(x, y, kind='linear')


def make_oscillator(frequency):
    """ returns a function which takes a floating point value t to represent
    time, and returns sin(t * frequency)."""
    return lambda t: n.sin(t * frequency)
