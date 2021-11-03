# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 16:19:14 2013

@author: Ashish
"""

g = 9.81


def box_volume(a, b, c):
    """calculates and returns the volume of a cuboid with edge lenghts
    a,b,c"""
    return a * b * c


def fall_time(h):
    """computes and returns the time needed for an object falling from height
    h to hit the ground"""
    t = ((2 * h) / float(g)) ** 0.5
    return t


def interval_point(a, b, x):
    """computes and returns take three number and interprets a and b as the
    start and end point of an interval, and x as a fraction between
    0 and 1 that determines how far to go towards b starting from a"""
    return a + (b - a) * x


def impact_velocity(h):
    """computes and return the impact velocity of an object dropped at
    height h"""
    return fall_time(h) * g


def signum(x):
    """computes and returns 1 if x>0, returns 0 if x=0 and returns -1 if
    x<0"""
    if x == 0:
        return 0
    if x > 0:
        return 1
    if x < 0:
        return -1
