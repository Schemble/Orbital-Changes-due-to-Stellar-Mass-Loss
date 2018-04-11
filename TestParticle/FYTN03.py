#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:34:35 2017

@author: John
"""
from scipy import*
import numpy

''' 
This is a compilation of methods used in the course 'Computational Physics, 
FYTN03'. The course is divided into three modules, each with its own focus.
'''

'''
Module A
'''

class ModuleA:
    '''
    In this module the main focus is on ordinary differential equations and 
    integration. The two methods to solve ODE are Euler's method and the second
    order Runge-Kutta Method. ...
    '''
    def Euler(f, y0, t0, tf, steps):
        '''
        f = differential equation(s).
        y0= starting value(s).
        t0 = start time.
        tf = stop time.
        steps = number of steps.
        '''
        
        h=(tf-t0)/steps
        
        if type(y0) is list:
            
            y0=array(y0)
        
        
        if type(y0) is numpy.ndarray:
            
            ylen=len(y0)
                    
            Y=array([ ylen*[0] for i in range(steps) ], dtype=numpy.float)
            
            Y[0]=y0
            
            for i in range(1, steps):
                
                Y[i]=Y[i-1]+h*f(Y[i-1])
                
        
        elif type(y0) is float or int:
            
            Y=zeros(steps)
            
            Y[0]=y0
            
            for i in range(1, steps):
                
                Y[i]=Y[i-1]+h*f(Y[i-1])
        
        else:
            TypeError('y0 must be a list, array, integer or float')
        
        return Y
    
    def RK2(f, y0, t0, tf, steps, a=0):
        '''
        f = differential equation(s)
        y0 = starting value(s)
        t0 = start time
        tf = stop time
        steps= number of steps
        a = first RK constant
        '''
        
        # Make the RK constants
        b=1-a
        m=1/(2*b)
        
        #
        h=(tf-t0)/steps
        
        if type(y0) is list:
            
            y0=array(y0)
        
        
        if type(y0) is numpy.ndarray:
            
            ylen=len(y0)
                    
            Y=array([ ylen*[0] for i in range(steps) ], dtype=numpy.float)
            
            Y[0]=y0
            
            for i in range(1, steps):
                
                k1=h*f(Y[i-1])
                k2=h*f(Y[i-1]+m*k1)
                Y[i]=Y[i-1]+a*k1+b*k2
                
        
        elif type(y0) is float or int:
            
            Y=zeros(steps)
            
            Y[0]=y0
            
            for i in range(1, steps):
                
                Y[i]=Y[i-1]+h*f(Y[i-1])
        
        else:
            TypeError('y0 must be a list, array, integer or float')
        
        return Y
    
    def RK4(f, y0, t0, tf, steps):
        '''
        f = differential equation(s)
        y0 = starting value(s)
        t0 = start time
        tf = stop time
        steps= number of steps
        '''
        
        
        
        h=(tf-t0)/steps
        
        if type(y0) is list:
            
            y0=array(y0)
        
        
        if type(y0) is numpy.ndarray:
            
            ylen=len(y0)
                    
            Y=array([ ylen*[0] for i in range(steps) ], dtype=numpy.float)
            
            Y[0]=y0
            
            for i in range(1, steps):
                
                k1=h*f(Y[i-1])
                k2=h*f(Y[i-1]+k1/2)
                k3=h*f(Y[i-1]+k2/2)
                k4=h*f(Y[i-1]+k3)
                Y[i]=Y[i-1]+k1/6+k2/3+k3/3+k4/6
                
        
#        elif type(y0) is float or int:
#            
#            Y=zeros(steps)
#            
#            Y[0]=y0
#            
#            for i in range(1, steps):
#                
#                Y[i]=Y[i-1]+h*f(Y[i-1])
        
        else:
            TypeError('y0 must be a list, array, integer or float')
        
        return Y