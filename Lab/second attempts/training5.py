# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:01:39 2013

@author: Ashish
"""


def count_sub_in_file(filename, s):
    """takes 2 arguments filename and substring s and returns the number
    of occurrences of s in the file"""
    try:
        f = open(filename, 'r')
    except IOError:
        return -1
    words = f.read()
    f.close
    p = 0
    r = 0
    for char in words:
        if s == char:
            r = r + 1
    xs = words.split()
    for x in xs:
        if s == x:
            p = p + 1
    return p + r


def count_vowels(s):
    """counts the number of vowels in a string and return an interger value"""
    p = 0
    xs = s.lower()
    for x in xs:
        if 'a' == x:
            p += 1
        if 'e' == x:
            p += 1
        if 'i' == x:
            p += 1
        if 'o' == x:
            p += 1
        if 'u' == x:
            p += 1
    return p
