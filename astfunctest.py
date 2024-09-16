
"""
Created on Tue Dec 10 21:01:29 2013

@author: rj

Created, by the author, as an example of a program using functions and
modules which can be imported in order to use its functions or 
run from the command line.

The asteroid data comes from 
http://ssd.jpl.nasa.gov/sbdb_query.cgi

"""

from Asteroids import Asteroids as As

import numpy as np
import matplotlib.pyplot as plt


def extractsm(astr):
   """ 
   Extract the semi-major axes from the list of tuples
   and return as a list(sm).
   """
   sm = []
   for (n,a,e,t) in astr:
      sm.append(a)
   return sm
    
def extractecc(astr):
   """ 
   Extract the eccentricities from the list of tuples
   and return as a list(ecc).
   """
   ecc = []
   for (n,a,e,t) in astr:
      ecc.append(e)
   return ecc
    
if __name__ == "__main__":
   """
   This part runs only if astfunctest.py is run 
   from the command line.
   """
   print ('Running astfunctest.py from the command line')
    
   astr = As
   sm = extractsm(astr)
   ecc = extractecc(astr)
   
   fig, axes = plt.subplots()
   axes.plot(sm,ecc, 'r')
   axes.set_xlabel('Semi-Major Axis(AU)')
   axes.set_ylabel('Eccentricity')
   axes.set_title('SMA vs Ecc for 50 Asteroids')
