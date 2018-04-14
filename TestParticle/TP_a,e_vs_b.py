#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 22:26:04 2018

@author: John
"""

import TestParticle as TP
from scipy import*
from matplotlib import pyplot as plt
from scipy.stats import linregress

m=1
x=1
logbeta=arange(-1, 2, 0.25)
logbeta=arange(-3, 0, 0.1)
beta=10**logbeta
ac=[0.5077439990113547,
 0.51334646205679624,
 0.53296464167535629,
 0.58131538196630328,
 0.66175768286129866,
 0.74522086102627361,
 0.76511765129691267,
 0.80565140494059195,
 0.84315840602492631,
 0.86907985534275733,
 0.8906881001488488,
 0.90862433883210214,
 0.92403358151211734,
 0.93684915567335525,
 0.94778767810357478,
 0.95687214118878805,
 0.96436416271515635,
 0.97056003723466411,
 0.97552838148165533,
 0.97986054083339535]
SMA=[]
E=[]
alpha=arange(0.1, 1, 0.1)

j=0
for a in alpha:
    sma=[]
    e=[]
    i=0
    for b in beta:        
#        if a<ac[i]:
        ex=TP.TestParticle(alpha=a, beta=b, circular=1)
        ex.runrk4()
        SMa=ex.GetA()
        if SMa != 'Unbound':               
            sma.append(ex.GetA())
        
            e.append(ex.Orbit(0.001)[-1])
        i+=1
        print(j,i)
    SMA.append(sma)
    E.append(e)
    j+=1
#plt.figure()
#plt.grid()
#plt.xscale('log')
#plt.xlabel(r'$\log(\beta)$')
#plt.ylabel(r'$a$')
#for i in range(len(SMA)):
#    plt.plot(beta[len(beta)-len(SMA[i]):], SMA[i], '.', label=r'$\alpha={:.1f}$'.format(alpha[i]))
#plt.legend()
#plt.show()

plt.figure()
plt.grid()
plt.xscale('log')
plt.xlabel(r'$\log(\beta)$')
plt.ylabel(r'$a$')
for i in range(len(SMA)):
    plt.plot(beta[len(beta)-len(SMA[i]):], SMA[i], label=r'$\alpha={:.1f}$'.format(alpha[i]))
plt.legend()
plt.show()

#plt.figure()
#plt.grid()
#plt.xscale('log')
#plt.xlabel(r'$\log(\beta)$')
#plt.ylabel(r'$e$')
#for i in range(len(E)):
#    plt.plot(beta[len(beta)-len(E[i]):], E[i], '.', label=r'$\alpha={:.1f}$'.format(alpha[i]))
#plt.legend()
#plt.show()

plt.figure()
plt.grid()
plt.xscale('log')
plt.xlabel(r'$\log(\beta)$')
plt.ylabel(r'$e$')
for i in range(len(E)):
    plt.plot(beta[len(beta)-len(E[i]):], E[i], label=r'$\alpha={:.1f}$'.format(alpha[i]))
plt.legend()
plt.show()

