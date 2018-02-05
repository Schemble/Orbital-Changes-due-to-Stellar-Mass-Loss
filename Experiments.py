#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:55:41 2018

@author: John
"""

import TestParticle as TP
from scipy import*
from matplotlib import pyplot as plt
from scipy.stats import linregress


'''
Determine critical value of alpha during instantainious massloss (beta=0)
'''

alpha=[0.2, 0.4, 0.6, 0.8]
m=1
x=1
Etot=[]


for a in alpha:
    test=TP.TestParticle(m, x, circular=True, alpha=a, beta=0)
    test.InstMLoss()
    Etot.append(test.Etot())

fig=plt.figure()
plt.plot(alpha, Etot, 'o')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'Total Energy $[\frac{AU^2M_\odot}{yr^2}]$')
plt.xlim(xmin=0, xmax=1)
plt.ylim(ymin=-20, ymax=20)
plt.xticks(arange(0, 1.1, 0.1))
plt.grid()
plt.savefig('Figures/Testparticle/TP_Etot_vs_a.png')
plt.close(fig)

#The data points seem to follow a linear pattern, make a linear fit

linreg=linregress(alpha, Etot)
intercept, slope=linreg.intercept, linreg.slope

def findy(x):
    return slope*x+intercept



x_fit=linspace(0, 1)
y_fit=findy(x_fit)

fig=plt.figure()
ax = fig.add_subplot(111)
plt.plot(alpha, Etot, 'o', x_fit, y_fit)
plt.xlabel(r'$\alpha$')
plt.ylabel(r'Total Energy $[\frac{AU^2M_\odot}{yr^2}]$')
plt.xlim(xmin=0, xmax=1)
plt.ylim(ymin=-20, ymax=20)
plt.xticks(arange(0, 1.1, 0.1))
ax.grid()
plt.savefig('Figures/Testparticle/TP_Etot_vs_a_fit.png')
plt.close()


#Find value of alpha at Etot=0

def findx(y):
    return (y-intercept)/slope


alpha_crit=findx(0)

fig=plt.figure()
ax = fig.add_subplot(111)
plt.plot(alpha, Etot, 'o', x_fit, y_fit, [0,1], [0,0], '--')
plt.plot(alpha_crit, 0, 'ro', label=r'$\alpha_{crit}$'+'={}'.format(alpha_crit))
fig.legend(loc=2)
plt.xlabel(r'$\alpha$')
plt.ylabel(r'Total Energy $[\frac{AU^2M_\odot}{yr^2}]$')
plt.xticks(arange(0, 1.1, 0.1))
plt.xlim(xmin=0, xmax=1)
plt.ylim(ymin=-20, ymax=20)
ax.grid()
plt.savefig('Figures/Testparticle/TP_Etot_vs_a_acrit.png')
plt.close()
