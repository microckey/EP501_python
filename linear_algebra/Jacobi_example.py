#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 07:29:12 2020

Illustrate the use of Jacobi iteration to solve a linear system

@author: zettergm
"""

import numpy as np
from ittools import Jacobi


# Create a sparse, diagonally dominant system (similar to FDE for BVP)
n=10
a0=-1*np.ones(n-1)
a1=4*np.ones(n)
a2=-1*np.ones(n-1)
A=np.diag(a1)
A=np.diag(a0,-1)+np.diag(a1,0)+np.diag(a2,1)

# Jacobi iterations
x0=np.random.randn(n,1)
#x0=10*np.ones((n,1))    # "bad" initial guess to show effects on convergence
b=np.ones((n,1))
tol=1e-2
print("Verbose Jacobi iteration solution")
print("---------------------------------------------------------------------")
[x,iteration]=Jacobi(x0,A,b,tol,False)
print("---------------------------------------------------------------------")
print("Iterative solution")
print(x)
print("Number of iterations required and tolerance")
print(iteration)
print(tol)
print("Built-in python solution")
xpyth=np.linalg.solve(A,b)
print(xpyth)
print("Residual:  ")
print(x-xpyth)