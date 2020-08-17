#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:57:16 2020

@author: zettergm
"""

# Imports
import numpy as np


# Define test problem
A=np.array([[1, 4, 2], [3, 2, 1], [2, 1, 3]])    # system to be solved
b=np.array([[15], [10], [13]])                   # RHS of system
Awork=np.concatenate((A,b),axis=1)               # composite work array/matrix; will be overwritten
print("Initial state of work matrix")
print(Awork)


# Simple Elimination (no pivoting or scaling)
[nrow,ncol]=A.shape
for i in range(0,nrow-1):            # row being used for elimination
    for j in range(i+1,nrow-1):      # row we are eliminating from
        pivel=Awork[i,i]           # pivot element
        Awork[j,i]=0             # factor being eliminated
        for k in range(i+1,ncol):    # column elements, make sure to interate into the solution vector
            Awork[j,k]=Awork[j,k]-Awork[j,k]/pivel*Awork[i,k]
            print("Present iteration of elimination")
            print(Awork)


print("Final state of work matrix")
print(Awork)
