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
    x=x0                     # initial guess
    difftot=tol+1e3          # to insure we enter iterations
    [n,_]=A.shape()          # system size, note use of throwaway variable _
    residual=10*np.ones((n,1))   # residual
    
    it=1
    while (difftot<tol & it<maxit):
        # save previous iteration values
        difftotprev=difftot
        residualprev=residual
        xprev=x
        for i in range(0,n):
            residual[i]=b[i]
            for j in range(0,n):
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

        if (difftot>difftotprev & it>2):
            warnings.warn("Solution seems to be diverged; check diagonal dominance...")
            
        it=it+1
    
    nit=it-1
    if (nit>=maxit):
        warnings.warn("Max iterations used; convergence not achieved")
        
    return [x,nit]
