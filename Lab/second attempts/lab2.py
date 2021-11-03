# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 16:35:40 2013

@author: Ashish
"""


def seconds2days(n):
    """computes and returns n seconds into days"""
    return n / float(24 * 3600)


def box_surface(a, b, c):
    """computes and returns the surface area of a box"""
    return ((a * b) + (a * c) + (b * c)) * 2


def triangle_area(a, b, c):
    """computes and returns the area of a triangle"""
    s = (a + b + c) / float(2)
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
