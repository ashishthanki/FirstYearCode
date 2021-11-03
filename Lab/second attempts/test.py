# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 15:35:39 2013

@author: Ashish
"""


from lab10 import read2coldata, extract_parameters, sixty_degree_time

ts, Ts = read2coldata('time_temp.txt')
Ti, Ta, c = extract_parameters(ts, Ts)
print "Model parameters are Ti=%f C, Tf=%fC," % (Ti, Ta)
print "                     time constant=%fs" % c
waittime = sixty_degree_time(Ti, Ta, c)
print "The drink reaches 60 degrees after %s seconds = %f minutes" \
      % (waittime, waittime / 60.)
