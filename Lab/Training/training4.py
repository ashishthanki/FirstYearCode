"""
Spyder Editor

This temporary script file is located here:
C:\Users\at6g13\.spyder2\.temp.py
"""


import urllib


def line_averages(filename):
    """Compute the average value for every line
    and return the average values in a list"""
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    r = []
    for line in lines:
        numbers = line.split(',')
        s = 0
        for number in numbers:
            s = s + float(number)
        r.append(s/len(numbers))
    return r


def noaa_string():
    url = "http://weather.noaa.gov/pub/data" +\
        "/observations/metar/decoded/EGHI.TXT"
    noaa_data_string = urllib.urlopen(url).read()
    return noaa_data_string


def noaa_temperature(s):
    """find and returns the temperature in
    celius"""
    lines = s.split('\n')
    for line in lines:
        words = line.split()
        if words[0] == 'Temperature:':
            return int(words[3][1:])
