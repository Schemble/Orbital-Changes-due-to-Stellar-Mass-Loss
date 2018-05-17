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
#
#alpha=arange(0, 1, 0.1)
m=1
x=1
#Etot=[]

#
#for a in alpha:
#    test=TP.TestParticle(m, x, circular=True, alpha=a, beta=0)
#    test.InstMLoss()
#    Etot.append(test.Etot())

#fig=plt.figure()
#plt.plot(alpha, Etot, 'o')
#plt.xlabel(r'$\alpha$')
#plt.ylabel(r'Total Energy $[\frac{AU^2M_\odot}{yr^2}]$')
#plt.xlim(xmin=0, xmax=1)
#plt.ylim(ymin=-20, ymax=20)
#plt.xticks(arange(0, 1.1, 0.1))
#plt.grid()
#plt.savefig('Figures/Testparticle/TP_Etot_vs_a.png')
#plt.show(fig)

#The data points seem to follow a linear pattern, make a linear fit

#linreg=linregress(alpha, Etot)
#intercept, slope=linreg.intercept, linreg.slope

def findy(x):
    return slope*x+intercept



#x_fit=linspace(0, 1)
#y_fit=findy(x_fit)

#fig=plt.figure()
#ax = fig.add_subplot(111)
#plt.plot(alpha, Etot, 'o', x_fit, y_fit)
#plt.xlabel(r'$\alpha$')
#plt.ylabel(r'Total Energy $[\frac{AU^2M_\odot}{yr^2}]$')
#plt.xlim(xmin=0, xmax=1)
#plt.ylim(ymin=-20, ymax=20)
#plt.xticks(arange(0, 1.1, 0.1))
#ax.grid()
#plt.savefig('Figures/Testparticle/TP_Etot_vs_a_fit.png')
#plt.show()


#Find value of alpha at Etot=0

def findx(y):
    return (y-intercept)/slope

def analyticalEper(alpha, e):
    G=4*pi**2 
    return (G*m)/x*(alpha/(1-e)-1/2) 

def analyticalEapo(alpha, e):
    G=4*pi**2 
    return (G*m)/x*(alpha/(1+e)-1/2) 
#
#
#
#e_list=arange(0.1, 1, 0.1)
##alpha_crit=findx(0)
#
#fig=plt.figure()
#ax = fig.add_subplot(111)
#cmap = plt.get_cmap('jet')
##plt.plot(x_fit, y_fit , [0,1], [0,0], 'g--', alpha, Etot, '.')
##plt.plot(alpha_crit, 0, 'ro', label=r'$\alpha_{crit}$'+'={:.1f}'.format(alpha_crit))
#for e in e_list[::-1]:
#    plt.plot(linspace(0, 1), analyticalEper(linspace(0, 1), e),'--',c=cmap(e))
#plt.plot(linspace(0, 1), analyticalEapo(linspace(0, 1), 0),'b',label=r'$e_0={:.1f}$, $\alpha_c={:.2f}$'.format(0, 1/2))
#for e in e_list:
#    plt.plot(linspace(0, 1), analyticalEapo(linspace(0, 1), e),'--',c=cmap(e), label=r'$e_0={:.1f}$, $\alpha_c={:.2f}$'.format(e, (1-e)/2))
#fig.legend(bbox_to_anchor=(1, 0.85), loc='upper right', ncol=1)
##plt.tight_layout(rect=[0,0,0.75,1])
#plt.xlabel(r'$\alpha$')
#plt.ylabel(r'Total Energy $[\frac{AU^2M_\odot}{yr^2}]$')
#plt.xticks(arange(0, 1.1, 0.1))
#plt.xlim(xmin=0, xmax=1)
#plt.ylim(ymin=-20, ymax=20)
#plt.subplots_adjust(right=0.7, bottom=0.3)
#ax.grid()
##plt.savefig('Figures/Testparticle/TP_Etot_vs_a_acrit.png')
#plt.show()

'''
What does the orbit look like after instantainious mass loss.
'''

alpha=linspace(0, 0.5, 11)
m=1
x=1


#plt.figure()
#plt.grid()
#for a in alpha[:-1]:
#    test=TP.TestParticle(m, x, circular=True, alpha=a, beta=0)
#    test.InstMLoss()
#    test.runrk4(orbit=1)
#    x_plot=test.xlist
#    y_plot=test.ylist
#    plt.plot(x_plot, y_plot, label=r'$\alpha$'+'={:.2f}'.format(a))
#
#
#plt.legend(loc=2)
##plt.savefig('Figures/TestParticle/TP_Orbits_a=0-0.4_b=0.png')
#plt.show()

#fig=plt.figure()
#ax = fig.add_subplot(111)
#ax.set_aspect('equal')
#for a in alpha[:-1]:
#    test=TP.TestParticle(m, x, circular=True, alpha=a, beta=0)
#    test.InstMLoss()
#    test.runrk4(orbit=1)
#    x_plot=test.xlist
#    y_plot=test.ylist
#    plt.plot(x_plot, y_plot, label=r'$\alpha={:.2f}$, $a={:.2f}$, $e={:.2f}$'.format(a, test.GetA(), test.GetEc()))
#fig.legend(bbox_to_anchor=(1, 0.827), loc='upper right', ncol=1)
##plt.tight_layout(rect=[0,0,0.75,1])
#plt.plot(0,0,'ro')
#plt.xlabel('x [AU]')
#plt.ylabel('x [AU]')
##plt.xticks(arange(0, 1.1, 0.1))
##plt.xlim(xmin=0, xmax=1)
##plt.ylim(ymin=0,ymax=1)
#plt.subplots_adjust(right=0.6, bottom=0.3)
#ax.grid()
##plt.savefig('Figures/Testparticle/TP_Etot_vs_a_acrit.png')
#plt.show()




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
#    e.append(test.GetEc())
#    
def analyticalAperi(alpha, e):
    return (1-alpha)*(1-e)/(1-2*alpha-e)
def analyticalAapo(alpha, e):
    return (1-alpha)*(1+e)/(1-2*alpha+e)
#
def analyticaleccApo(alpha,e):
    return abs(e-alpha)/(1-alpha)
def analyticaleccPeri(alpha,e):
    return (e+alpha)/(1-alpha)

##
alph=linspace(0, 0.5)
#e_list=arange(0.1, 1, 0.2)
#
#plt.figure()
#plt.xlabel(r'$\alpha$')
#plt.ylabel(r'$a/a_0$[AU]')
#plt.plot(alph[:-1], analyticalA(alph[:-1]))
#plt.plot(alpha, sma, '.')
#plt.grid()
#plt.show()

#plt.figure()
#plt.xlabel(r'$\alpha$')
#plt.ylabel(r'$e$')
#plt.plot(alph, analyticalecc1(alph))
##plt.plot(alpha, e, '.')
#plt.xlim(xmin=0, xmax=0.5)
#plt.ylim(ymin=0,ymax=1)
#plt.grid()
#plt.show()

e_list=arange(0.1, 1, 0.1)
#alpha_crit=findx(0)

fig=plt.figure()
ax = fig.add_subplot(111)
cmap = plt.get_cmap('jet')
#plt.plot(x_fit, y_fit , [0,1], [0,0], 'g--', alpha, Etot, '.')
#plt.plot(alpha_crit, 0, 'ro', label=r'$\alpha_{crit}$'+'={:.1f}'.format(alpha_crit))
for e in e_list[::-1]:
    ac=(1-e)/2
    plt.plot(linspace(0, ac, 100)[:-1], analyticalAperi(linspace(0, ac, 100)[:-1], e),'--',c=cmap(e))
plt.plot(linspace(0, 0.5, 100), analyticalAperi(linspace(0, 0.5, 100), 0),'b',label=r'$e_0=0.0$, $\alpha_c=0.5$')
for e in e_list:
    ac=(1+e)/2
    plt.plot(linspace(0, ac, 1100)[:-1], analyticalAapo(linspace(0, ac, 1100)[:-1], e),'--',c=cmap(e) ,label=r'$e_0={:.1f}$, $\alpha_c={:.2f}$'.format(e, ac))
fig.legend(bbox_to_anchor=(1, 0.85), loc='upper right', ncol=1)
#plt.tight_layout(rect=[0,0,0.75,1])
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\frac{a}{a_0}$')
plt.xticks(arange(0, 1.1, 0.1))
plt.xlim(xmin=0, xmax=1)
plt.ylim(ymin=0,ymax=30)
plt.subplots_adjust(right=0.7, bottom=0.3)
ax.grid()
#plt.savefig('Figures/Testparticle/TP_Etot_vs_a_acrit.png')
plt.show()


fig=plt.figure()
ax = fig.add_subplot(111)
cmap = plt.get_cmap('jet')
#plt.plot(x_fit, y_fit , [0,1], [0,0], 'g--', alpha, Etot, '.')
#plt.plot(alpha_crit, 0, 'ro', label=r'$\alpha_{crit}$'+'={:.1f}'.format(alpha_crit))
for e in e_list[::-1]:
    ac=(1-e)/2
    plt.plot(linspace(0, ac, 100)[:-1], analyticaleccPeri(linspace(0, ac, 100)[:-1], e),'--',c=cmap(e))
plt.plot(linspace(0, 0.5), analyticaleccPeri(linspace(0, 0.5), 0),'b',label=r'$e_0=0.0$, $\alpha_c=0.5$')
for e in e_list:
    ac=(1+e)/2
    plt.plot(linspace(0, ac, 10000)[:-1], analyticaleccApo(linspace(0, ac, 10000)[:-1], e),'--',c=cmap(e) ,label=r'$e_0={:.1f}$, $\alpha_c={:.2f}$'.format(e, ac))
fig.legend(bbox_to_anchor=(1, 0.85), loc='upper right', ncol=1)
#plt.tight_layout(rect=[0,0,0.75,1])
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$e$')
plt.xticks(arange(0, 1.1, 0.1))
plt.xlim(xmin=0, xmax=1)
plt.ylim(ymin=0,ymax=1)
plt.subplots_adjust(right=0.7, bottom=0.3)
ax.grid()
#plt.savefig('Figures/Testparticle/TP_Etot_vs_a_acrit.png')
plt.show()

'''
beta=inf
'''
#
#def analyticalA(alpha):
#    return 1/(1-alpha)
#
#fig=plt.figure()
#ax = fig.add_subplot(111)
#plt.plot(linspace(0, 1, 150), analyticalA(linspace(0, 1, 150)))
##fig.legend(bbox_to_anchor=(1, 0.85), loc='upper right', ncol=1)
#plt.xlabel(r'$\alpha$')
#plt.ylabel(r'$a$')
#plt.xticks(arange(0, 1.1, 0.1))
#plt.xlim(xmin=0, xmax=1)
#plt.ylim(ymin=0, ymax=100)
##plt.subplots_adjust(right=0.7, bottom=0.3)
#ax.grid()
##plt.savefig('Figures/Testparticle/TP_Etot_vs_a_acrit.png')
#plt.show()


