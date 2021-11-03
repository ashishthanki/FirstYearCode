# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 02:47:00 2014

@author: Ashish
"""


import pylab as py
import numpy as np


def binom(n, k):
    """Function that calulates and returns the binomial coefficeint ie.
    performs n choose k"""
    if 0 <= k <= n:
        p = 1
        for t in xrange(min(k, n - k)):
            p = (p * (n - t)) // (t + 1)
        return p
    else:
        return 0


def bezier(points):
    """Function that computes and returns a cubic bezier curve with control
    points defined by n x 2 and returns 101 x 2 array of of x, y"""
    a = points
    n = np.shape(a)[0] - 1
    b = np.zeros([101, 2])
    terms = np.zeros([n+1, 2])
    t = np.linspace(0, 1, 101)
    for i in range(0, 101):
        for j in range(0, n+1):
            terms[j, :] = a[j, :]*binom(n, j)*t[i]**j*(1-t[i])**(n-j)
        b[i, :] = sum(terms, 0)
    py.plot(b[:, 0], b[:, 1])
    py.plot(a[:, 0], a[:, 1], 'ko')
    py.plot(a[:, 0], a[:, 1], 'k')
    py.show()
    return b[:, 0:2]


def rational_bezier(points, weights):
    """Function that computes and returns a cubic bezier curve with n control
    points with n weights and returns 101 x 2 array of of x, y on the
    curve for t[0, 1]"""
    a = points
    w = weights
    n = np.shape(a)[0] - 1
    b = np.zeros([101, 2])
    terms = np.zeros([n+1, 2])
    d = np.zeros([n+1])
    t = np.linspace(0, 1, 101)
    for i in range(0, 101):
        for j in range(0, n+1):
            terms[j, :] = w[j]*a[j, :]*binom(n, j)*t[i]**j*(1-t[i])**(n-j)
            d[j] = w[j]*binom(n, j)*t[i]**j*(1-t[i])**(n-j)
        b[i, :] = sum(terms, 0)/sum(d)
    py.plot(b[:, 0], b[:, 1])
    py.plot(a[:, 0], a[:, 1], 'ko')
    py.plot(a[:, 0], a[:, 1], 'k')
    py.show()
    return b[:, 0:2]
