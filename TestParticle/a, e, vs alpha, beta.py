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

fixed_beta=10**(arange(-1, 2, 0.5))
fixed_alpha=arange(0,1,0.1)
i=0
b=fixed_beta[0]
b_max=fixed_beta[1]
alph=fixed_alpha[0]



tol=0.1
ex=TP.TestParticle(alpha=alph, beta=b)
ex.runrk4()
alpha_list=[alpha]
beta_list=[beta]
alist=[ex.GetA()]
while alph<alph_max:
    ex=TP.TestParticle(alpha=alph, beta=b_max)
    ex.runrk4()
    alpha_list.append(alph)
    beta_list.append(beta_max)
    alist=[ex.GetA()]
    
    while b<b_max:


        
        
    
        