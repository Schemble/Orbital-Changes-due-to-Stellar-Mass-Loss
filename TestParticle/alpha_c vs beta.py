#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:24:41 2018

@author: John
"""

import TestParticle as TP
from scipy import*
from matplotlib import pyplot as plt
from scipy.stats import linregress
#
#m=1
#x=1
#beta=[0.1, 1, 10, 100, 1000, 10000]
#alpha=1
#
#beta_c=[]
#alpha_c=[]
#
#
#for b in beta:
#    ex=TP.TestParticle(m,x, circular=1, alpha=alpha, beta=b)
#    ex.run(0.001, mloss=1)
#    beta_c.append(ex.t)
#    alpha_c.append(1-ex.m/ex.m_init)
#    
#    
#plt.figure()
#plt.plot(log10(array(beta_c)), alpha_c,'.')
#plt.xlabel(r'$\beta$')
#plt.ylabel(r'$\alpha_c$')
#plt.grid()
#plt.show()


#m=1
#x=1
#logbeta=arange(-1, 2, 0.01)
#beta=10**logbeta
#
#
#a_c=[]
#theta=[]
#
#def linreg(x, y):
#    linreg=linregress(x, y)
#    return -linreg.intercept/linreg.slope
#
#for b in beta:
#    a_min=0.5
#    a_max=1
#    ex=TP.TestParticle(alpha=a_min, beta=b, circular=1)
#    Emin=ex.Etot()
#    i=0
#    while abs(a_max-a_min)>0.01:
#        i+=1
#        a=(a_min+a_max)/2
#        ex=TP.TestParticle(alpha=a, beta=b, circular=1)
#        data=ex.runrk4(0.001)
#        E=ex.Etot()
#        if E<0:
#            a_min=a
#            Emin=E
#        elif E>0:
#            a_max=a
#            Emax=E
#        print(i, E)
#    theta.append(ex.Theta())
#    a_c.append(linreg([a_min, a_max], [Emin, Emax]))


plt.figure()
plt.xscale('log')
plt.plot(beta, a_c,'.')
for i in range(1, len(theta)):
    if theta[i] < theta[i-1]:
        plt.plot(beta[i],theta[i])
plt.xlabel(r'$\beta$')
plt.ylabel(r'$\alpha_c$')
plt.grid()
plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
        