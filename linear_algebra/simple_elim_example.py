#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:57:16 2020

@author: zettergm
"""

# Imports
import numpy as np
import math as ma


# Illustrate number of operations required to execute Cramer's Rule directly
lN=10;
numops=np.zeros(lN)
for i in range(0,lN):
     numops[i]=(i)*ma.factorial(i+2)+i+1;
print(numops)


# Define test problem
A=np.array([[1.0, 4.0, 2.0], [3.0, 2.0, 1.0], [2.0, 1.0, 3.0]])    # system to be solved
b=np.array([[15.0], [10.0], [13.0]])                   # RHS of system
Awork=np.concatenate((A,b),axis=1)               # composite work array/matrix; will be overwritten
print("Initial state of work matrix")
print(Awork)


# Simple Elimination example (no pivoting or scaling)
[nrow,ncol]=A.shape
for i in range(0,nrow-1):            # row being used for elimination, note latter argument of range is number of iterations
    pivel=Awork[i,i]                 # pivot element
    for j in range(i+1,nrow):        # row we are eliminating from
        elimel=Awork[j,i]                 # lead factor to be eliminated
        for k in range(i,ncol+1):    # column elements, make sure to interate into the solution vector
            Awork[j,k]=Awork[j,k]-elimel/pivel*Awork[i,k]
            print("Present iteration of elimination",i,j,k)
            print(pivel)
            print(elimel)
            print(Awork)


# Backsubstitution example
x=np.copy(Awork[:,-1]);
print("Initial value of solution vector")
print(x)

for i in range(nrow-1,-1,-1):
    denom=Awork[i,i]
    x[i]=x[i]/denom
    for j in range(i+1,ncol):
         x[i]=x[i]-Awork[i,j]/denom*x[j]
         print("Present value of solution vector",i,j)
         print(x)


# Use built-in mathematical library from numpy to solve the same problem
xpyth=np.linalg.solve(A,b);
print("Solution vector computed via built-in numpy routine")
print(xpyth)

