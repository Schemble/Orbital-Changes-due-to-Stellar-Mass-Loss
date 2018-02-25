#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:01:10 2018

@author: John
"""

import TestParticle as TP
from scipy import*
from matplotlib import pyplot as plt
from scipy.stats import linregress
from scipy.optimize import curve_fit
from scipy import odr


'''
Find relation between critical alpha and varying beta
'''

beta=array([0, 10, 100, 1000])
m=1
x=1
alpha=[.2, .4, .6, .8]
alpha_crit=[0.5]
for b in beta[1:]:
    Etot=[]
    for a in alpha:
        test=TP.TestParticle(m, x, circular=1, alpha=a, beta=b)
        test.run(0.001)
        Etot.append(test.Etot())
    linreg=linregress(alpha, Etot)
    alpha_crit.append((0-linreg.intercept)/linreg.slope)
    
    


def polynomial(c, x):
    print(c[1])
    return c[0]*x**c[1]+c[2]

def exponential(c, x):
    return c[0]*exp(c[1]*x)+c[2]


model=odr.Model(exponential)
mydata = odr.Data(alpha_crit, beta)
myodr=odr.ODR(mydata, model, beta0=[1, 1, 1])
myoutput=myodr.run()
myoutput.pprint()

xfit=arange(0.5, 0.9, 0.01)
yfit=exponential(myoutput.beta, xfit)
plt.figure()
plt.grid()
#plt.yscale('log')
plt.plot(alpha_crit, beta, '.')
plt.ylabel(r'$\beta$')
plt.xlabel(r'$\alpha_{crit}$')
plt.plot(xfit, yfit)
#plt.xlim(xmin=0.5, xmax=1)
plt.savefig('Figures/Testparticle/TP_b_vs_ac_b={}-{}.png'.format(min(beta), max(beta)))
plt.show()