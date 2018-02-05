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
        
        
    def timestep(self, h, m_loss=True):
        
        G=4*pi**2
        
        ax=-self.x*G*self.m/(sqrt(self.x**2+self.y**2)**3)
        ay=-self.y*G*self.m/(sqrt(self.x**2+self.y**2)**3)


        self.vx=self.vx+ax*h
        self.vy=self.vy+ay*h
        self.v=sqrt(self.vx**2+self.vy**2)
        self.vlist.append(self.v)
        
        self.x=self.x+self.vx*h
        self.y=self.y+self.vy*h
        
        self.r=sqrt(self.x**2+self.y**2)
        self.rlist.append(self.r)
        
        self.tlist.append(self.t+h)
        
        if m_loss==True:
            self.m-=self.alpha/(self.beta/h)*self.m_init
        
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
            fig.savefig('Figures/TestParticle/TP_Trajectory_a={}_b={}.png'.format(self.alpha,self.beta))
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
        if self.Etot() <= 0:
            return True
        else:
            return False
    
    def Etot(self):
        G=4*pi**2      
        return 1/2*self.v**2-G*self.m/self.r
    
    def InstMLoss(self):
        self.m-=self.alpha*self.m
        
    def Orbit(self, h):
        
        x_orb=[self.x]
        y_orb=[self.y]
        
        theta = arctan2(self.y, self.x)
        if theta<0:
            theta+=2*pi
        
        theta_p=theta
        
        while theta>=theta_p:
            self.timestep(h, m_loss=0)
            x_orb.append(self.x)
            y_orb.append(self.y)
            theta_p=theta
            theta = arctan2(self.y, self.x)
            if theta<0:
                theta+=2*pi
                    
        fig=plt.figure()
        ax=fig.add_subplot(111)
        ax.set_aspect('equal')
        ax.grid()
        plt.xlabel('x [AU]')
        plt.ylabel('y [AU]')
        ax.plot(0,0,'ro', x_orb, y_orb,'b-')
        fig.savefig('Figures/TestParticle/TP_orbit_a={}_b={}.png'.format(self.alpha,self.beta))
        fig.show()
    


