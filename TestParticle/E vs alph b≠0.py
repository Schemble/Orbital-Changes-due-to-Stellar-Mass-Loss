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
import scipy.optimize as op

'''
Find relation between critical alpha and varying beta
'''

logbeta=arange(-1, 2, 0.5)
beta=10**logbeta
m=1
x=1
alpha=array([.1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
alpha_crit=[0.5]
xplot=linspace(0.1,1)
#alpha=[1]
fig=plt.figure()
ax=fig.add_subplot(111)
ax.grid()

Etot=[]


for a in alpha:
    test=TP.TestParticle(m, x, circular=True, alpha=a, beta=0)
    test.InstMLoss()
    Etot.append(test.Etot())

linreg=linregress(alpha, Etot)
plt.plot(xplot, xplot*linreg.slope+linreg.intercept, label=r'$\beta=0$')
#print(linreg.intercept)


def logarithmic(x, a, c):
    print(x,a,b, c)
    return a*log(x)+c
    

def polynomial(x, a, b, c):
    return a*x**b+c

def exponential(x, a, b, c):
    return a*exp(b*x)+c

def other(x, a, b,c, d):
    return a*x/(b-c*x)+d

data=[]
for b in beta[1:]:
    Etot=[]
    for a in alpha:
        test=TP.TestParticle(m, x, circular=1, alpha=a, beta=b)
        test.runrk4()
        
        Etot.append(test.Etot())
#
#
#        print('beta={}, alpha={} done'.format(b, a))
   
#    model=odr.Model(logarithmic)
#    mydata = odr.Data(alpha, array(Etot))
#    myodr=odr.ODR(mydata, model, beta0=[1, 1, 1])
#    myoutput=myodr.run()
#    myoutput.pprint()
#    c=curve_fit(polynomial, alpha, Etot)
#    print('pol',polynomial(0, c[0][0], c[0][1], c[0][2]))
#    yplot=polynomial(xplot, c[0][0], c[0][1], c[0][2])
#    c=curve_fit(other, alpha, Etot)
#    print(other(0, c[0][0], c[0][1], c[0][2], c[0][3]))
#    yplot=other(xplot, c[0][0], c[0][1], c[0][2], c[0][3])
#    def f(x):
#        global c
#
#        return c[0][0]*x/(c[0][1]-c[0][2]*x)+c[0][3]
    
    
#    a_crit=op.brentq(f, 0, 1)
#    alpha_crit.append(a_crit)
    plt.plot(alpha, Etot, '.', label=r'$\beta=${}'.format(b))
    print(test.Etot(),test.r, test.v, test.m)
#    plt.plot(xplot, yplot, label=r'$\beta={}$'.format(b))
#plt.title(r'$\frac{x}{1-x}$ fit')
plt.ylabel(r'$E_{tot}$')
plt.xlabel(r'$\alpha$')
plt.legend()
#plt.savefig('TP_E_vs_alph_beta=[{}-{}].png'.format(beta[0], beta[-1]))
plt.show()

#



#print(alpha_crit)
#

#
#xfit=arange(0.5, 0.9, 0.01)
#yfit=exponential(myoutput.beta, xfit)
#c=curve_fit(exponential, alpha_crit, beta)
#yplot=exponential(linspace(.5, 1), c[0][0], c[0][1], c[0][2])
#plt.figure()
#plt.grid()
#plt.yscale('log')
#plt.xscale('log')
#plt.plot(alpha_crit, beta, '.')
#plt.ylabel(r'$\beta$')
#plt.xlabel(r'$\alpha_{crit}$')
#plt.plot(xplot, yplot)
#plt.xlim(xmin=0.5, xmax=1)
#plt.savefig('Figures/Testparticle/TP_b_vs_ac_b={}-{}.png'.format(min(beta), max(beta)))
#plt.show()
    

