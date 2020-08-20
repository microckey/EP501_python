#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:36:20 2020

@author: zettergm
"""

import numpy as np
import sys


# Perform Gaussian elimination
def Gauss_elim(A,b,verbose):

    # system size and error checking
    [nrow,ncol]=A.shape
    if (nrow == ncol):
        n=nrow
    else:
        sys.exit("Matrix to be solved must be square")
    
    # create the work array for elimination
    Awork=np.concatenate((A,b),axis=1)               # composite work array/matrix; will be overwritten
    if (verbose):
        print("Initial state of work matrix")
        print(Awork)
        
    # ordering array for pivoting and scaling
    # order=np.arange(0,n,1)
    # print (order)
        
    # Simple Elimination example (no pivoting or scaling)
    for i in range(0,n-1):            # row being used for elimination, note latter argument of range is number of iterations
        pivel=Awork[i,i]                 # pivot element
        for j in range(i+1,n):        # row we are eliminating from
            elimel=Awork[j,i]                 # lead factor to be eliminated
            Awork[j,i]=0                      # forcing this to zero avoid precision issues
            for k in range(i+1,n+1):    # column elements, make sure to interate into the solution vector
                Awork[j,k]=Awork[j,k]-elimel/pivel*Awork[i,k]
                if (verbose):
                    print("Present iteration of elimination",i,j,k)
                    print(pivel)
                    print(elimel)
                    print(Awork)
                
    return [Awork,order]
                

# execute backsubstitution
def backsub(Awork,verbose):
        
    [nrow,ncol1]=Awork.shape
    x=np.copy(Awork[:,-1]);
    if (verbose):
        print("Initial value of solution vector")
        print(x)
    
    for i in range(nrow-1,-1,-1):
        denom=Awork[i,i]
        x[i]=x[i]/denom
        for j in range(i+1,ncol1-1):
             x[i]=x[i]-Awork[i,j]/denom*x[j]
             if (verbose):
                 print("Present value of solution vector",i,j)
                 print(x)
    return x
             
    