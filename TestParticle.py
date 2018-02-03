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
    
    def __init__(self, m, x, y=0, vx=0, vy=0, alpha=None, beta=None, circular=False):
        
        G=4*pi**2
        
        time=0
        self.t=time
        self.tlist=[time]
        self.m=m
        self.m_init=m
        self.mlist=[m]
        self.x=x
        self.xlist=[x]
        self.y=y
        self.ylist=[y]
        self.vx=vx
        self.vy=vy
        self.v=sqrt(self.vx**2+self.vy**2)
        self.vlist=[self.v]
        self.alpha=alpha
        self.beta=beta
        self.r=sqrt(self.x**2+self.y**2)
        self.rlist=[self.r]
        if circular==True:       
            self.torb=2*pi*sqrt(self.r**3/(G*m))
            self.vy=sqrt(G*m/self.r)
        self.v=sqrt(self.vx**2+self.vy**2)
        
        
    def timestep(self, h):
        
        G=4*pi**2
        
        ax=-self.x*G*self.m/(sqrt(self.x**2+self.y**2)**3)
        ay=-self.y*G*self.m/(sqrt(self.x**2+self.y**2)**3)


        self.vx=self.vx+ax*h
        self.vy=self.vy+ay*h
        self.v=sqrt(self.vx**2+self.vy**2)
        self.vlist.append(self.v)
        
        self.x=self.x+self.vx*h
        self.y=self.y+self.vy*h
        
        self.m-=self.alpha/(self.beta/h)*self.m_init
        self.r=sqrt(self.x**2+self.y**2)
        self.rlist.append(self.r)
        
        self.tlist.append(self.t+h)
        
    def run(self, h, plot=False, animate=False):

        G=4*pi**2

        
        for n in range(int((self.beta*self.torb)/h)):
            self.timestep(h)
            self.xlist.append(self.x)
            self.ylist.append(self.y)

        
        if plot==True:
            fig=plt.figure()
            ax=fig.add_subplot(111)
            ax.set_aspect('equal')
            ax.grid()
            plt.xlabel('x [AU]')
            plt.ylabel('y [AU]')
            ax.plot(0,0,'ro', self.xlist, self.ylist,'b-')
            fig.savefig('Figures/TestParticle/TP_Orbit_a={}_b={}.png'.format(self.alpha,self.beta))
            fig.show()
        
        
        
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
                return track, pos, time_text
            
            
            def animate(i):
                posx = [self.xlist[i]]
                posy = [self.ylist[i]]
                xtrack.append([self.xlist[i]])
                ytrack.append([self.ylist[i]])
                pos.set_data(posx, posy)
                track.set_data(xtrack, ytrack)
                time_text.set_text(time_template % (i*dt))
                return track, pos, time_text
        
            self.ani = animation.FuncAnimation(fig, animate, arange(1, len(self.ylist), 10),
                                          interval=1, blit=True, init_func=init)
            
    def Bound(self):
        G=4*pi**2
        if 1/2*self.v**2-G*self.m/self.r <= 0:
            return True
        else:
            return False
    
    def InstMLoss(self):
        self.m-=self.alpha*self.m
        
    def Orbit(self):
        
            
            
            
        
m=1
x=1
test=TestParticle(m, x, alpha=0.6, beta=0, circular=True)
#test.run(0.0001,plot=1, animate=0)
test.InstMLoss()
print(test.Bound())
#plt.figure()
#plt.plot(test.t, test.r)
##plt.ylim(ymax=2, ymin=-2)
#plt.ylabel('Orbital Radius [AU]')
#plt.xlabel('Time [yr]')
#plt.show