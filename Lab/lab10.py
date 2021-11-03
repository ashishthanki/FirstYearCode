# -*- coding: utf-8 -*-
"""
Created on Wed Dec 04 17:02:03 2013

@author: at6g13
"""
import numpy as np
import scipy.optimize
import pylab


def model(ts, Ti, Ta, c):
    """computes and returns the T(t)"""
    T = ((Ti - Ta) * np.exp(- ts / c)) + Ta
    return T


def read2coldata(filename):
    """opens a text file with two columns of data. The columns have to be
    separated by white space. The function should return a tuple of two
    numpy-arrays where the first contains all the data from the first column
    in the file, and the second all the data in the second column."""
    f = open(filename, 'r')
    a = f.readlines()
    f.close()
    b = []
    c = []
    for i in a:
        b.append(float(i.split()[0]))
        c.append(float(i.split()[1]))
    d = np.array(b)
    e = np.array(c)
    return d, e


def extract_parameters(ts, Ts):
    """numpy array ts with time values and a numpy array Ts of the same length
    as ts with corresponding temperature values. The function should estimate
    and return a tuple of the three model parameters Ti, Ta and c"""
    p, pcov = scipy.optimize.curve_fit(model, ts, Ts, p0=[80, 20, 750])
    return p


def sixty_degree_time(Ti, Ta, c):
    """the model paramaters Ti (initial temperature), Ta (ambient temperature)
    and c the cooling rate time constant. The function should return an
    estimate of the number of seconds after which the temperature of the drink
    has cooled down to 60 degree Celsius"""
    a = np.log(float(60 - Ta) / (Ti - Ta)) * c
    return a


def plot(ts, Ts, Ti, Ta, c):
    """Input Parameters:

      ts : Data for time (ts)
                (numpy array)
      Ts : data for temperature (Ts)
                (numpy arrays)
      Ti : model parameter Ti for Initial Temperature
                (number)
      Ta : model parameter Ta for Ambient Temperature
                (number)
      c  : model parameter c for the time constant
                (number)

    This function will create plot that shows the model fit together
    with the data.

    Function returns None.
    """

    pylab.plot(ts, Ts, 'o', label='data')
    fTs = model(ts, Ti, Ta, c)
    pylab.plot(ts, fTs, label='fitted')
    pylab.legend()
    pylab.show()
