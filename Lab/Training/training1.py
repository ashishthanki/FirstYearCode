# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:50:18 2013

@author: Ashish
"""

def average(a, b):
    """Compute and return the arithmetic mean of a and b"""
    return (a + b) / float(2)


def distance(a, b):
    """computes and returns the distance between a and b"""
    return abs(a - b)


def geometric_mean(a, b):
    """computes and returns the geometric mean of two numbers"""
    return (a * b) ** 0.5


def pyramid_volume(A, h):
    """computes and returns the volume of a pyramid with base area A and
    height h"""
    return (A * h) / float(3)

