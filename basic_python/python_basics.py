#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 06:45:58 2020

A script to illustrate some basic plotting and matrix operations in Python

@author: zettergm
"""

import numpy as np
from funexamples import fun1D,fun2D


# Define some variable so we can plot things
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
[X,Y]=np.meshgrid(x,y)


# Example function evaluations to plot
y1=fun1D(x,1,1,3)
y2=fun1D(x,1.5,-1,2)
Z1=fun2D(X,Y,2,0,0,3,4)
Z2=fun2D(X,Y,5,2,-2,2,2)


# this matrix and vector represent the system of equations:
# 1)   x +  2y +  4z = 18
# 2)  2x + 12y -  2z =  9
# 3)  5x + 26y +  5z = 14
A=np.array([[1, 2, 4],[2, 12, -2],[5,26,5]])      #matrix of coefficients
b=np.array([[18], [9], [14]])                     #this is the column vector representing the RHS of the system

B=A';               %transpose of A


# Some basic commands to display variables
print("A = ");
print(A);

print("b = ");
print(b);

# Compute some matrix properties and print them
disp('det(A) = ');
disp(det(A));

disp('trace(A) = ');
disp(trace(A));

disp('condition # of A = ');
disp(cond(A));

disp('transpose(A) = ');
disp(B);

disp('Aii (diagonal elements of A) = ');
disp(diag(A));

%matrix functions
disp('A*B (matrix multiplication) = ');
disp(A*B);

disp('Aij*Bij (scalar multiplication) = ');
disp(A.*B);

disp('5*A (multiplication) = ');
disp(5*A);

disp('Solution (x) of the system A*x=b:  ');
disp('x = ');
xvec=A\b;
disp(xvec);

disp('I (3x3 identity matrix) = ');
disp(eye(3));

disp('A^{-1} (inverse of A) = ')
disp(A\eye(3));                    %this is preferred over inv(A) (see matlab documentation)

%slicing and concatenation of array/matrices
disp('2nd row of A = ');
disp(A(2,:));

disp('2nd column of A = ');
disp(A(:,2));

disp('flat list (column vector) of matrix elements of A:  ')
disp(A(:));

disp('[A|A] (horizontal concatenation of A with itself):  ')
disp(cat(2,A,A));

disp('Vertical concatenation of A with itself:  ')
disp(cat(1,A,A));

disp('diagonal matrix:  ');
a1=10:-1:1;                        %count backward
a1=a1(:);                          %convert to column vector
disp(diag(a1,0));

disp('LU decomposition of A (A=L*U):  ')
[L,U]=lu(A);
disp('L = ');
disp(L);
disp('U = ');
disp(U);

disp('Eigenvalues of A = ');
[psi,lambda]=eig(A);
disp(lambda);
disp('Eigenvectors of A = ');
disp(psi(:,1));
disp(psi(:,2));
disp(psi(:,3));