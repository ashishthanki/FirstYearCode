# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:35:33 2013

@author: at6g13
"""


def derivative(f, x, eps=10**-6):
    """computes and returns a numerical approximation of the first derivative
    of the function f(x) using central differences"""
    r = (f(x + 0.5 * eps) - f(x - 0.5 * eps)) / eps
    return r


def newton(f, x, feps, maxit):
    """takes a function f(x) and an initial guess x for the root of the
    function f(x), an allowed tolerance feps and the maximum
    number of iterations that are allowed maxit and return the newton-raphson
    algorithm"""
    p = 0
    while abs(f(x)) > feps:
        p += 1
        if maxit == p:
            raise RuntimeError("Failed after %d iterations" % maxit)
        x = x - (float(f(x)) / derivative(f, x))
    return x


def is_palindrome(s):
    """takes a string s and returns the value True if s is a palindrome,
    and returns False otherwise"""
    b = len(s)
    c = 0
    for i in range(b):
        if s[i] == s[-(i+1)]:
            c = c + 1
    if c == b:
        return True
    else:
            return False
