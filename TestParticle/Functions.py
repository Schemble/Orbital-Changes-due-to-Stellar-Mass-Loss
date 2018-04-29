#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:59:23 2018

@author: John
"""
import TestParticle as TP
from scipy import*
from matplotlib import pyplot as plt
import random


def a(alpha, beta):
    idx=unravel_index(argmin(abs(grid_x-beta),axis=None), grid_x.shape)[0]
    idy=unravel_index(argmin(abs(grid_y-alpha),axis=None), grid_x.shape)[1]
    return grid_za[idx, idy]
def e(alpha, beta):
    idx=unravel_index(argmin(abs(grid_x-beta),axis=None), grid_x.shape)[0]
    idy=unravel_index(argmin(abs(grid_y-alpha),axis=None), grid_x.shape)[1]
    return grid_ze[idx, idy]

e_int=[]
e_sim=[]
a_int=[]
a_sim=[]
alph_list=[]
beta_list=[]
for i in range(10000):
    beta=random.uniform(-1, 4)
    alpha=random.random()
    e_int.append(e(alpha, beta))
    a_int.append(a(alpha, beta))
    alph_list.append(alpha)
    beta_list.append(beta)
    sim=TP.TestParticle(alpha=alpha, beta=beta)
    sim.runrk4()
    a_sim.append(log10(sim.GetA()))
    e_sim.append(sim.GetEc())
    if e_sim[-1]>1:
        e_sim[-1]=inf
plt.figure()
plt.ymin=0
plt.ymax=1
plt.xmin=-1
plt.xmax=4
plt.scatter(beta_list, alph_list, c=log10(array(a_int)/array(a_sim)))
plt.xlabel(r'$\log\beta$')
plt.ylabel(r'$\alpha$')
plt.colorbar(label='log(a_interpolated/a_simulated)')
plt.show()

plt.figure()
plt.ymin=0
plt.ymax=1
plt.xmin=-1
plt.xmax=4
plt.scatter(beta_list, alph_list, c=log10(array(e_int)/array(e_sim)))
plt.xlabel(r'$\log\beta$')
plt.ylabel(r'$\alpha$')
plt.colorbar(label='log(e_interpolated/e_simulated)')
plt.show()