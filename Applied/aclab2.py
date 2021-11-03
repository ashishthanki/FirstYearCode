# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 02:47:00 2014

@author: Ashish
"""


import pylab as py
import numpy as np
import os


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


def bezier_spline_aerofoil(file_path):
    """Create a bezier spline aerofoil with lower points and upper points
    with weighting of all control points is 1, function prints coodrinates
    and writes them to a file called aerofoil.dat"""
    l = np.array([[1.0, 0.0], [0.5, 0.08], [0.0, -0.05], [0.0, 0.0]])
    u = np.array([[0.0, 0.0], [0.0, 0.1], [0.4, 0.2], [1.0, 0.0]])
    wl = [1, 1, 1, 1]
    wu = [1, 1, 1, 1]
    n = len(l)
    m = len(u)
    upper = rational_bezier(u, wu)
    lower = rational_bezier(l, wl)
    l[-1] = u[0] = (float(m/(m+n))*u[1])+(float(n/(m+n))*l[-2])
    data_file = open(file_path + '//aerofoil.dat', 'w')
    for i in range(0, 100):
        data_file.write("%f\t %f\n" % (lower[i, 0], lower[i, 1]))
    for i in range(0, 101):
        data_file.write("%f\t %f\n" % (upper[i, 0], upper[i, 1]))
    data_file.close()


def command(file_path, Re=1397535, M=0.1):
    """Creates a file with commands that are to be inputed into xfoil to
    create a polar.dat file to be read by python"""
    command_file = open(file_path + '//commands.in', 'w')
    command_file.write(
        'load ' + file_path + '//aerofoil.dat' + "\n"
        'CubicBez' + "\n"
        'panel' + "\n"
        'oper' + "\n"
        'visc ' + str(Re) + "\n"
        'M ' + str(M) + "\n"
        'type 1' + "\n"
        'pacc' + "\n"
        + file_path + '//polar.dat' + "\n" + "\n"
        'iter' + "\n"
        '1000' + "\n"
        'cl 1.2' + "\n" + "\n" + "\n"
        'quit' + "\n" + "\n")
    command_file.close()


def run_xfoil(file_path, xfoil_path):
    """Executes the commands.in file in xfoil which produces a polar.dat
    file which is opened by python and the cd and cl figures are returned"""
    run = xfoil_path + '/Xfoil.app/Contents/Resources/xfoil < '\
        + file_path + '/commands.in '
    os.system(run)
    a = open(file_path + '//polar.dat', 'r')
    b = a.read()
    a.close()
    os.remove(file_path + '//polar.dat')
    c = b.split()
    cl = float(c[-6])
    cd = float(c[-5])
    return (cd, cl)
