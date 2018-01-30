#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:21:56 2018

@author: John
"""


from scipy import *
from matplotlib import pyplot as plt

class TestParticle:
    
    def __init__(self, m, x, y, vx, vy, alpha=None, beta=None):
        
        time=0
        self.t=time
        self.m=m
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        #self.mloss=mloss
        #self.losst=losst
        
        
    def timestep(self, h):
        
        G=4*pi**2
        
        ax=-self.x*G*self.m/(sqrt(self.x**2+self.y**2)**3)
        ay=-self.y*G*self.m/(sqrt(self.x**2+self.y**2)**3)


        self.vx=self.vx+ax*h
        self.vy=self.vy+ay*h
        
        self.x=self.x+self.vx*h
        self.y=self.y+self.vy*h
        
        
        self.t=self.t+h
        
    def run(self, t, h):
        
        xlist=[self.x]
        ylist=[self.y]
        
        for n in range(int(t/h)):
            self.timestep(h)
            xlist.append(self.x)
            ylist.append(self.y)
#            if self.losst!=None and self.t<self.losst or self.losst==None:
#                self.m=self.m-self.m*self.mloss/(t/h)
        plt.figure()
        plt.plot(xlist, ylist, 0,0,'o')
        plt.axis('equal')
        plt.show()
        


test=TestParticle(1, 1, 0, 0, 2*pi)
test.run(10, 0.001)


