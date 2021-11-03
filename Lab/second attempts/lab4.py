# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:13:04 2013

@author: Ashish
wc"""


def seq_sqrt(xs):
    """takes a list of positive intergers and returns the square root of all
    the numbers in a list"""
    result = []
    for x in xs:
        result.append(x ** 0.5)
    return result


def mean(xs):
    """takes a sequence xs of numbers and returns the mean of the list"""
    return float(sum(xs)) / len(xs)


def wc(filename):
    """returns the number of words in a file"""
    f = open(filename, 'r')
    words = f.read()
    f.close
    s = words.split()
    return len(s)
