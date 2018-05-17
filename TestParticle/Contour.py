#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:16:02 2018

@author: John
"""

from scipy import *
from matplotlib import pyplot as plt
from scipy.stats import linregress
import TestParticle as TP

alph_list=[]
beta_list=[]
a_list=[]
e_list=[]
E_list=[]
th_list=[]

data_points=[]

with open('grid_data2.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        #alph_list.append(float(l[0]))
        #beta_list.append(float(l[1]))
        #a_list.append(float(l[2]))
        #e_list.append(float(l[3]))
#        E_list.append(float(l[4]))
#        th_list.append(float(l[5]))
        data_points.append([float(l[0]), log10(float(l[1])), log10(float(l[2])), float(l[3]), float(l[4]), float(l[5])])




#with open('grid_data3.csv') as f:
#    for line in f.readlines():
#        l=line.split(',')
#        #alph_list.append(float(l[0]))
#        #beta_list.append(float(l[1]))
#        #a_list.append(float(l[2]))
#        #e_list.append(float(l[3]))
##        E_list.append(float(l[4]))
##        th_list.append(float(l[5]))
#        data_points.append([float(l[0]), log10(float(l[1])), log10(float(l[2])), float(l[3]), float(l[4]), float(l[5])])


#with open('grid_data3.1.csv') as f:
#    for line in f.readlines():
#        l=line.split(',')
#        #alph_list.append(float(l[0]))
#        #beta_list.append(float(l[1]))
#        #a_list.append(float(l[2]))
#        #e_list.append(float(l[3]))
##        E_list.append(float(l[4]))
##        th_list.append(float(l[5]))
#        data_points.append([float(l[0]), log10(float(l[1])), log10(float(l[2])), float(l[3]), float(l[4]), float(l[5])])
#with open('extra_e_data2(4).csv') as f:
#    for line in f.readlines():
#        l=line.split(',')
#        #alph_list.append(float(l[0]))
#        #beta_list.append(float(l[1]))
#        #a_list.append(float(l[2]))
#        #e_list.append(float(l[3]))
##        E_list.append(float(l[4]))
##        th_list.append(float(l[5]))
#        data_points.append([float(l[0]), log10(float(l[1])), log10(float(l[2])), float(l[3]), float(l[4]), float(l[5])])
#with open('extra2_a_data(4).csv') as f:
#    for line in f.readlines():
#        l=line.split(',')
#        #alph_list.append(float(l[0]))
#        #beta_list.append(float(l[1]))
#        #a_list.append(float(l[2]))
#        #e_list.append(float(l[3]))
##        E_list.append(float(l[4]))
##        th_list.append(float(l[5]))
#        data_points.append([float(l[0]), log10(float(l[1])), log10(float(l[2])), float(l[3]), float(l[4]), float(l[5])])
#with open('extra_a_data(4).csv') as f:
#    for line in f.readlines():
#        l=line.split(',')
#        #alph_list.append(float(l[0]))
#        #beta_list.append(float(l[1]))
#        #a_list.append(float(l[2]))
#        #e_list.append(float(l[3]))
##        E_list.append(float(l[4]))
##        th_list.append(float(l[5]))
#        data_points.append([float(l[0]), log10(float(l[1])), log10(float(l[2])), float(l[3]), float(l[4]), float(l[5])])


data_points=array(data_points) 

#alph_list=array(alph_list)
#beta_list=array(beta_list)
data_points = array(sorted(data_points, key=lambda x: x[0]))
data_points = array(sorted(data_points, key=lambda x: x[1]))
i=0
while i+1 <len(data_points):
    if all(data_points[i, :2]==data_points[i+1,:2]):
       data_points=delete(data_points, i, 0)
       
    elif all(data_points[i,0]!=data_points[i+1:,0]) and all(data_points[i,1]!=data_points[i+1:,1]):
        data_points=delete(data_points, i, 0)
        
    i+=1
alph_list=data_points[:,0]
beta_list=data_points[:,1]    
alph_uniq=list(set(alph_list))
alph_uniq.sort()
beta_uniq=list(set(beta_list))
beta_uniq.sort()
#beta_uniq = [ round(elem, 2) for elem in beta_uniq ]

def backlinint(value, x1, x2, f1, f2):
    f=value
    return (x1*(f2-f)+x2*(f-f1))/(f2-f1)


def contour(value, idx):
    beta=[]
    alpha=[]
    x_grid=[]
    y_grid=[]
    c=[]
    for b in beta_uniq:
        line=data_points[where(data_points[:,1]==b)]
        
        diff=line[:,idx]-value
        if any(diff<=0) and any(diff>=0):
            diff=abs(diff)
            p1=line[where(diff==sort(diff)[0])][0]
            
            p2=line[where(diff==sort(diff)[1])][0]
            i=2
            while (p2[idx]-value)*(p1[idx]-value)>0:
                p2=line[where(diff==sort(diff)[i])][0]
                i+=1
        
            alpha.append(backlinint(value, p1[0], p2[0], p1[idx], p2[idx]))
            beta.append(b)
            x_grid.append(b)
            c.append(abs(p1[0]-p2[0]))
    for alph in alph_uniq:
        line=data_points[where(data_points[:,0]==alph)]
        diff=line[:,idx]-value
        if any(diff<=0) and any(diff>=0):
            diff=abs(diff)
            p1=line[where(diff==sort(diff)[0])][0]
            
            p2=line[where(diff==sort(diff)[1])][0]
            i=2
            while (p2[idx]-value)*(p1[idx]-value)>0:
                p2=line[where(diff==sort(diff)[i])][0]
                i+=1
        
            beta.append(backlinint(value, p1[1], p2[1], p1[idx], p2[idx]))
            alpha.append(alph)
            y_grid.append(alph)

    return alpha, beta, x_grid, y_grid

#alpha_plot, beta_plot, x_grid, y_grid, c=contour(0.4, 3)
e_list=arange(0, 1,0.1)
#alpha_plot = [x for _,x in sorted(zip(beta_plot,alpha_plot))]
#beta_plot.sort()
fig, ax = plt.subplots()
#ax.set_xticks(x_grid)
#ax.set_yticks(y_grid)
#ax.xaxis.grid(True)
#ax.yaxis.grid(True)
for e in e_list:
    alpha_plot, beta_plot, x_grid, y_grid=contour(e, 3)
    alpha_plot = [x for _,x in sorted(zip(beta_plot,alpha_plot))]
    beta_plot.sort()
    plt.plot(beta_plot, alpha_plot,'.-', label='e={:.1f}'.format(e))
    print(len(beta_plot))
plt.grid()
plt.ylabel(r'$\alpha$')
plt.xlabel(r'$\log\beta$')
plt.legend()
plt.show()

#alpha_plot, beta_plot, x_grid, y_grid, c=contour(0.4, 3)
a_list=arange(0, 1.5, 0.1)
#alpha_plot = [x for _,x in sorted(zip(beta_plot,alpha_plot))]
#beta_plot.sort()
fig, ax = plt.subplots()
#ax.set_xticks(x_grid)
#ax.set_yticks(y_grid)
#ax.xaxis.grid(True)
#ax.yaxis.grid(True)
for a in a_list:
    alpha_plot, beta_plot, x_grid, y_grid=contour(a, 2)
    alpha_plot = [x for _,x in sorted(zip(beta_plot,alpha_plot))]
    beta_plot.sort()
    plt.plot(beta_plot, alpha_plot,'.-', label='a={:.2f}'.format(a))
    print(len(beta_plot))
plt.grid()
plt.ylabel(r'$\alpha$')
plt.xlabel(r'$\log\beta$')
plt.legend()
plt.show()







def backlinint(value, x1, x2, f1, f2):

    f=value
    return (x1*(f2-f)+x2*(f-f1))/(f2-f1)
    
    
def linint(x, y, points):
    x1=points[0][1]
    y1=points[0][0]
    x2=points[1][1]
    y2=points[1][0]
    f1=array(points[0][2:])
    f2=array(points[1][2:])
    
    if x1==x2:
        f=(f1*(y2-y)+f2*(y-y1))/(y2-y1)
    elif y1==y2:
        f=(f1*(x2-x)+f2*(x-x1))/(x2-x1)
    return f
def Bilint(x, y ,points):
    
#    points=[[x11, y11, f11], 
#            [x12, y12, f12], 
#            [x21, y21, f21], 
#            [x22, y22, f22]]   
    
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
        return [inf, inf]
    if x11==x and y11==y:
        return f11
    if x12==x and y12==y:
        return f12
    if x21==x and y21==y:
        return f21
    if x22==x and y22==y:
        return f22
    
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




