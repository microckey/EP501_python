#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 06:50:02 2020

Module containing functions for iterative solutions of linear systems

@author: zettergm
"""

import numpy as np
import warnings


# Perform Jacobi iteration
def Jacobi(x0,A,b,tol,verbose):
    # get set up for iterations
    maxit=100
    x=np.copy(x0)            # initial guess, note use of copy to avoid overwriting input
    difftot=tol+1e3          # to insure we enter iterations
    [n,_]=A.shape            # system size, note use of python "throwaway" variable _
    residual=10*np.ones(n)   # residual, initialize to be large enough so that main loops triggers
    if (verbose):
        print("System size:  ")
        print(n)
        print("Matrix:  ")
        print(A)
        print("RHS:  ")
        print(b)
    
    it=1
    while (difftot>tol and it<maxit):
        # save previous iteration values
        difftotprev=difftot
        residualprev=np.copy(residual)        # note use of copy...
        xprev=np.copy(x)
        for i in range(0,n):
            residual[i]=b[i]
            for j in range(0,n):
                #print(i,j,residual[i],residualprev[i])
                residual[i]=residual[i]-A[i,j]*xprev[j]
            x[i]=xprev[i]+residual[i]/A[i,i]
        difftot=np.sum(np.abs(residual-residualprev))
        
        if (verbose):
            print("x=")
            print(x)
            print("it=")
            print(it)
            print("difftot=")
            print(difftot)
            print("residual=")
            print(residual)
            print("residualprev=")
            print(residualprev)

        if (difftot>difftotprev and it>2):
            warnings.warn("Solution seems to be diverging; check diagonal dominance...")
            
        it=it+1
    
    nit=it-1
    if (nit>=maxit):
        warnings.warn("Max iterations used; convergence not achieved")
        
    return [x,nit]
