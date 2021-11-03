# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:26:45 2013

@author: Ashish
"""

from scipy import integrate


def trapez(f, a, b, n):
    """computes and returns the trapezoidal integration rule"""
    h = float((b - a)) / n
    p = sum(map(lambda i: f(a + i * h), range(1, n)))
    return (h * 0.5) * (f(a) + f(b) + 2 * p)


def finderror(n):
    """uses the trapez() function and returns the error of the
    trapezoidal integral approximation."""
    error = trapez(lambda x: x * x, 0, 2, n)
    return (1 / float(3) * 2 ** 3) - error


def using_quad():
    """computes the integral of x2 from a=0 to b=2 using scipy.integrate.quad.
    should return the value that the quad() function returns a tuple
    y,abserr"""
    I = integrate.quad(lambda x: x ** 2, 0, 2)
    return I


def std_dev(x):
    """computes a list of floating point numbers and returns the SD of the
    elements"""
    N = len(x)
    u = sum(x) * 1 / float(N)
    t = 0
    for i in x:
        t += (i - u) ** 2
    o = (float(t) / N) ** 0.5
    return o
