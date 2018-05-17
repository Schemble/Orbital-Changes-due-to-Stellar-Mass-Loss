#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 20:31:19 2018

@author: John
"""

from matplotlib import pyplot as plt
from scipy import interpolate
import numpy as np
from scipy import*


alph_list=[]
beta_list=[]
ac_list=[]
e_list=[]
E_list=[]
th_list=[]
data_points=[]

with open('ac_vs_beta_data.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        beta_list.append(log10(float(l[0])))
        ac_list.append(float(l[1]))
        th_list.append(float(l[2]))
        data_points.append([log10(float(l[0])),float(l[1]),float(l[2])])

#plt.figure()
#plt.plot(beta_list, ac_list)
#plt.show()
data_points=array(data_points)
def linint(value, x1, x2, f1, f2):
    x=value
    return (f1*(x2-x)+f2*(x-x1))/(x2-x1)


mi=linspace(1, 10)
ai=1
mf=0.6
alpha=mi-mf

tm=[]
for m in mi:
    alpha=1-mf/m
    if alpha>0.5:
        diff=abs(array(data_points[:,1])-alpha)
        p1=data_points[argmin(diff)]
        p2=data_points[int(where(diff==sort(diff)[1])[0])]
        print(alpha,p1, p2)
        bc=linint(alpha, p1[1], p2[1], p1[0], p2[0])
        tm.append(sqrt((ai**3)/m)*10**bc)
    else:
        tm.append(0)
plt.figure()
plt.grid()
plt.plot(tm, mi)
plt.ylabel(r'initial mass [M$_\odot$]')
plt.xlabel(r'minimum time [years]')
plt.show()      
        
        
        
        
        
        
        
        
        
        
        