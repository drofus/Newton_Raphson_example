#!/usr/bin/env python
#-*-coding: utf-8-*-

import numpy as np

def f(x):
    return (x**2.)+3*x

def df(x):
    return (2*x) + 3

def dx(f,x):
    return abs(0-f(x))

def newtonR(f,df,x0,tol,Nmax=500):
    
    p = dx(f,x0)
    
    n = 0
    while True:
        
        x0 = x0 - (f(x0))/(df(x0))
        #p = dx(f,x0)
        if n > Nmax:
            print ("Nmax iter max reached")
            break
        n += 1
        if abs(f(x0)) < tol:
            break
    
    return x0

print(newtonR(f,df,3/4.,1e-4))
