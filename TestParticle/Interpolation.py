#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 10:42:42 2018

@author: John
"""

from scipy import *
from matplotlib import pyplot as plt
from scipy.stats import linregress
import TestParticle as TP
import itertools

alph_grid=[]
beta_grid=[]
a_grid=[]
e_grid=[]
E_grid=[]
th_grid=[]

alph_lattice=[]
beta_lattice=[]
a_lattice=[]
e_lattice=[]
E_lattice=[]
th_lattice=[]

alph_list=[]
beta_list=[]
a_list=[]
e_list=[]
E_list=[]
th_list=[]

lattice_points=[]
data_points=[]
with open('grid_data.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_lattice.append(float(l[0]))
        beta_lattice.append(log10(float(l[1])))
#        a_lattice.append(float(l[2]))
#        e_lattice.append(float(l[3]))
#        E_lattice.append(float(l[4]))
#        th_lattice.append(float(l[5]))
        lattice_points.append([float(l[0]),log10(float(l[1])), float(l[2]), float(l[3]), float(l[4]), float(l[5])])
#alph_lattice=array(alph_lattice[1:])
#beta_lattice=log10(array(beta_lattice[1:]))
#a_lattice=log10(array(a_lattice[1:]))
#e_lattice=array(e_lattice[1:])
#E_lattice=array(E_lattice[1:])
#th_lattice=array(th_lattice[1:])



with open('data.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_list.append(float(l[0]))
#        beta_list.append(log10(float(l[1])))
#        a_list.append(float(l[2]))
#        e_list.append(float(l[3]))
#        E_list.append(float(l[4]))
#        th_list.append(float(l[5]))
        data_points.append([float(l[0]), float(l[1]), float(l[2]), float(l[3]), float(l[4]), float(l[5])])

#alph_list=array(alph_list)
#beta_list=array(beta_list)
#a_list=log10(array(a_list))
#e_list=array(e_list)
#E_list=array(E_list)
#th_list=array(th_list)
        



data_points=array(data_points)  
#i=0    
#while i<len(data_points):
#    if any(data_points[i,:2]==data_points[i+1:,:2]):
#        print(data_points[i,:2])
#        print(data_points[i+1:,:2])
#        data_points=delete(data_points, i, 0)
#    i+=1



data_points=array(data_points)
alph_uniq=list(set(alph_lattice))
alph_uniq.sort()
beta_uniq=list(set(beta_lattice))
beta_uniq.sort()
beta_uniq = [ round(elem, 2) for elem in beta_uniq ]


def Bilint(x, y ,points):
    '''
    points=[[x11, y11, f11], 
            [x12, y12, f12], 
            [x21, y21, f21], 
            [x22, y22, f22]]   
    '''
        
    points = sorted(points, key=lambda x: x[0])
    points = sorted(points, key=lambda x: x[1])
    x11=points[0][1]
    y11=points[0][0]
    f11=array(points[0][2:])
    x12=points[1][1]
    y12=points[1][0]
    f12=array(points[1][2:])
    x21=points[2][1]
    y21=points[2][0]
    f21=array(points[2][2:])
    x22=points[3][1]
    y22=points[3][0]
    f22=array(points[3][2:])
    #print(x11, y11)
    if any(f11==inf) or any(f12==inf) or any(f21==inf) or any(f22==inf):
        return 'unbound'
    if (y11==y21 and y12==y22):
        
        y1=y11
        y2=y22
        Q1=(f11*(x21-x)+f21*(x-x11))/(x21-x11)
        Q2=(f12*(x22-x)+f22*(x-x12))/(x22-x12)
        f=(Q1*(y2-y)+Q2*(y-y1))/(y2-y1)
    elif (x11==x12 and x21==x22):
        x1=x11
        x2=x22
        Q1=(f11*(y12-y)+f12*(y-y11))/(y12-y11)
        Q2=(f21*(y22-y)+f22*(y-y21))/(y22-y21)
        f=(Q1*(x2-x)+Q2*(x-x1))/(x2-x1)
    elif (y11==y22 and y12==y21):
        y1=y11
        y2=y21
        Q1=(f11*(x22-x)+f22*(x-x11))/(x22-x11)
        Q2=(f12*(x21-x)+f21*(x-x12))/(x21-x12)
        f=(Q1*(y2-y)+Q2*(y-y1))/(y2-y1)
    elif (x11==x21 and x12==x22):
        x1=x11
        x2=x12
        Q1=(f11*(y21-y)+f21*(y-y11))/(y21-y11)
        Q2=(f12*(y22-y)+f22*(y-y12))/(y22-y12)
        f=(Q1*(x2-x)+Q2*(x-x1))/(x2-x1)
    return f
def interpolate(beta, alpha):
    '''
    find the lattice values closest to point
    '''
    print(beta, alpha)
    bdiff=abs(array(beta_uniq)-beta)
    b1=beta_uniq[argmin(bdiff)]
    b2=beta_uniq[int(where(bdiff==sort(bdiff)[1])[0])]
    blim=[b1, b2]
    blim.sort()
    adiff=abs(array(alph_uniq)-alpha)
    a1=alph_uniq[argmin(adiff)]
    a2=alph_uniq[int(where(adiff==sort(adiff)[1])[0])]
    alim=[a1, a2]
    alim.sort()
    '''
    Find the values of all points along closest lattice lines
    '''
#    pointsb1=[]
#    pointsb2=[]
#    pointsa1=[]
#    pointsa2=[]
#    
#    a1indices = [i for i, x in enumerate(data_points[:,0]) if x == a1]
#    a2indices = [i for i, x in enumerate(data_points[:,0]) if x == a2]
#    b1indices = [i for i, x in enumerate(data_points[:,1]) if x == b1]
#    b2indices = [i for i, x in enumerate(data_points[:,1]) if x == b2]
    pointsb1  = [x for x in data_points if x[1]==b1]
    pointsb2  = [x for x in data_points if x[1]==b2]
    pointsa1  = [x for x in data_points if x[0]==a1]
    pointsa2  = [x for x in data_points if x[0]==a2]
    
#    for j in b1indices:        
#
#        if alpha>=alim[0] and alpha<=alim[1]:
##            beta=beta_list[j]
##            a=a_list[j]
##            e=e_list[j]
##            E=E_list[j]
##            th=th_list[j]
#            pointsb1.append(data_points[j])
#            
#    for j in b2indices:
#
#        if alpha>=alim[0] and alpha<=alim[1]:
##            beta=beta_list[j]
##            a=a_list[j]
##            e=e_list[j]
##            E=E_list[j]
##            th=th_list[j]
#            pointsb2.append(data_points[j])
#        
#    for j in a1indices:
#
#        if beta>=blim[0] and beta<=blim[1]:
##            alpha=alph_list[j]
##            a=a_list[j]
##            e=e_list[j]
##            E=E_list[j]
##            th=th_list[j]
#            pointsa1.append(data_points[j])
#        
#    for j in a2indices:
#
#        if beta>=blim[0] and beta<=blim[1]:
##            alpha=alph_list[j]
##            a=a_list[j]
##            e=e_list[j]
##            E=E_list[j]
##            th=th_list[j]
#            pointsa2.append(data_points[j])

    '''
    Find closest points
    '''

    b1diff=[abs(x[0]-alpha) for x in pointsb1]
    pb11=pointsb1[argmin(b1diff)]
    if pb11[0]<=alpha:
        pointsb1=[x for x in pointsb1 if x[0]>=alpha]
    elif pb11[0]>=alpha:
        pointsb1=[x for x in pointsb1 if x[0]<=alpha]

    b1diff=[abs(x[0]-alpha) for x in pointsb1]
    pb12=pointsb1[argmin(b1diff)]
    deltab1=abs(pb11[0]-pb12[0])

    
    
    b2diff=[abs(x[0]-alpha) for x in pointsb2]
    pb21=pointsb2[argmin(b2diff)]
    if pb21[0]<=alpha:
        pointsb2=[x for x in pointsb2 if x[0]>=alpha]
    elif pb21[0]>=alpha:
        pointsb2=[x for x in pointsb2 if x[0]<=alpha]
    b2diff=[abs(x[0]-alpha) for x in pointsb2]
    pb22=pointsb2[argmin(b2diff)]
    deltab2=abs(pb21[0]-pb22[0])

        
        
    a1diff=[abs(x[1]-beta) for x in pointsa1]
    pa11=pointsa1[argmin(a1diff)]
    if pa11[1]<=beta:
        pointsa1=[x for x in pointsa1 if x[1]>=beta]
    elif pa11[1]>=beta:
        pointsa1=[x for x in pointsa1 if x[1]<=beta]
    a1diff=[abs(x[1]-beta) for x in pointsa1]
    pa12=pointsa1[argmin(a1diff)]
    deltaa1=abs(pa11[1]-pa12[1])

        
        
        
    a2diff=[abs(x[1]-beta) for x in pointsa2]
    pa21=pointsa2[argmin(a2diff)]
    if pa21[1]<=beta:
        pointsa2=[x for x in pointsa2 if x[1]>=beta]
    elif pa21[1]>=beta:
        pointsa2=[x for x in pointsa2 if x[1]<=beta]
    a2diff=[abs(x[1]-beta) for x in pointsa2]
    pa22=pointsa2[argmin(a2diff)]
    deltaa2=abs(pa21[1]-pa22[1])

        
        
        
    deltas=[deltab1, deltab2, deltaa1, deltaa2]
    
    
    if min(deltas)==deltab1 or min(deltas)==deltab2:
        points=[pb11, pb12, pb21, pb22]
    elif min(deltas)==deltaa1 or min(deltas)==deltaa2:
        points=[pa11, pa12, pa21, pa22]
        

    '''
    interpolate
    '''
    f=Bilint(beta, alpha, points)
    return(f)
#interpolate(2.2101614945686077, 0.7058482368337547)
e_int=[]
e_sim=[]
a_int=[]
a_sim=[]
alph_plot=[]
beta_plot=[]
for i in range(1000):
    
    beta=random.uniform(-1, 4)
    alpha=random.uniform(0.1, 0.95)
    print(i, beta)
    f=interpolate(beta, alpha)
    if type(f)!=str:
        a_int.append(f[0])
        e_int.append(f[1])
        alph_plot.append(alpha)
        beta_plot.append(beta)
        sim=TP.TestParticle(alpha=alpha, beta=10**beta)
        sim.runrk4()
        a_sim.append(log10(sim.GetA()))

plt.figure()
plt.ymin=0
plt.ymax=1
plt.xmin=-1
plt.xmax=4
plt.scatter(beta_plot, alph_plot, c=array(a_int)/array(a_sim))
plt.xlabel(r'$\log\beta$')
plt.ylabel(r'$\alpha$')
plt.colorbar(label='(a_interpolated/a_simulated)')
plt.show()
        
    
    
