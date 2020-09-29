#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 07:18:17 2020

Demonstrates interval halving as a method for root finding

@author: zettergm
"""


# Imports
import numpy as np
from nonlinear_fns import fun3
import matplotlib.pyplot as plt


# Setup for iterations for a closed domain method
maxit=100
minx=0
maxx=2*np.pi
tol=1e-6
verbose=True


# Initial interval spec
a0=np.pi/4
b0=np.pi
a=a0
b=b0


# Interval halving iterations
it=1
converged=False
while(!converged and it<=maxit):
    c=(a+b)/2.0
    aprev=a
    bprev=b
    if (fun3(a)*fun3(b)<0):    # we crossed zero so root is in this interval
        b=c
        left=True
    else:
        a=c
        left=False
    xnew=c
    fval=fun3(xnew)
    converged=abs(fval)<tol
    
    if (verbose):
        fig1=plt.figure
        plt.clf
        