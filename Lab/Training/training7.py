# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\at6g13\.spyder2\.temp.py
"""


def count_chars(s):
    """computes a string s and returns a dictionary.
    The dictionary's keys are the set of characters that occur in string s.
    The value for each key is the number
    of times that this character occurs in the string s"""
    result = {}
    for character in s:
        result[character] = s.count(character)
    return result


def derivative(f, x, eps=10**-6):
    """computes and returns a numerical approximation of the first
    derivative of the function f(x) using central differences"""
    r = (f(x + 0.5 * eps) - f(x - 0.5 * eps)) / eps
    return r
