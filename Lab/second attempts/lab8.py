# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:51:27 2013

@author: Ashish
"""

import math
import pylab
import scipy.optimize


def f1(x):
    """computes and returns a function"""
    return math.cos(2 * math.pi * x) * math.exp(- x ** 2)


def f2(x):
    """computes and returns a function"""
    return math.log(x + 2.1)


def create_plot_data(f, xmin, xmax, n):
    """computes a function and returns two sequences"""
    xs = []
    ys = []
    if n >= 2:
        for i in range(n):
            xi = xmin + i * float(xmax - xmin) / (n-1)
            xs.append(xi)
            ys.append(f(xi))
    return xs, ys


def myplot():
    """computes f1(x) and plots f1(x) using 1001 points for -2 to +2. the
    function should return None"""
    xs, ys = create_plot_data(f1, -2, 2, 1001)
    xsi, ysi = create_plot_data(f2, -2, 2, 1001)
    pylab.plot(xs, ys, label='f1')
    pylab.plot(xsi, ysi, label='f2')
    pylab.xlabel('f1 and f2')
    pylab.legend()
    pylab.show()
    pylab.savefig('plot.pdf')
    pylab.savefig('plot.png')


def y(x):
    """difference of f1(x) and f2(x)"""
    y = f1(x) - f2(x)
    return y


def find_cross():
    """finds and returns the value of x for which f1 = f2"""
    return scipy.optimize.brentq(y, 0, 1)
