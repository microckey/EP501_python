#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:40:51 2020

@author: zettergm

known issues:  
1)  Need to control number of decimal places in output printing to improve readability
"""

import numpy as np
from elimtools import Gauss_elim,backsub

nrow=10
ncol=10
A=np.random.randn(nrow,ncol)
b=np.random.randn(nrow,1)

# Simple test problem for debugging
#A=np.array([[1.0, 4.0, 2.0], [3.0, 2.0, 1.0], [2.0, 1.0, 3.0]])    # system to be solved
#b=np.array([[15.0], [10.0], [13.0]])                               # RHS of system

# Solve with elimtools
[Awork,order]=Gauss_elim(A,b,True)
x=backsub(Awork[order,:],True)
print("Value of x computed via Gaussian elimination and backsubstitution:  ")
print(x)

# Use built-in linear algebra routines to solve and compare
xpyth=np.linalg.solve(A,b);
print("Solution vector computed via built-in numpy routine")
print(xpyth)