#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:28:09 2018

@author: John
"""
from scipy import *
from matplotlib import pyplot as plt
from scipy.stats import linregress
import TestParticle as TP

'''
Single orbit 
'''
#test=TP.TestParticle(circular=1)
#test.runrk4(orbit=1)
#print(test.GetEc())
#
#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.set_aspect('equal')
#ax.grid()
#plt.plot(test.xlist, test.ylist)
#plt.show()




'''
Simple orbit
'''

#test=TP.TestParticle(beta=100,circular=1)
#print(test.Etot())
#test.runrk4()
#print(test.Etot())
#
#
#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.set_aspect('equal')
#ax.grid()
#plt.plot(test.xlist, test.ylist)
#plt.show()


'''
simple orbit mass loss
'''

test=TP.TestParticle(alpha=0.61, beta=10**0.28,circular=1)
test.runrk4()
print(log10(test.GetA()))
#
#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.set_aspect('equal')
#ax.grid()
#plt.plot(test.xlist, test.ylist)
#plt.show()
#
#
#
#test=TP.TestParticle(alpha=0.5, beta=100,circular=1)
#print(test.Etot())
#test.run(0.001, mloss=1)
#print(test.Etot())
#
#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.set_aspect('equal')
#ax.grid()
#plt.plot(test.xlist, test.ylist)
#plt.show()

#
#test=TP.TestParticle(alpha=0.85808885965525894, beta=16.595869074375681, circular=1)
##print(test.Etot())
#test.runrk4()
#print(test.Etot())
#
#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.set_aspect('equal')
#ax.grid()
#plt.plot(test.xlist, test.ylist)
#plt.show()
#
#
#test=TP.TestParticle(alpha=0.859375, beta=16.595869074375681, circular=1)
##print(test.Etot())
#test.runrk4()
#print(test.Etot())
#
#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.set_aspect('equal')
#ax.grid()
#plt.plot(test.xlist, test.ylist)
#plt.show()




'''
E vs alpha
'''

#logbeta=arange(-2, 1, 0.01)
#beta=10**logbeta
#
#m=1
#x=1
#alpha=array([.4])
#alpha_crit=[0.5]
#xplot=linspace(0.1, 1)
#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.grid()
#
#Etot=[]
#
#
#for a in alpha:
#    test=TP.TestParticle(m, x, circular=True, alpha=a, beta=0)
#    test.InstMLoss()
#    Etot.append(test.Etot())
#
#linreg=linregress(alpha, Etot)
#plt.plot(xplot, xplot*linreg.slope+linreg.intercept, label=r'$\beta=0$')
#
#data=[]
#for b in beta:
##    Etot=[]
#    for a in alpha:
#        test=TP.TestParticle(m, x, circular=1, alpha=a, beta=b)
#        test.runrk4()
#        
#        Etot.append(test.m)
#    plt.plot(alpha, Etot, '.', label=r'$\beta=${}'.format(b))
#
#plt.ylabel(r'$E_{tot}$')
#plt.xlabel(r'$\alpha$')
#plt.legend()
#plt.show()

#plt.plot(beta, Etot)
#print(1)
#logbeta=arange(-1, 2, 0.5)
#beta=10**logbeta
#beta=[0,0.1, 1,10,100]
#m=1
#x=1
#alpha=array([.1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
#alpha_crit=[0.5]
#xplot=linspace(0.1, 1)
#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.grid()
#
#Etot=[]
#
#
#for a in alpha:
#    test=TP.TestParticle(m, x, circular=True, alpha=a, beta=0)
#    test.InstMLoss()
#    Etot.append(test.Etot())
#
#linreg=linregress(alpha, Etot)
#plt.plot(xplot, xplot*linreg.slope+linreg.intercept, label=r'$\beta=0$')
#
#data=[]
#for b in beta[1:]:
#    Etot=[]
#    for a in alpha:
#        test=TP.TestParticle(m, x, circular=1, alpha=a, beta=b)
#        test.run(0.001, mloss=1)
#        
#        Etot.append(test.Etot())
#    plt.plot(alpha, Etot, '.', label=r'$\beta=${}'.format(b))
#
#plt.ylabel(r'$E_{tot}$')
#plt.xlabel(r'$\alpha$')
#plt.legend()
#plt.show()
