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

alph_list=[]
beta_list=[]
a_list=[]
e_list=[]
E_list=[]
th_list=[]

def Gather(f):
    a_list.append(f.GetA())
    e_list.append(f.GetEc())
    E_list.append(f.Etot())
    th_list.append(f.Theta())
    alph_list.append(f.alpha)
    beta_list.append(f.beta)

m=1
x=1
logbeta=arange(-1, 3.1, 0.01)
beta=10**logbeta


a_c=[]
theta=[]

def linreg(x, y):
    linreg=linregress(x, y)
    return -linreg.intercept/linreg.slope

for b in beta:
    a_min=0.5
    a_max=1
    ex=TP.TestParticle(alpha=a_min, beta=b, circular=1)
    Emin=ex.Etot()
    i=0
    while abs(a_max-a_min)>0.01:
        i+=1
        a=(a_min+a_max)/2
        ex=TP.TestParticle(alpha=a, beta=b, circular=1)
        data=ex.runrk4()
        Gather(ex)
        E=ex.Etot()
        if E<0:
            a_min=a
            Emin=E
        elif E>0:
            a_max=a
            Emax=E
        print(i, E)
    
    theta.append(ex.Theta())
    a_c.append(linreg([a_min, a_max], [Emin, Emax]))
#    if len(a_c)>2 and a_c[-1]<a_c[-2]:
#        break

with open('critical_data.csv', 'w') as f:
    for i in range(len(alph_list)):
        out_string=''
        out_string+=str(alph_list[i])
        out_string+=','+str(beta_list[i])
        out_string+=','+str(a_list[i])
        out_string+=','+str(e_list[i])
        out_string+=','+str(E_list[i])
        out_string+=','+str(th_list[i])
        out_string+='\n'
        f.write(out_string)
#plt.figure()
#plt.xscale('log')
#plt.scatter(beta, a_c,c=theta)
#plt.xlabel(r'$\beta$')
#plt.ylabel(r'$\alpha_c$')
#plt.grid()
#plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
        