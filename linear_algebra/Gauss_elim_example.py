#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:40:51 2020

@author: zettergm
"""

import numpy as np
#from elimtools import Gauss_elim,backsub
import elimtools

#nrow=4
#ncol=4
#A=np.random.randn(nrow,ncol)
#b=np.random.randn(nrow,1)

# Define test problem
A=np.array([[1.0, 4.0, 2.0], [3.0, 2.0, 1.0], [2.0, 1.0, 3.0]])    # system to be solved
b=np.array([[15.0], [10.0], [13.0]])                               # RHS of system

Awork=elimtools.Gauss_elim(A,b)
x=elimtools.backsub(Awork)
print("Final value of x:  ")
print(x)