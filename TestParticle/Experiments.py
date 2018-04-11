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

alpha=arange(0, 1, 0.1)
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
plt.show(fig)

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
plt.show()


#Find value of alpha at Etot=0

def findx(y):
    return (y-intercept)/slope


alpha_crit=findx(0)

fig=plt.figure()
ax = fig.add_subplot(111)
plt.plot(x_fit, y_fit , [0,1], [0,0], 'g--', alpha, Etot, '.')
plt.plot(alpha_crit, 0, 'ro', label=r'$\alpha_{crit}$'+'={:.1f}'.format(alpha_crit))
fig.legend(loc=2)
plt.xlabel(r'$\alpha$')
plt.ylabel(r'Total Energy $[\frac{AU^2M_\odot}{yr^2}]$')
plt.xticks(arange(0, 1.1, 0.1))
plt.xlim(xmin=0, xmax=1)
plt.ylim(ymin=-20, ymax=20)
ax.grid()
plt.savefig('Figures/Testparticle/TP_Etot_vs_a_acrit.png')
plt.show()

'''
What does the orbit look like after instantainious mass loss.
'''

#alpha=arange(0, 0.5, 0.1)
#m=1
#x=1
#
#
#plt.figure()
#for a in alpha:
#    test=TP.TestParticle(m, x, circular=True, alpha=a, beta=0)
#    test.InstMLoss()
#    x_plot, y_plot= test.Orbit(0.01, plot=0)
#    plt.plot(x_plot, y_plot, label=r'$\alpha$'+'={:.1f}'.format(a))
#
#plt.plot(0,0,'ro')
#plt.xlabel('x [AU]')
#plt.ylabel('x [AU]')
#plt.legend(loc=2)
#plt.savefig('Figures/TestParticle/TP_Orbits_a=0-0.4_b=0.png')
#plt.show()
#    
'''
a vs alph, e vs alph inst. mloss
'''
#alpha=arange(0, 0.5, 0.025)
#e=[]
#sma=[]
#for a in alpha:
#    test =TP.TestParticle(alpha=a, circular=1)
#    test.InstMLoss()
#    sma.append(test.GetA())
#    e.append(test.Orbit(0.001)[4])
#    
#def analyticalA(alpha):
#    return (alpha-1)/(2*alpha-1)
#
#def analyticalE(alpha):
#    return 1-(1-2*alpha)/(1-alpha)
#
#alph=linspace(0, 0.5, 100)
#
##plt.figure()
##plt.xlabel(r'$\alpha$')
##plt.ylabel(r'$a/a_0$[AU]')
##plt.plot(alph[:-1], analyticalA(alph[:-1]))
##plt.plot(alpha, sma, '.')
##plt.grid()
##plt.show()
#
#plt.figure()
#plt.xlabel(r'$\alpha$')
#plt.ylabel(r'$e$')
#plt.plot(alph, analyticalE(alph))
#plt.plot(alpha, e, '.')
#plt.grid()
#plt.show()


