#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:02:28 2018

@author: John
"""
from matplotlib import pyplot as plt
from scipy import interpolate

alph_list=[]
beta_list=[]
a_list=[]
e_list=[]
E_list=[]
th_list=[]
with open('grid_data.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_list.append(float(l[0]))
        beta_list.append(float(l[1]))
        a_list.append(float(l[2]))
        e_list.append(float(l[3]))
        E_list.append(float(l[4]))
        th_list.append(float(l[5]))
alph_list=array(alph_list)
beta_list=log10(array(beta_list))
a_list=log10(array(a_list))
e_list=array(e_list)
E_list=array(E_list)
th_list=array(th_list)

for i in range(len(e_list)):
    if e_list[i]>1:
        e_list[i]=inf


alph_uniq=list(set(alph_list))
plt.figure()
plt.grid()
for alph in alph_uniq:
    beta_plot=[]
    a_plot=[]
    indices = [i for i, x in enumerate(alph_list) if x == alph]
    for j in indices:
        beta_plot.append(beta_list[j])
        a_plot.append(a_list[j])
    plt.plot(beta_plot, a_plot, '.-')

plt.xlabel(r'$\beta$')
plt.ylabel(r'$a$')
plt.show()

beta_uniq=list(set(beta_list))
plt.figure()
plt.grid()
for b in beta_uniq:
    alph_plot=[]
    a_plot=[]
    indices = [i for i, x in enumerate(beta_list) if x == b]
    for j in indices:
        alph_plot.append(alph_list[j])
        a_plot.append(a_list[j])
    plt.plot(alph_plot, a_plot, '.-')

plt.xlabel(r'$\alpha$')
plt.ylabel(r'$a$')
plt.show()

beta_uniq=list(set(beta_list))
plt.figure()
plt.grid()
for b in beta_uniq:
    alph_plot=[]
    e_plot=[]
    indices = [i for i, x in enumerate(beta_list) if x == b]
    for j in indices:
        alph_plot.append(alph_list[j])
        e_plot.append(e_list[j])
    plt.plot(alph_plot, e_plot, '.-')

plt.xlabel(r'$\alpha$')
plt.ylabel(r'$e$')
plt.show()

alph_uniq=list(set(alph_list))
plt.figure()
plt.grid()
for alph in alph_uniq:
    beta_plot=[]
    e_plot=[]
    indices = [i for i, x in enumerate(alph_list) if x == alph]
    for j in indices:
        beta_plot.append(beta_list[j])
        e_plot.append(e_list[j])
    plt.plot(beta_plot, log10(e_plot), '.-')

plt.xlabel(r'$\beta$')
plt.ylabel(r'$e$')
plt.show()


#f=interpolate.interp2d(beta_list, alph_list, e_list, kind='linear')
#
#xnew=linspace(min(beta_list), max(beta_list), 100)
#ynew=linspace(min(alph_list), max(alph_list), 100)
#znew=f(xnew, ynew)
#
#plt.figure()
#plt.imshow(znew, extent=(min(beta_list),max(beta_list),min(alph_list),max(alph_list)), origin='lower')
#plt.scatter(beta_list, alph_list, c=e_list)
#plt.show()
#
#
#f=interpolate.interp2d(beta_list, alph_list, a_list, kind='linear')
#
#xnew=linspace(min(beta_list), max(beta_list), 100)
#ynew=linspace(min(alph_list), max(alph_list), 100)
#znew=f(xnew, ynew)
#
#plt.figure()
#plt.imshow(znew, extent=(min(beta_list),max(beta_list),min(alph_list),max(alph_list)), origin='lower')
#plt.scatter(beta_list, alph_list, c=a_list)
#plt.show()


grid_x, grid_y = np.mgrid[min(beta_list):max(beta_list):500j, min(alph_list):max(alph_list):500j]
points=column_stack((beta_list, alph_list))
grid_z1 = interpolate.griddata(points, a_list, (grid_x, grid_y), method='linear')

plt.figure()
#plt.xscale('log')
plt.scatter(beta_list, alph_list, c=a_list)
plt.imshow(grid_z1.T, extent=(min(beta_list),max(beta_list),min(alph_list),max(alph_list)), origin='lower')
plt.show()

