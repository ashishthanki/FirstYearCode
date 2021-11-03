# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\at6g13\.spyder2\.temp.py
"""

import scipy.integrate


def trapez(f, a, b, n):
    """computes and returns an appoximation of f(x)"""
    h = float(b - a) / n
    s = 0
    for i in range(1, n):
        xi = a + i*h
        s = s + f(xi)
    return (h/2.) * (f(a) + f(b) + 2*s)


def finderror(n):
    """ which computes and returns the trapez() function to find the error of
    the trapezoidal integral approximation."""
    return 8/3. - trapez(lambda x: x*x, 0, 2, n)


def using_quad():
    """computes and returns the integral of x2 from a=0 to b=2
    using scipy.integrate.quad."""
    return scipy.integrate.quad(lambda x: x*x, 0, 2)


def std_dev(x):
    """takes a list x of floating point numbers and computes and returns the
    standard deviation of the sample"""
    n = len(x)
    s = 0
    for i in x:
        s = s + i
    mu = s/float(n)
    u = 0
    for i in x:
        u = u + (i - mu)**2
    return (u/n)**0.5
