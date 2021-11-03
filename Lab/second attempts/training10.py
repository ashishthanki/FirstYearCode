# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 11:04:43 2013

@author: Ashish
"""

import numpy as np


def model(ts, Ti, Ta, c):
    """implements and returns equation 1"""
    C = float(c)
    T = (Ti - Ta) * np.exp(-ts / C) + Ta
    return T
