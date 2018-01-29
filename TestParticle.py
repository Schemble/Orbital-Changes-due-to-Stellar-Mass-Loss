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


class BinaryOrbits:
    
    def __init__(self, m1, x1, y1, vx1, vy1, m2, x2, y2, vx2, vy2):
        self.m1=m1
        self.x1=x1
        self.y1=y1
        self.vx1=vx1
        self.vy1=vy1
        self.m2=m2
        self.x2=x2
        self.y2=y2
        self.vx2=vx2
        self.vy2=vy2
        
        G=4*pi**2
        
        self.vy1=sqrt(G*(m1+m2)/2)
        self.vy2=-sqrt(G*(m1+m2)/2)
        print(self.vy1,self.vy2)
        
        
    def timestep(self, h=0.01):
        G=1
        G=6.67260e-11   #[Nm^2/kg^2]
        G=4*pi**2       #[Au^3yr^-2M_sol-1]
            
            
        ax1=-self.x1*G*self.m2/(sqrt(self.x1**2+self.y1**2)+sqrt(self.x2**2+self.y2**2))**3
        ay1=-self.y1*G*self.m2/(sqrt(self.x1**2+self.y1**2)+sqrt(self.x2**2+self.y2**2))**3
        ax2=-self.x2*G*self.m1/(sqrt(self.x1**2+self.y1**2)+sqrt(self.x2**2+self.y2**2))**3
        ay2=-self.y2*G*self.m1/(sqrt(self.x1**2+self.y1**2)+sqrt(self.x2**2+self.y2**2))**3
        print(sqrt(self.x1**2+self.y1**2)+sqrt(self.x2**2+self.y2**2))
#        ax1=-self.x1*G*self.m2/(sqrt(abs(self.x1-self.x2)**2+abs(self.y1-self.y2)**2))**3
#        ay1=-self.y1*G*self.m2/(sqrt(abs(self.x1-self.x2)**2+abs(self.y1-self.y2)**2))**3
#        ax2=-self.x2*G*self.m1/(sqrt(abs(self.x1-self.x2)**2+abs(self.y1-self.y2)**2))**3
#        ay2=-self.y2*G*self.m1/(sqrt(abs(self.x1-self.x2)**2+abs(self.y1-self.y2)**2))**3
        
        self.vx1=self.vx1+ax1*h
        self.vy1=self.vy1+ay1*h
        self.vx2=self.vx2+ax2*h
        self.vy2=self.vy2+ay2*h
      
        self.x1=self.x1+self.vx1*h
        self.y1=self.y1+self.vy1*h
        self.x2=self.x2+self.vx2*h
        self.y2=self.y2+self.vy2*h
        

#test=BinaryOrbits(1, 1, 0, 0, 2.23365, 1, -1, 0, 0, -2.23365)
#x1_list=[test.x1]
#y1_list=[test.y1]
#x2_list=[test.x2]
#y2_list=[test.y2]
#for i in range(100):
#    test.timestep()
#    x1_list.append(test.x1)
#    y1_list.append(test.y1)
#    x2_list.append(test.x2)
#    y2_list.append(test.y2)
#    
#plt.figure()
#plt.plot(x1_list, y1_list,'.', x2_list, y2_list, '.')
#plt.axis('equal')
#plt.show