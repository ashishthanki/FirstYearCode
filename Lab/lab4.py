# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:34:35 2013

@author: at6g13
"""


def seq_sqrt(xs):
    """computes and list of postive integers
    and returns the square root of the numbers
    in a list"""
    result = []
    for x in xs:
        result.append(x ** 0.5)
    return result


def mean(xs):
    """takes a sequence of numbers and
    returns the mean"""
    total = 0
    for i in xs:
        total += i
    length = len(xs)
    mean = float(total) / float(length)
    return mean


def wc(filename):
    """compute and returns the number words in the file ,filename"""
    words = []
    w = []
    f = open(filename, 'r')
    words = f.readlines()
    for line in words:
        w = line.split()
        for j in w:
            words.append(j)
    return len(words)
