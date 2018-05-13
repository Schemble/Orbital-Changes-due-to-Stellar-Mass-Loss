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
import FYTN03
from scipy.integrate import odeint
import numpy

G=4*pi**2

class TestParticle:
    
    def __init__(self, m=1, x=1, y=0, vx=0, vy=0, x_s=0, y_s=0, alpha=None, beta=None, circular=True):
        
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
        
        self.x_s=x_s
        self.y_s=y_s
        self.alpha=alpha
        if alpha==0:
            self.alpha=None
        self.beta=beta
        self.r=sqrt((self.x-self.x_s)**2+(self.y-self.y_s)**2)
        self.rlist=[self.r]
        if circular==True:       
            self.torb=2*pi*sqrt(self.r**3/(G*m))
            self.vy=sqrt(G*m/self.r)
        self.v=sqrt(self.vx**2+self.vy**2)
        self.vlist=[self.v]
        self.E=self.Etot()
        self.Elist=[self.E]
        self.a=self.GetA()
        self.alist=[self.a]
    
    def Getr(self, x, y):
        return sqrt((x-self.x_s)**2+(y-self.y_s)**2)
    
    
    def timestep(self, h, mloss=0):
        
        G=4*pi**2
        
        ax=-(self.x-self.x_s)*G*self.m/(self.r**3)
        ay=-(self.y-self.y_s)*G*self.m/(self.r**3)

        
        self.vx=self.vx+ax*h
        self.vy=self.vy+ay*h
        self.v=sqrt(self.vx**2+self.vy**2)
        self.vlist.append(self.v)
        
        self.x=self.x+self.vx*h
        self.y=self.y+self.vy*h
        
        self.r=self.Getr(self.x, self.y)
        
        
        self.t+=h
        
        if mloss==True:
            self.m-=self.alpha/(self.beta/h)*self.m_init
        
        return self.t, self.x, self.y, self.m, self.Etot(), self.r
        
    def run(self, h, plot=False, animate=False, mloss=0, un_break=0):

        G=4*pi**2

        
        for n in range(int((self.beta*self.torb)/h)):
            self.timestep(h, mloss=mloss)
            self.xlist.append(self.x)
            self.ylist.append(self.y)
            self.tlist.append(self.t)
            self.mlist.append(self.m)
            self.Elist.append(self.Etot())
            self.rlist.append(self.r)
            if self.Elist[-1]<0:
                self.alist.append(self.GetA())
            if self.Elist[-1]>0 and un_break==1:
                break
        
        if plot==True:
            fig=plt.figure()
            ax=fig.add_subplot(111)
            ax.set_aspect('equal')
            ax.grid()
            plt.xlabel('x [AU]')
            plt.ylabel('y [AU]')
            ax.plot(self.x_s,self.y_s,'ro', self.xlist, self.ylist,'b-')
            fig.savefig('Figures/TestParticle/TP_Trajectory_a={}_b={}.png'.format(self.alpha,self.beta))
            fig.show()
        
        
        
        if animate==True:
            fig = plt.figure()
            ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
            ax.set_aspect('equal')
            ax.grid()
            
            ax.plot(self.x_s, self.y_s,0, 'ro')
            
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
            
        return self.tlist, self.xlist, self.ylist, self.mlist, self.Elist, self.alist
     
#    def oldrunrk4(self):
#        if self.alpha==None:
#            Y=[self.x, self.y, self.vx, self.vy]
#            tol=[0.1, 0.1, 0.1, 0.1]
#        else:
#            Y=[self.x, self.y, self.vx, self.vy, self.m]
#            tol=[0.1, 0.1, 0.1, 0.1, 0.1]
#        #steps=int((self.beta)/h)
#        data, self.tlist = RK4(self.__diff__, Y, 0, self.beta, tol=tol)
#        
#        if data[-1][-1]<0 and self.alpha !=None:
#
#            h=data[-2][-1]*self.beta/(self.alpha*self.m_init)
#            
#            corr=RK4step(self.__diff__, data[-2], h=h)
#            
#            data[-1]=corr[-1]
#            self.tlist[-1]=h
#        if self.alpha!=None:
#            self.mlist=data[:][ -1]
#            self.m=self.mlist[-1]
#        self.xlist=data[:][0]
#        self.ylist=data[:][1]
#
#        self.x=self.xlist[-1]
#        self.y=self.ylist[-1]
#        self.rlist=sqrt(self.xlist**2+self.ylist**2)
#        self.r=self.rlist[-1]
#        self.vx=data[-1][2]
#        self.vy=data[-1][3]
#        self.vlist=list(sqrt(data[:][2]**2+data[:][3]**2))
#        self.v=self.vlist[-1]
#        return self.mlist, self.xlist, self.ylist, self.vlist,  data
    

    
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
        if self.alpha==None:
            return
        self.m-=self.alpha*self.m_init
        if self.m<0:
            self.m=0
    

    def Orbit(self, h, plot=False):
        
        if self.Etot()>0:
           print('Unbound')
           return inf
        
        x_orb=[self.x]
        y_orb=[self.y]
        r_orb=[self.r]
        
        
        theta_i = self.Theta()
        dtheta=0
        dtheta_p=0
        
        while dtheta>=dtheta_p:
            self.timestep(h)
            x_orb.append(self.x)
            y_orb.append(self.y)
            r_orb.append(self.r)
            dtheta_p=dtheta
            dtheta = self.Theta()-theta_i
            if dtheta<0:
                dtheta+=2*pi
            

            
        a=(max(r_orb)+min(r_orb))/2
        e=1-min(r_orb)/a
        
        return x_orb, y_orb, r_orb, a, e
    
    def Theta(self):
        theta = arctan2(self.y-self.y_s, self.x-self.x_s)
        if theta<0:
            theta+=2*pi
        return theta
    
    def GetA(self):
        E=self.Etot()
        if E<0:
            
            return -G*self.m/(2*E)
        else:
            return inf
        
    def GetEc(self):
        L=cross([self.x, self.y, 0], [self.vx, self.vy, 0])
        L2=L[0]**2+L[1]**2+L[2]**2
        #e=sqrt(1+(2*self.Etot()*L2)/(G*self.m)**2)
        e=sqrt(1-L2/(G*self.m*self.GetA()))
        if e < 1:
            return e
        else:
            return e
    
    def __diff__(self, Y0):
        
        if self.alpha==None:
            dx=Y0[2]
            dy=Y0[3]
            dvx=-(Y0[0]-self.x_s)*G*self.m/(((Y0[0]-self.x_s)**2+(Y0[1]-self.y_s)**2)**(3/2))
            dvy=-(Y0[1]-self.y_s)*G*self.m/(((Y0[0]-self.x_s)**2+(Y0[1]-self.y_s)**2)**(3/2))
            return array([dx, dy, dvx, dvy])
        else:
            dm=-self.alpha/(self.beta*self.torb)*self.m_init
            dx=Y0[2]
            dy=Y0[3]
            dvx=-(Y0[0]-self.x_s)*G*Y0[-1]/(((Y0[0]-self.x_s)**2+(Y0[1]-self.y_s)**2)**(3/2))
            dvy=-(Y0[1]-self.y_s)*G*Y0[-1]/(((Y0[0]-self.x_s)**2+(Y0[1]-self.y_s)**2)**(3/2))
            return array([dx, dy, dvx, dvy, dm])
        
    def RK4step(self, f, y0, h):
        '''
        f = differential equation(s)
        y0 = starting value(s)
        t0 = start time
        tf = stop time
        tol = tolerance
        '''
        
        if type(y0) is list:
            
            y0=array(y0)
        
        
        if type(y0) is numpy.ndarray:
            
            ylen=len(y0)
                    
            Y=array([ ylen*[0] for i in range(2) ], dtype=numpy.float)
            Y[0]=y0
    
            k1=h*f(Y[0])
            k2=h*f(Y[0]+k1/2)
            k3=h*f(Y[0]+k2/2)
            k4=h*f(Y[0]+k3)
            Y[1]=(Y[0]+k1/6+k2/3+k3/3+k4/6)
        
    
        else:
            TypeError('y0 must be a list, array, integer or float')
        
        return Y

    def runrk4(self, orbit=False, ubbreak=0):
        
        if self.alpha==None and self.beta==0 and orbit==False:
            return
        
        if (self.beta==None or self.beta==0) and orbit==False:
            self.InstMLoss()
            return
        
        if orbit==True:
            beta_i=self.beta
            self.beta=float('inf')
            alpha_i=self.alpha
            self.alpha=None
        if self.alpha==None:
            Y=array([self.x, self.y, self.vx, self.vy])
            tol=[0.1, 0.1, 0.1, 0.1]
            dtheta=0
            dtheta_p=0
        else:
            Y=array([self.x, self.y, self.vx, self.vy, self.m])
            tol=[0.1, 0.1, 0.1, 0.1, 0.1]
            
        t=self.t
        tf=self.beta
        h=0.0001
        S=1
        theta_i=self.Theta()
        while t<self.beta:
            y=[]
            
            for h0 in [h, h/2]:
                y.append(self.RK4step(self.__diff__, Y, h0)[-1])
            
            diff=abs(y[0]-y[1])

            if any(diff > tol):
                
                h *= S*min(tol/diff)**(1/5)
                if t+h>tf:
                    h=tf-t
                
            
                #print(shape(Y), shape(Y[i-1]+k1/6+k2/3+k3/3+k4/6))
                
                Y=self.RK4step(self.__diff__, Y, h)[-1]
                
                t+=h
                
                
            else:
                
                t+=h
                
                
                Y=y[0]
                h *= S*min(tol/diff)**(1/5)
                if t+h>tf:
                    h=tf-t
            
            self.t=t
            self.tlist.append(self.t)
            self.x=Y[0]
            self.xlist.append(self.x)
            self.y=Y[1]
            self.ylist.append(self.y)
            self.vx=Y[2]
            self.r=sqrt(self.x**2+self.y**2)
            self.rlist.append(self.r)
            self.vy=Y[3]
            self.v=sqrt(self.vx**2+self.vy**2)
            self.vlist.append(self.v)
            self.theta=self.Theta()
            if self.alpha != None:
                self.m=Y[4]
                self.mlist.append(self.m)
            if ubbreak== True and self.Unbound()==True:
                break
            if orbit==True:
                dtheta_p=dtheta
                dtheta = self.Theta()-theta_i
                if dtheta<0:
                    dtheta+=2*pi
            
                if dtheta<=dtheta_p:
                    self.beta=beta_i
                    self.alpha=alpha_i
                    break
def RK4(f, y0, t0, tf, tol):
    '''
    f = differential equation(s)
    y0 = starting value(s)
    t0 = start time
    tf = stop time
    tol = tolerance
    '''
    
    
    
    h=0.001
    
    if type(y0) is list:
        
        y0=array(y0)
    
    
    if type(y0) is numpy.ndarray:
        
        ylen=len(y0)
                
        Y=[]
        
        Y.append(y0)
        
        t=t0
        tlist=[t]
        i=1
        S=1
        while t<tf:
            y=[]
            
            for h0 in [h, h/2]:
                k1=h0*f(Y[i-1])
                k2=h0*f(Y[i-1]+k1/2)
                k3=h0*f(Y[i-1]+k2/2)
                k4=h0*f(Y[i-1]+k3)
                y.append(Y[i-1]+k1/6+k2/3+k3/3+k4/6)
            
            diff=abs(y[0]-y[1])
            #print(diff)
            if any(diff > tol):
                
                h = S*min(tol/diff)**(1/5)*h
                if t+h>tf:
                    h=tf-t
                k1=h*f(Y[i-1])
                k2=h*f(Y[i-1]+k1/2)
                k3=h*f(Y[i-1]+k2/2)
                k4=h*f(Y[i-1]+k3)
            
                #print(shape(Y), shape(Y[i-1]+k1/6+k2/3+k3/3+k4/6))
                
                Y.append(Y[i-1]+k1/6+k2/3+k3/3+k4/6)
                
                t+=h
                tlist.append(t)
                
            else:
                
                t+=h
                tlist.append(t)
                
                Y.append(y[0])
                if t+h>tf:
                    h=tf-t
                h *= S*min(tol/diff)**(1/4)
            i+=1

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
    
    return Y, tlist

