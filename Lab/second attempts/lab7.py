# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:32:29 2013

@author: Ashish
"""


def derivative(f, x, eps=1e-6):
    """computes and returns the derivative of f"""
    y = (f(x + eps / 2) - f(x - eps / 2)) / eps
    return y


def newton(f, x, feps, maxit):
    """which takes a function and returns the newton raphson algorithm"""
    p = 0
    while abs(f(x)) > feps:
        p += 1
        if maxit == p:
            raise RuntimeError("Failed after %d iterations" % maxit)
        x = x - (float(f(x)) / derivative(f, x))
    return x


def is_palindrome(s):
    """takes a string s and returns the true if s is a palindrome
    and returns false if it is not"""
    p = 0
    for k in range(len(s)):
        if s[k] == s[-(k + 1)]:
            p += 1
    if p == len(s):
        return True
    else:
        return False
