# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:00:14 2014

@author: Ashish
"""


def mult3vec(c, v):
    return map(lambda x: x * c, v)


def multvec(c, v):
    return map(lambda x: x * c, v)


def convert_time(t):
    d = float(t) / 1440
    h = abs(d - int(d)) * 24
    m = abs(h - int(h)) * 60
    return (int(d), int(h), round(m))


import numpy as n


def nearest(xs, a):
    return min(xs, key=lambda x: abs(x - a))


def derivative(f, xs):
    cx = 10 ** -6
    return map(lambda x: float(f(x + cx) - f(x)) / cx, xs)


def read(filename):
    f = open(filename, 'r')
    w = f.readlines()
    f.close
    result1 = []
    result2 = []
    for l in w:
        result1.append(l.split()[0])
        result2.append(l.split()[1])
    x = n.array(result1)
    y = n.array(result2)
    return (x, y)


def isfib(F):
    old = 0
    cur = 1
    xs = [0, 1]
    for d in range(len(F) - 2):
        c = old + cur
        xs.append(c)
        old = cur
        cur = c
    if xs == F:
        return True
    else:
        return False
