#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:23:06 2018

@author: John
"""

import TestParticle as TP
from scipy import*
from matplotlib import pyplot as plt
from scipy.stats import linregress
import time

fixed_beta=10**(arange(3.25, 4.25, 0.25))
fixed_beta=[10**4]
fixed_alpha=arange(0.01,1,0.01)
i=0
#b=fixed_beta[0]
#b_max=fixed_beta[1]
alph=fixed_alpha[0]
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
ti=time.time()
for alph in fixed_alpha:
    b=fixed_beta[0]
    ex=TP.TestParticle(alpha=alph, beta=b)
    ex.runrk4()
    Gather(ex)
    for b in fixed_beta:
            ex=TP.TestParticle(alpha=alph, beta=b)
            ex.runrk4()
            Gather(ex)
            print(alph, b, time.time()-ti)
with open('grid_data3.2.csv', 'w') as f:
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
#plt.grid()
#plt.xscale('log')
#plt.scatter(array(beta_list), array(alph_list), c=log10(array(a_list)))
#plt.ylabel(r'$\beta$')
#plt.xlabel(r'$\alpha$')
#plt.colorbar()
#plt.show()
#
#plt.figure()
#plt.grid()
#plt.xscale('log')
#plt.scatter(array(beta_list), array(alph_list), c=array(e_list))
#plt.ylabel(r'$\beta$')
#plt.xlabel(r'$\alpha$')
#plt.colorbar()
#plt.show()

        
#x, y = meshgrid(log10(beta_list), alph_list)
#
#Z=a_list
#
#plt.figure()
#im=plt.imshow(Z)#, origin='lower', extent=[min(log10(beta_list)),max(log10(beta_list)),min(alph_list), max(alph_list)])
##cset=plt.contour(Z, arange(0, 3, 0.2), cmap=plt.cm.Greys, extent=[0,0.5,0,0.5])
#plt.xlabel(r'$\beta$')
#plt.ylabel(r'$\alpha$')
#
#plt.colorbar(im)
#plt.show()
        