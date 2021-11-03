# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 11:04:43 2013

@author: Ashish
"""

import numpy as np
from numpy import array
import pylab
from scipy import optimize


def model(ts, Ti, Ta, c):
    """implements and returns equation 1"""
    C = float(c)
    T = (Ti - Ta) * np.exp(-ts / C) + Ta
    return T


def read2coldata(filename):
    """opens a text file with two columns of data,and returns two numpy arrays
    where the first contains all the data from the first column etc"""
    f = open(filename, 'r')
    n = f.readlines()
    f.close
    result1 = []
    result2 = []
    for i in n:
        result1.append(float(i.split()[0]))
        result2.append(float(i.split()[1]))
    ts = array(result1)
    Ts = array(result2)
    return (ts, Ts)


def extract_parameters(ts, Ts):
    """which expects two numpy arrays ts and Ts of the same length,and returns
    a tuple of the three model parameters Ti,Ta and c by fitting into 1"""
    popt, pcov = optimize.curve_fit(model, ts, Ts, p0=[80, 20, 1200])
    return popt


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
    pylab.savefig('testcompare.pdf')


def sixty_degree_time(Ti, Ta, c):
    """returns the number of seconds for the drink to cool to 60 degrees"""
    T = 60
    p1 = float(T - Ta) / (Ti - Ta)
    return np.log(p1) * -c


if __name__ == "__main__":
    ts, Ts = read2coldata('time_temp.txt')
    Ti, Ta, c = extract_parameters(ts, Ts)
    print("Model parameters are Ti=%f C, Tf=%fC," % (Ti, Ta))
    print("                     time constant=%fs" % c)
    waittime = sixty_degree_time(Ti, Ta, c)
    print("The drink reaches 60 degrees after %s seconds = %f minutes"
          % (waittime, waittime / 60.))
