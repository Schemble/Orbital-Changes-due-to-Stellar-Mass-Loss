#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:05:49 2018

@author: John
"""

import TestParticle as TP
from scipy import*
from matplotlib import pyplot as plt


alpha=array([0.1, 0.2, 0.3, 0.4])
x=1
m=1
alist=[]
G=4*pi**2

def analytical(alpha, e=0):
        return (alpha-1)*(1-e)/(2*alpha-1+e)


#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.set_aspect('equal')
#ax.grid()
#plt.xlabel('x [AU]')
#plt.ylabel('y [AU]')
#for alph in alpha:
#    ex=TP.TestParticle(m, x, circular=1, alpha=alph)
#    iorb_x, iorb_y = ex.Orbit(0.001)
#    ex.InstMLoss()
#    orb_x, orb_y= ex.Orbit(0.001)
#    a=max((max(orb_x)+abs(min(orb_x)))/2, (max(orb_y)+abs(min(orb_y)))/2)
#    alist.append(a)
#
#    plt.plot(orb_x, orb_y, label=r'$\alpha={}, a/a_0={:.3f}$'.format(alph, a))
#    
#plt.plot(iorb_x, iorb_y, label='Initial Orbit')
#plt.title(r'$\beta=0$')
#plt.legend()
##plt.savefig('TP_a_vs_alph.png')
#plt.close()
#
#print(analytical(alpha))
        
    
#a_init=1
#x=arange(0.5, 0.9, 0.1)
#for x in x:
#    v=sqrt(G*m*(2/x-1/a_init))
#    e0=(a_init-x)/a_init
#    
#    alpha=arange(0.1, (1-e0)/2, 0.1)
#    
#    fig=plt.figure()
#    ax=fig.add_subplot(111)
#    ax.set_aspect('equal')
#    ax.grid()
#    plt.xlabel('x [AU]')
#    plt.ylabel('y [AU]')
#    for alph in alpha:
#        ex=TP.TestParticle(m, x, vy=v, alpha=alph)
#        iorb_x, iorb_y = ex.Orbit(0.001)
#        ex.InstMLoss()
#        xlist, ylist= ex.Orbit(0.001)
#        a=max((max(xlist)+abs(min(xlist)))/2, (max(ylist)+abs(min(ylist)))/2)
#        alist.append(a)
#        plt.plot(xlist, ylist, label=r'$\alpha={:.2}, a/a_0={:.3f}$'.format(alph, a))
#        print(a, analytical(alph, e0))
#    plt.plot(iorb_x, iorb_y, label='Initial Orbit')
#    plt.title(r'$\beta=0, e_0={:.2f}$'.format(e0))
#    plt.legend()
#    plt.savefig('TP_a_vs_alph_e0={}.png'.format(e0))
#    plt.show()
    
    
    
a_init=1
x_list=arange(0.5, 1.01, 0.1)
x_list[-1]=1

fig=plt.figure()
ax=fig.add_subplot(111)
ax.grid()
plt.xlabel(r'$\alpha$')
plt.ylabel('a[AU]')

for x in x_list:
    v=sqrt(G*m*(2/x-1/a_init))
    e0=(a_init-x)/a_init
    
    alpha=arange(0.1, (1-e0)/2, 0.1)
    alist=[]
    
    for alph in alpha:
        ex=TP.TestParticle(m, x, vy=v, alpha=alph)
        iorb_x, iorb_y = ex.Orbit(0.001)
        ex.InstMLoss()
        xlist, ylist= ex.Orbit(0.001)
        a=max((max(xlist)+abs(min(xlist)))/2, (max(ylist)+abs(min(ylist)))/2)
        alist.append(a)
    
    plt.plot(alpha, alist, 'o', label=r'$e_0={:.2}$'.format(e0))
    plt.plot(linspace(0, (1-e0)/2-0.02), analytical(linspace(0, (1-e0)/2-0.02), e0), '-')
    
plt.title(r'$\beta=0, r_{mloss}=r_{min}$')
plt.legend()
plt.savefig('TP_a_vs_alph_.png'.format(e0))
plt.show()