#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 06:55:11 2020

@author: zettergm
"""

import numpy as np


def fun1D(x,A,x0,sigma):
    fval=A*np.exp(-(x-x0)**2/2/sigma)
    return fval


def fun2D(X,Y,A,x0,y0,sigmax,sigmay):
    fval=A*np.exp(-(X-x0)**2/2/sigmax)*np.exp(-(Y-y0)**2/2/sigmay)
    return fval