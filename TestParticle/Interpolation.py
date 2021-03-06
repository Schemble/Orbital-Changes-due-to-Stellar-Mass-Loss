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
with open('grid_data3.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_lattice.append(float(l[0]))
        beta_lattice.append(log10(float(l[1])))
#        a_lattice.append(float(l[2]))
#        e_lattice.append(float(l[3]))
#        E_lattice.append(float(l[4]))
#        th_lattice.append(float(l[5]))
        lattice_points.append([float(l[0]),log10(float(l[1])), log10(float(l[2])), float(l[3]), float(l[4]), float(l[5])])

#with open('grid_data3.1.csv') as f:
#    for line in f.readlines():
#        l=line.split(',')
#        alph_lattice.append(float(l[0]))
#        beta_lattice.append(log10(float(l[1])))
##        a_lattice.append(float(l[2]))
##        e_lattice.append(float(l[3]))
##        E_lattice.append(float(l[4]))
##        th_lattice.append(float(l[5]))
#        lattice_points.append([float(l[0]),log10(float(l[1])), log10(float(l[2])), float(l[3]), float(l[4]), float(l[5])])


#alph_lattice=array(alph_lattice[1:])
#beta_lattice=log10(array(beta_lattice[1:]))
#a_lattice=log10(array(a_lattice[1:]))
#e_lattice=array(e_lattice[1:])
#E_lattice=array(E_lattice[1:])
#th_lattice=array(th_lattice[1:])



with open('grid_data3.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_list.append(float(l[0]))
        beta_list.append(log10(float(l[1])))
        a_list.append(float(l[2]))
        e_list.append(float(l[3]))
#        E_list.append(float(l[4]))
#        th_list.append(float(l[5]))
        data_points.append([float(l[0]), log10(float(l[1])), log10(float(l[2])), float(l[3]), float(l[4]), float(l[5])])
#with open('grid_data3.1.csv') as f:
#    for line in f.readlines():
#        l=line.split(',')
#        alph_list.append(float(l[0]))
#        beta_list.append(log10(float(l[1])))
#        a_list.append(float(l[2]))
#        e_list.append(float(l[3]))
##        E_list.append(float(l[4]))
##        th_list.append(float(l[5]))
#        data_points.append([float(l[0]), log10(float(l[1])), log10(float(l[2])), float(l[3]), float(l[4]), float(l[5])])


#alph_list=array(alph_list)
#beta_list=array(beta_list)
#a_list=log10(array(a_list))
#e_list=array(e_list)
#E_list=array(E_list)
#th_list=array(th_list)
        

lattice_points = array(sorted(lattice_points, key=lambda x: x[0]))
lattice_points = array(sorted(lattice_points, key=lambda x: x[1]))

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
#beta_uniq = [ round(elem, 2) for elem in beta_uniq ]


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
def interpolate(beta, alpha):
    '''
    find the lattice values closest to point
    '''
#    print(beta, alpha)
    bdiff=abs(array(beta_uniq)-beta)
    b1=beta_uniq[argmin(bdiff)]

    if len(where(bdiff==sort(bdiff)[1])[0])>1:
        b2=beta_uniq[int(where(bdiff==sort(bdiff)[1])[0][1])]
    elif len(where(bdiff==sort(bdiff)[1])[0])==1:
        b2=beta_uniq[int(where(bdiff==sort(bdiff)[1])[0])]
    blim=[b1, b2]
    blim.sort()
    adiff=abs(array(alph_uniq)-alpha)

    a1=alph_uniq[argmin(adiff)]
    if len(where(adiff==sort(adiff)[1])[0])>1:
        a2=alph_uniq[int(where(adiff==sort(adiff)[1])[0][1])]
    elif len(where(adiff==sort(adiff)[1])[0])==1:
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
    if pb11[0]<alpha:
        pointsb1=[x for x in pointsb1 if x[0]>=alpha]
    elif pb11[0]>alpha:
        pointsb1=[x for x in pointsb1 if x[0]<=alpha]
    elif pb11[0]==alpha:
        pointsb1=[x for x in pointsb1 if x[0]!=alpha]
    b1diff=[abs(x[0]-alpha) for x in pointsb1]
    pb12=pointsb1[argmin(b1diff)]
    deltab1=abs(pb11[0]-pb12[0])

    
    
    b2diff=[abs(x[0]-alpha) for x in pointsb2]
    pb21=pointsb2[argmin(b2diff)]
    if pb21[0]<alpha:
        pointsb2=[x for x in pointsb2 if x[0]>=alpha]
    elif pb21[0]>alpha:
        pointsb2=[x for x in pointsb2 if x[0]<=alpha]
    elif pb21[0]==alpha:
        pointsb2=[x for x in pointsb2 if x[0]!=alpha]
    b2diff=[abs(x[0]-alpha) for x in pointsb2]
    pb22=pointsb2[argmin(b2diff)]
    deltab2=abs(pb21[0]-pb22[0])

        
        
    a1diff=[abs(x[1]-beta) for x in pointsa1]
    pa11=pointsa1[argmin(a1diff)]
    if pa11[1]<beta:
        pointsa1=[x for x in pointsa1 if x[1]>=beta]
    elif pa11[1]>beta:
        pointsa1=[x for x in pointsa1 if x[1]<=beta]
    elif pa11[1]==beta:
        pointsa1=[x for x in pointsa1 if x[1]!=beta]
    a1diff=[abs(x[1]-beta) for x in pointsa1]
    pa12=pointsa1[argmin(a1diff)]
    deltaa1=abs(pa11[1]-pa12[1])

        
        
        
    a2diff=[abs(x[1]-beta) for x in pointsa2]
    pa21=pointsa2[argmin(a2diff)]
    if pa21[1]<beta:
        pointsa2=[x for x in pointsa2 if x[1]>=beta]
    elif pa21[1]>beta:
        pointsa2=[x for x in pointsa2 if x[1]<=beta]
    elif pa21[1]==beta:
        pointsa2=[x for x in pointsa2 if x[1]!=beta]
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
    
'''
Compare interpolation to simulation at random points
'''
#e_int=[]
##e_sim=[]
#a_int=[]
##a_sim=[]
#alph_plot=[]
#beta_plot=[]
#for i in range(10):
#    
#    beta=random.uniform(-1, 4)
#    alpha=random.uniform(0.1, 0.95)
#    print(i, beta)
#    f=interpolate(beta, alpha)
#    if type(f)!=str:
#        a_int.append(f[0])
#        e_int.append(f[1])
#        alph_plot.append(alpha)
#        beta_plot.append(beta)
#        #sim=TP.TestParticle(alpha=alpha, beta=10**beta)
#        #sim.runrk4()
#        #a_sim.append(log10(sim.GetA()))
#
#plt.figure()
#plt.ymin=0
#plt.ymax=1
#plt.xmin=-1
#plt.xmax=4
#plt.scatter(beta_plot, alph_plot)#, c=array(a_int)/array(a_sim))
#plt.xlabel(r'$\log\beta$')
#plt.ylabel(r'$\alpha$')
#plt.colorbar(label='(a_interpolated/a_simulated)')
#plt.show()
'''
Error Check
'''
#
#beta_list=arange(min(beta_uniq), max(beta_uniq), 0.5)
#alph_list=arange(min(alph_uniq), max(alph_uniq), 0.2)
#
#f1 = plt.figure()
#f2 = plt.figure()
#ax1 = f1.add_subplot(111)
#f1.subplots_adjust(right=0.65)
#ax2 = f2.add_subplot(111)
#f2.subplots_adjust(right=0.65)
#ax1.grid()
#ax2.grid()
#for i in range(5):
#    a=random.uniform(min(alph_uniq), max(alph_uniq))
#    
#    a_plot=[]
#    e_plot=[]
#    bint=linspace(min(beta_uniq), max(beta_uniq), 100)
#    for b in bint:
#        h=interpolate(b, a)
#        a_plot.append(h[0])
#        e_plot.append(h[1])
#    ax1.plot(bint, a_plot,'.-', label=r'$\alpha$={}'.format(a))
#    ax2.plot(bint, e_plot,'.-', label=r'$\alpha$={}'.format(a))
#    
#    a_sim=[]
#    e_sim=[]
#    beta_e=[]
#    for b in beta_list:
#        ex=TP.TestParticle(alpha=a, beta=10**b)
#        ex.runrk4()
#        a_sim.append(log10(ex.GetA()))
#        if ex.GetEc()<1:
#            e_sim.append(ex.GetEc())
#            beta_e.append(b)
#    ax1.plot(beta_list, a_sim,'o', label=r'$\alpha$={}'.format(a))
#    ax2.plot(beta_e, e_sim,'o', label=r'$\alpha$={}'.format(a))
#ax1.set_ylabel(r'$a$')
#ax1.set_xlabel(r'$\log\beta$')
#ax2.set_ylabel(r'$e$')
#ax2.set_xlabel(r'$\log\beta$')
#ax1.legend(bbox_to_anchor=(1, 0.89), loc='upper left', ncol=1)
#ax2.legend(bbox_to_anchor=(1, 0.89), loc='upper left', ncol=1)
#
#plt.show()
#
#f1 = plt.figure()
#f2 = plt.figure()
#ax1 = f1.add_subplot(111)
#f1.subplots_adjust(right=0.65)
#ax2 = f2.add_subplot(111)
#f2.subplots_adjust(right=0.65)
#ax1.grid()
#ax2.grid()
#for i in range(5):
#    b=random.uniform(min(beta_uniq), max(beta_uniq))
#    
#    a_plot=[]
#    e_plot=[]
#    aint=linspace(min(alph_uniq), max(alph_uniq), 100)
#    for a in aint:
#        h=interpolate(b, a)
#        a_plot.append(h[0])
#        e_plot.append(h[1])
#    ax1.plot(aint, a_plot,'.-', label=r'$\log\beta$={}'.format(b))
#    ax2.plot(aint, e_plot,'.-', label=r'$\log\beta$={}'.format(b))
#    
#    a_sim=[]
#    e_sim=[]
#    alph_e=[]
#    for a in alph_list:
#        ex=TP.TestParticle(alpha=a, beta=10**b)
#        ex.runrk4()
#        a_sim.append(log10(ex.GetA()))
#        if ex.GetEc()<1:
#            e_sim.append(ex.GetEc())
#            alph_e.append(a)
#    ax1.plot(alph_list, a_sim,'o', label=r'$\log\beta$={}'.format(b))
#    ax2.plot(alph_e, e_sim,'o', label=r'$\log\beta$={}'.format(b))
#ax1.set_ylabel(r'$a$')
#ax1.set_xlabel(r'$\alpha$')
#ax2.set_ylabel(r'$e$')
#ax2.set_xlabel(r'$\alpha$')
#ax1.legend(bbox_to_anchor=(1, 0.89), loc='upper left', ncol=1)
#ax2.legend(bbox_to_anchor=(1, 0.89), loc='upper left', ncol=1)
#plt.show()

'''
troubleshoot
'''

#interpolate(3.0303030303, 0.4934556214410667)


'''
Discussion
'''


beta_plot=linspace(min(beta_uniq),max(beta_uniq))
mi=arange(1, 4, 0.2)
ai=1
mf=0.6
plt.figure()
plt.grid()
for m in mi:
    e_plot=[]
    alpha=1-mf/m
    if alpha>0.5 and alpha<max(alph_uniq):
        
        print(alpha)
        for b in beta_plot:            
            f=interpolate(b, alpha)
            e_plot.append(f[1])
        t_plot=sqrt((ai**3)/m)*10**beta_plot
        plt.plot(log10(t_plot), e_plot, label='{}'.format(m))
plt.legend()
plt.ylabel(r'$e$')
plt.xlabel(r't')
plt.show() 




















 
    
    
