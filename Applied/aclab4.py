# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:42:04 2014

@author: Ashish
"""


import pylab as p
import numpy as np
import os
from scipy.optimize import fmin_bfgs, fmin_l_bfgs_b
import math


def binom(n, i):
    if 0 <= i <= n:
        a = 1
        for t in xrange(min(i, n - i)):
            a = (a * (n - t)) / (t + 1)
        return a
    else:
        return 0


def rational_bezier(points, weights):
    a = points
    w = weights
    n = (len(points) - 1)
    t = np.linspace(0, 1, 101)
    terms = np.zeros([n + 1, 2])
    Bezier = np.zeros([101, 2])
    wb = np.zeros(n + 1)
    for i in range(0, 101):
        for s in range(0, n + 1):
            terms[s, :] = w[s] * binom(n, s) * t[i] ** (s) * (1 - t[i]) ** \
                (n - s) * a[s, :]
            wb[s] = w[s] * binom(n, s) * t[i] ** (s) * (1 - t[i]) ** \
                (n - s)
        Bezier[i, :] = (sum(terms, 0) / sum(wb, 0))
    return Bezier


def parametric_aerofoil(w, file_path):
    """"""
    l = np.array([[1.0, 0.0], [0.5, 0.08], [0.0, -0.05], [0.0, 0.0]])
    u = np.array([[0.0, 0.0], [0.0, 0.1], [0.4, 0.2], [1.0, 0.0]])
    weightsl = [1, 1, 1, 1]
    weightsu = [1, 1, w, 1]
    m = len(u)
    n = len(l)
    l[-1, :] = u[0, :] = (m / float(m + n)) * u[1, :] + (n / float(n + m)) * \
        l[-2, :]
    lower = rational_bezier(l, weightsl)
    upper = rational_bezier(u, weightsu)
    data_file = open(file_path + '\\aerofoil.dat', 'w')
    for i in range(0, 100):
        data_file.write("%f %f\n" % (lower[i, 0], lower[i, 1]))
    for i in range(0, 101):
        data_file.write("%f %f\n" % (upper[i, 0], upper[i, 1]))
    data_file.close()
    #p.plot(upper[:, 0], upper[:, 1])
    #p.plot(lower[:, 0], lower[:, 1])
    #p.plot(l[:, 0], l[:, 1], 'ko')
    #p.plot(u[:, 0], u[:, 1], 'ko')
    #p.plot(l[:, 0], l[:, 1], 'k')
    #p.plot(u[:, 0], u[:, 1], 'k')


def run_xfoil_wcl(w, cl, file_path, xfoil_path, Re=1397535, M=0.1):
    parametric_aerofoil(w, file_path)
    command_file = open(file_path + '\\commands.in', 'w')
    command_file.write(
        'load ' + file_path + '\\aerofoil.dat' + "\n"
        'CubicBez' + "\n"
        'panel' + "\n"
        'oper' + "\n"
        'visc ' + str(Re) + "\n"
        'M ' + str(M) + "\n"
        'type 1' + "\n"
        'pacc' + "\n"
        + file_path + '\\polar.dat' + "\n" + "\n"
        'iter' + "\n"
        '1000' + "\n"
        'cl ' + str(cl) + "\n" + "\n" + "\n"
        'quit' + "\n" + "\n")
    command_file.close()
    run = xfoil_path + '\\xfoilP4 < ' + file_path + '\\commands.in'
    os.system(run)
    a = open(file_path + '\\polar.dat', 'r')
    b = a.read()
    a.close()
    os.remove(file_path + '\\polar.dat')
    os.remove(file_path + '\\aerofoil.dat')
    os.remove(file_path + '\\commands.in')
    c = b.split()
    cl = float(c[-6])
    cd = float(c[-5])
    return cd


def parameter_sweep(w_array, cl, file_path, xfoil_path, Re=1397535, M=0.1):
    cdlist = []
    command_file = open(file_path + '\\commands.in', 'w')
    command_file.write(
        'load ' + file_path + '\\aerofoil.dat' + "\n"
        'CubicBez' + "\n"
        'panel' + "\n"
        'oper' + "\n"
        'visc ' + str(Re) + "\n"
        'M ' + str(M) + "\n"
        'type 1' + "\n"
        'pacc' + "\n"
        + file_path + '\\polar.dat' + "\n" + "\n"
        'iter' + "\n"
        '1000' + "\n"
        'cl ' + str(cl) + "\n" + "\n" + "\n"
        'quit' + "\n" + "\n")
    command_file.close()
    for w in w_array:
        parametric_aerofoil(w, file_path)
        run = xfoil_path + '\\xfoilP4 < ' + file_path + '\\commands.in'
        os.system(run)
        a = open(file_path + '\\polar.dat', 'r')
        b = a.read()
        a.close()
        os.remove(file_path + '\\polar.dat')
        os.remove(file_path + '\\aerofoil.dat')
        c = b.split()
        cd = float(c[-5])
        cdlist.append(cd)
    os.remove(file_path + '\\commands.in')
    return cdlist


#1D quadratic moving least squares
def mls(x, X, y, sigma):
    N = max(len(y))
    weights = np.zeros(N)
    A = np.zeros([N, 3])
    A[:, 0] = X**2
    A[:, 1] = X
    A[:, 2] = np.ones([1, N])
    for i in range(1, N):
        weights[i] = math.exp(-sum((x - x[i]) ** 2) / (2 * sigma))
        W = math.diag(weights)
        a = math.linalg.lstsq(math.dot(math.dot(A.conj().T, W), A),
                              math.dot(math.dot(A.conj().T, W), y))
        f = a[0][0] * x ** 2 + a[0][1] * x + a[0][2]
        return f


def mls_error(sigma, X, y, cd):
    y_test = np.zeros(11)
    error = np.zeros(11)
    for i in range(0, 11):
        y_test[i] = mls(X[i], (X[0: i], X[i + 1: -1]), (y[0: i],
                        y[i + 1: -1]), sigma)
        error[i] = (cd[i] - y_test[i]) ** 2
    sum_error = math.sum(error)
    return sum_error


def one_dim_opt(x0, cl, file_path, xfoil_path):
    opt_out = fmin_bfgs(run_xfoil_wcl, x0, args=(cl, file_path, xfoil_path),
                        epsilon=0.15)
    return opt_out


def parametric_aerofoil4(w_list, file_path):
    l = np.array([[1.0, 0.0], [0.5, 0.08], [0.0, -0.05], [0.0, 0.0]])
    u = np.array([[0.0, 0.0], [0.0, 0.1], [0.4, 0.2], [1.0, 0.0]])
    weightsl = [1, 1, w_list[2], w_list[3]]
    weightsu = [1, 1, w_list[0], w_list[1]]
    m = len(u)
    n = len(l)
    l[-1, :] = u[0, :] = (m / float(m + n)) * u[1, :] + (n / float(n + m)) * \
        l[-2, :]
    lower = rational_bezier(l, weightsl)
    upper = rational_bezier(u, weightsu)
    data_file = open(file_path + '\\aerofoil.dat', 'w')
    for i in range(0, 100):
        data_file.write("%f %f\n" % (lower[i, 0], lower[i, 1]))
    for i in range(0, 101):
        data_file.write("%f %f\n" % (upper[i, 0], upper[i, 1]))
    data_file.close()
    #p.plot(upper[:, 0], upper[:, 1])
    #p.plot(lower[:, 0], lower[:, 1])
    #p.plot(l[:, 0], l[:, 1], 'ko')
    #p.plot(u[:, 0], u[:, 1], 'ko')
    #p.plot(l[:, 0], l[:, 1], 'k')
    #p.plot(u[:, 0], u[:, 1], 'k')


def run_xfoil_4wcl(w_list, cl, file_path, xfoil_path):
    a = 340.3  # speed of sound
    v = 12.5  # velocity
    M = v/float(a)  # Mach number
    nu = 0.00001461  # kinematic viscosity
    L = 0.698  # chord length of aircraft wing
    Re = v*L/nu  # Reynold’s number
    M = 0.1
    parametric_aerofoil4(w_list, file_path)
    command_file = open(file_path + '\\commands.in', 'w')
    command_file.write(
        'load ' + file_path + '\\aerofoil.dat' + "\n"
        'CubicBez' + "\n"
        'panel' + "\n"
        'oper' + "\n"
        'visc ' + str(Re) + "\n"
        'M ' + str(M) + "\n"
        'type 1' + "\n"
        'pacc' + "\n"
        + file_path + '\\polar.dat' + "\n" + "\n"
        'iter' + "\n"
        '1000' + "\n"
        'cl ' + str(cl) + "\n" + "\n" + "\n"
        'quit' + "\n" + "\n")
    command_file.close()
    run = xfoil_path + '\\xfoilP4 < ' + file_path + '\\commands.in'
    os.system(run)
    a = open(file_path + '\\polar.dat', 'r')
    b = a.read()
    a.close()
    os.remove(file_path + '\\polar.dat')
    os.remove(file_path + '\\aerofoil.dat')
    os.remove(file_path + '\\commands.in')
    c = b.split()
    cl = float(c[-6])
    cd = float(c[-5])
    return cd


def four_dim_opt(x0, weight_limits, cl, file_path, xfoil_path):
    opt_out = fmin_l_bfgs_b(run_xfoil_4wcl, x0, args=(cl, file_path,
                                                      xfoil_path),
                            bounds=weight_limits, epsilon=0.3,
                            approx_grad=True)
    return opt_out
