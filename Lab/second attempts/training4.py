# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 18:52:43 2013

@author: Ashish
"""

import urllib


def line_averages(filename):
    """computes a string filename, open and read that file.returns
    an average value for every line"""
    y = []
    f = open(filename, 'r')
    lines = f.readlines()
    f.close
    for x in lines:
        numbers = x.split(',')
        s = 0
        for number in numbers:
            s = s + float(number)
        y.append(s/len(numbers))
    return y


def noaa_string():
    url = "http://weather.noaa.gov/pub/data" +\
        "/observations/metar/decoded/EGHI.TXT"
    noaa_data_string = urllib.urlopen(url).read()
    return noaa_data_string


def noaa_temperature(x):
    """computes a string s and returns the temperature in degress celsius"""
    lines = x.split('\n')
    for line in lines:
        words = line.split()
        if words[0] == 'Temperature:':
            return int((words[3][1:]))
