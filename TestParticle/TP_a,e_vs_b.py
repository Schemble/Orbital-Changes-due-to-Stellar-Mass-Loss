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

fixed_beta=10**(arange(-2, 4.1, 0.25))
fixed_alpha=arange(0.1,1,0.1)
i=0

alph=fixed_alpha[0]

beta_list=[]
alpha_list=[]
a_list=[]
tol=0.05

S=0.95
h_min=0.01
for alph in fixed_alpha:
    
    a='Unbound'
    i=0
    while a == 'Unbound':
        b=fixed_beta[i]
        ex=TP.TestParticle(alpha=alph, beta=b, circular=1)
        ex.runrk4()
        a=ex.GetA()
        sma=[a]
        b_list=[b]
        alph_list=[alph]
        i+=1
        h=0.1*b
    for beta in fixed_beta[i:]:
        b_max=beta
        ex=TP.TestParticle(alpha=alph, beta=b_max, circular=1)
        ex.runrk4()
        af=ex.GetA()
        a=sma[-1]
        diff=abs(log10(a)-log10(af))
        if diff<tol:
            b=b_max
        elif diff>tol and h==0.1*fixed_beta[i-1]:
            h=0.1*b
        while b<b_max: 
            
            y=[]
            
            for h0 in [h, h/2]:
                
                ex=TP.TestParticle(alpha=alph, beta=b+h0, circular=1)
                ex.runrk4()
                
                y.append(ex.GetA())
            diff=abs(log10(y[0])-log10(y[1]))
            
            if diff>tol:
                h *= S*(tol/diff)**(1/5)
                if b+h>b_max:
                    b=b_max
                    break
                b+=h
                ex=TP.TestParticle(alpha=alph, beta=b, circular=1)
                ex.runrk4()
                sma.append(ex.GetA())
                b_list.append(b)
                alph_list.append(alph)
                if b+h>b_max:
                    b=b_max
                    break
                    
            else:
                sma.append(y[0])
                b+=h
                b_list.append(b)
                alph_list.append(alph)
                h *= S*(tol/diff)**(1/4)
                if b+h>b_max:
                    b=b_max
                    break

        sma.append(af)
        b_list.append(b)
        alph_list.append(alph)
        print(alph, b)
    a_list.append(sma)
    beta_list.append(b_list)
    alpha_list.append(alph_list)
plt.figure()
plt.grid()
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$\beta$')
plt.ylabel(r'$a$')
for i in range(len(a_list)):
    plt.plot(beta_list[i], a_list[i], '.-', label=r'$\alpha={:.1f}$'.format(fixed_alpha[i]))
plt.legend()
plt.show()



an_list=[]
alphn_list=[]
for b in fixed_beta:
    ann_list=[]
    alphnn_list=[]
    for i in range(len(a_list)):
        if any(beta_list[i]==b):
            ann_list.append(a_list[i][beta_list[i].index(b)])
            alphnn_list.append(alpha_list[i][beta_list[i].index(b)])
    an_list.append(ann_list)
    alphn_list.append(alphnn_list)

plt.figure()
plt.grid()
plt.yscale('log')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$a$')
for i in range(len(an_list)):
    plt.plot(alphn_list[i], an_list[i], '.-', label=r'$beta={}$'.format(fixed_beta[i]))
#plt.legend()
plt.show()
    


#m=1
#x=1
#logbeta=arange(-2, -1., 0.5)
#fixed_beta=10**logbeta
#
#a=[]
#E=[]
#alpha=arange(0.1, 1, 0.1)
##alpha=[0.1]
#beta_max=0.1
#beta_list=[]
#tol=0.1
#for alph in alpha:
#    sma=[]
#    b_list=[]    
#    e=[]
#    
#    S=0.95
#    hi=0.00001
#    for i in range(len(fixed_beta)-1):
#        print(i)
#        
#        b=fixed_beta[i]
#        
#        h=hi
#        b_max=fixed_beta[i+1]
#        if h/2>fixed_beta[i+1]-fixed_beta[i]:
#            b=fixed_beta[i+1]
#            ex=TP.TestParticle(alpha=alph, beta=b, circular=1)
#            ex.runrk4()
#            sma.append(ex.GetA())
#            b_list.append(b)
#        while b<b_max:
#            y=[]
#            
#            for h0 in [h, h/2]:
#                
#                ex=TP.TestParticle(alpha=alph, beta=b+h0, circular=1)
#                ex.runrk4()
#                
#                y.append(ex.GetA())
#            if y[0] != 'Unbound' and y[1] != 'Unbound': 
#                diff=abs(log10(y[0])-log10(y[1]))
#                
#                if diff>tol:
#                    h *= S*(tol/diff)**(1/5)
#                    hi=h
#                    if b+h>b_max:
#                        h=b_max-b
#                    ex=TP.TestParticle(alpha=alph, beta=b+h, circular=1)
#                    ex.runrk4()
#                    sa=ex.GetA()
#                    if sa == 'Unbound':
#                        sa=y[1]
#                        h=h0
#                    b+=h
#                    
#                    sma.append(sa)
#                    b_list.append(b)
#                    if b+h>b_max and b!=b_max:
#                        h=b_max-b
#                        
#                else:
#                    sma.append(y[0])
#                    b+=h
#                    b_list.append(b)
#                    
#                    h *= S*(tol/diff)**(1/4)
#                    hi=h
#                    if b+h>b_max and b!=b_max:
#                        h=b_max-b
#                        
#                print(b)
#            else:
#                b+=10**(0.001)
#                h=b_max-b
#            
#
#    a.append(sma)
#    beta_list.append(array(b_list))
#
#plt.figure()
#plt.grid()
#plt.xscale('log')
#plt.yscale('log')
#plt.xlabel(r'$\beta$')
#plt.ylabel(r'$a$')
#for i in range(len(a)):
#    plt.plot(beta_list[i], a[i], '.-', label=r'$\alpha={:.1f}$'.format(alpha[i]))
#plt.legend()
#plt.show()


#plt.figure()
#plt.grid()
#plt.xscale('log')
#plt.xlabel(r'$\beta$')
#plt.ylabel(r'$e$')
#for i in range(len(E)):
#    plt.plot(beta[len(beta)-len(E[i]):], E[i], label=r'$\alpha={:.1f}$'.format(alpha[i]))
#plt.legend()
#plt.show()
#for i in range(len(beta_list)):
#    linr = linregress(log10(1-beta_list[i]), log10(a[i]))
#
#    print(10**linr.intercept)
#print((1-alpha)/(1-2*alpha))
#a=[]
#for alph in alpha:
#    ex=TP.TestParticle(alpha=alph, beta=10000, circular=1)
#    ex.runrk4()
#    a.append(ex.GetA())
#print(a)
