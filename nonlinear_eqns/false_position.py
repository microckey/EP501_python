#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 06:45:05 2020

Illustrates the false position method for root finding

@author: zettergm
"""


# Imports
import numpy as np
from nonlinear_fns import fun1 as f1
import matplotlib.pyplot as plt


# Setup for iterations for a closed domain method
maxit=100
minx=0
maxx=2*np.pi
tol=1e-3
verbose=True


# Function we are finding roots of
x=np.linspace(minx,maxx,50)
y=f1(x)


# Initial interval spec
a0=np.pi/4
b0=np.pi
a=a0
b=b0


# Interval halving iterations
it=1
converged=False
while(not (converged) and (it<=maxit)):
    c=(a+b)/2.0
    
    c=a-f1(a)/( (f1(b)-f1(a))/(b-a) )
    
    aprev=a
    bprev=b
    if (f1(a)*f1(c)<0.0):    # we crossed zero so root is in this interval
        b=c
        left=True
    else:
        a=c
        left=False
    xnew=c
    fval=f1(xnew)
    converged=abs(fval)<tol
    it=it+1
    if (verbose):
        plt.figure(num=1)
        plt.clf
        plt.plot(x,y)
        plt.axis([a0,b0,-1,1])
        if (left):
            plt.plot(aprev,0,"k^")
            plt.plot(bprev,0,"r^")
        else:
            plt.plot(aprev,0,"r^")
            plt.plot(bprev,0,"k^")            
        plt.plot(c,0,"ko")
        yline=(f1(bprev)-f1(aprev))/(bprev-aprev)*(x-aprev)+f1(aprev);    # line approximation
        plt.plot(x,yline,"--")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("x = %f" % (xnew))
        plt.show()
        _=input("Press the enter key to continue...")
if (it==maxit):
    print("WARNING:  max number of iterations used; proceed with caution...")
print("Root value through interval halving:  ",xnew)
print("Number of iterations used:  ",it-1)
