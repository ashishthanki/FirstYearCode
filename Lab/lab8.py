# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:48:30 2013

@author: at6g13
"""
import math
import pylab
from scipy.optimize import brentq


def f1(x):
    """computes and returns the value of f(x)"""
    p = math.pi
    c = math.cos(2 * p * x)
    d = math.exp(-x ** 2)
    e = c * d
    return e


def f2(x):
    """accepts the number x as input and computes and returns f2(x)"""
    l = math.log(x + 2.1)
    return l


def create_plot_data(f, xmin, xmax, n):
    """returns a tuple (xs, ys) where xs and ys are two sequences,
    each containing n numbers"""
    xs = []
    ys = []
    for i in range(n):
        x = xmin + i*(xmax - xmin)/float(n - 1)
        xs.append(x)
        ys.append(f(x))
    return (xs, ys)


def myplot():
    """computes, plots and returns f1(x) and f2(x)"""
    data1 = create_plot_data(f1, -2, 2, 1001)
    pylab.plot(data1[0], data1[1], label='f1')
    data2 = create_plot_data(f2, -2, 2, 1001)
    pylab.plot(data2[0], data2[1], label='f2')
    pylab.legend()
    pylab.xlabel('x')
    pylab.ylabel('y')
    pylab.savefig('plot.png')
    pylab.savefig('plot.pdf')
    pylab.show()


def y(x):
    """difference of f1(x) and f(x)"""
    return f1(x) - f2(x)


def find_cross():
    """computes and returns the value for x for which f1(x) = f2(x)"""
    return brentq(y, 0, 0.2)
