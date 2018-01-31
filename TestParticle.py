#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:21:56 2018

@author: John
"""


from scipy import *
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from numpy import arange

class TestParticle:
    
    def __init__(self, m, x, y, vx, vy, alpha=None, beta=None):
        
        time=0
        self.t=time
        self.m=m
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.alpha=alpha
        self.beta=beta
        
        
        
    def timestep(self, h):
        
        G=4*pi**2
        
        ax=-self.x*G*self.m/(sqrt(self.x**2+self.y**2)**3)
        ay=-self.y*G*self.m/(sqrt(self.x**2+self.y**2)**3)


        self.vx=self.vx+ax*h
        self.vy=self.vy+ay*h
        
        self.x=self.x+self.vx*h
        self.y=self.y+self.vy*h
        
        
        self.t=self.t+h
        
    def run(self, t, h, animate=False):

        
        self.xlist=[self.x]
        self.ylist=[self.y]

        
        for n in range(int(t/h)):
            self.timestep(h)
            self.xlist.append(self.x)
            self.ylist.append(self.y)
        
        if animate==True:
            fig = plt.figure()
            ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
            ax.set_aspect('equal')
            ax.grid()
            
            ax.plot(0,0, 'ro')
            
            track, = ax.plot([], [],'-')
            pos, = ax.plot([], [],'.')
            posx, posy = [], []
            xtrack, ytrack = [], []
            time_template = 'time = %.3f t_orb'
            time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
            dt=h
            
            def init():
                del xtrack[:]
                del ytrack[:]
                time_text.set_text('')
                return pos, track, time_text
            
            
            def animate(i):
                posx = [self.xlist[i]]
                posy = [self.ylist[i]]
                xtrack.append([self.xlist[i]])
                ytrack.append([self.ylist[i]])
                pos.set_data(posx, posy)
                track.set_data(xtrack, ytrack)
                time_text.set_text(time_template % (i*dt))
                return pos, track, time_text
            
            print(len(self.ylist))
            self.ani = animation.FuncAnimation(fig, animate, arange(1, len(self.ylist), 10),
                                          interval=1, blit=True, init_func=init)
            plt.show
        
        

    
    
test=TestParticle(1, 1, 0, 0, 7)
test.run(10, 0.001, animate=True)


#fig = plt.figure()
#ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
#ax.set_aspect('equal')
#ax.grid()
#
#line, = ax.plot([], [], 'o', lw=2)
#time_template = 'time = %.1fs'
#time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
#dt=0.05
#
#def init():
#    line.set_data([], [])
#    time_text.set_text('')
#    return line, time_text
#
#
#def animate(i):
#    thisx = [0, test.xlist[i]]
#    thisy = [0, test.ylist[i]]
#    print(1)
#    line.set_data(thisx, thisy)
#    time_text.set_text(time_template % (i*dt))
#    return line, time_text
#
#ani = animation.FuncAnimation(fig, animate, arange(1, len(test.ylist)),
#                              interval=25)