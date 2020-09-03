#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 07:02:29 2020

Tests the performance of Gaussian elimination for systems of a variety of sizes

@author: zettergm
"""

# imports
import numpy as np


# define a range of system sizes to investigate
nvals=np.arange(50,550,50)        # note arange excluded the end of the range
testtime=np.zeros(nvals.size)     # time taken for each system size
lrep=5                            # number of times to repeat each step (for consistency)

for n in nvals:
    A=np.random.randn(n,n)
    b=np.random.randn(n,1)
    
    for irep in range(0,lrep):
        