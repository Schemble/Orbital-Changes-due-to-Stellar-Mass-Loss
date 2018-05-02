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

#lattice_points=[]
data_points=[]
#with open('grid_data.csv') as f:
#    for line in f.readlines():
#        l=line.split(',')
#        alph_lattice.append(float(l[0]))
#        beta_lattice.append(log10(float(l[1])))
#        a_lattice.append(float(l[2]))
#        e_lattice.append(float(l[3]))
#        E_lattice.append(float(l[4]))
#        th_lattice.append(float(l[5]))
#        lattice_points.append([float(l[0]),log10(float(l[1])), float(l[2]), float(l[3]), float(l[4]), float(l[5])])
#alph_lattice=array(alph_lattice[1:])
#beta_lattice=log10(array(beta_lattice[1:]))
#a_lattice=log10(array(a_lattice[1:]))
#e_lattice=array(e_lattice[1:])
#E_lattice=array(E_lattice[1:])
#th_lattice=array(th_lattice[1:])



with open('data2.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_list.append(float(l[0]))
        beta_list.append(float(l[1]))
        a_list.append(float(l[2]))
        e_list.append(float(l[3]))
#        E_list.append(float(l[4]))
#        th_list.append(float(l[5]))
        data_points.append([float(l[0]), float(l[1]), float(l[2]), float(l[3]), float(l[4]), float(l[5])])
data_points=array(data_points) 
alph_list=array(alph_list)
beta_list=array(beta_list)
#a_list=log10(array(a_list))
#e_list=array(e_list)
#E_list=array(E_list)
#th_list=array(th_list)
xdifflim=0.25
ydifflim=0.05
i=0
while i <len(alph_list):
   if all(alph_list[(i+1):]!=alph_list[i]) and all(alph_list[:i]!=alph_list[i]) and all(beta_list[(i+1):]!=beta_list[i]) and all(beta_list[:i]!=beta_list[i]):
       data_points=delete(data_points, i, 0)
       alph_list=delete(alph_list, i)
       beta_list=delete(beta_list, i)
   i+=1
   




#i=0    
#while i<len(data_points):
#    if any(data_points[i,:2]==data_points[i+1:,:2]):
#        print(data_points[i,:2])
#        print(data_points[i+1:,:2])
#        data_points=delete(data_points, i, 0)
#    i+=1



#
#alph_uniq=list(set(alph_list))
#alph_uniq.sort()
#beta_uniq=list(set(beta_list))
#beta_uniq.sort()
#beta_uniq = [ round(elem, 2) for elem in beta_uniq ]

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

def interpolate(alpha, beta):
    '''
    Find closest point
    '''
    print(alpha, beta)
    done=1
    maxdist=sqrt(0.05**2+0.25**2)
    i=0
    xline=0
    yline=0
    target=array([alpha, beta])
    diff=abs(data_points[:,:2]-array([alpha, beta]))
    dist=sqrt(diff[:, 0]**2+diff[:,1]**2)
    while 1:
        point_c1=data_points[where(dist==sort(dist)[i])[0][0]]

        if all(point_c1[:2]==target):
            return point_c1[1:]
        if any(point_c1==inf):
            return [inf ,inf]
        '''
        Find next closest point that is on the same line as first point.
        '''
        j=1
        while 1:
            
            point_c2=data_points[where(dist==sort(dist)[i+j])[0][0]]
            sign12=(point_c1[:2]-target)*(point_c2[:2]-target)
            if any(point_c2==inf):
                return [inf ,inf]
            #print(point_c1,point_c2,sign12)
            if sign12[0]<0 and point_c1[1]==point_c2[1]:
                xline=1
                break
            elif sign12[1]<0 and point_c1[0]==point_c2[0]:
                yline=1
                break
            elif sort(dist)[i+j]>maxdist:
                break
            j+=1
            
            if i+j==len(data_points)-1:
                break
        if sort(dist)[i+j]>maxdist:
                j=1
                i+=1
                continue
        break
    if any(sign12==0):
        points=[point_c1, point_c2]
        f=linint(beta, alpha, points)
        return f
    '''
    Find closest point outside previous line and on opposite side of target
    '''
    k=0
    l=1
    while done:
        point_c3=data_points[where(dist==sort(dist)[k])[0][0]]
        sign13=(point_c1[:2]-target)*(point_c3[:2]-target)
        if any(point_c3==inf):
            return [inf ,inf]
        if sort(dist)[k]>maxdist:
            return
            
        
        if xline==1 and sign13[1]<=0:  
            while 1:
                point_c4=data_points[where(dist==sort(dist)[k+l])[0][0]]
                sign34=(point_c3[:2]-target)*(point_c4[:2]-target)
                #print(point_c3[:2], point_c4[:2])
                if any(point_c3==inf):
                    return [inf ,inf]
                if sign34[0]<0 and point_c3[1]==point_c4[1]:
                    break
                elif sort(dist)[k+l]>maxdist:
                    break
                l+=1
            if sort(dist)[k+l]>maxdist:
                l=1
                k+=1
                
                continue
    
            break

        elif yline==1 and sign13[0]<=0: 
            while 1:
                point_c4=data_points[where(dist==sort(dist)[k+l])[0][0]]
                sign34=(point_c3[:2]-target)*(point_c4[:2]-target)
                #print(point_c3[:2], point_c4[:2])
                if any(point_c3==inf):
                    return [inf ,inf]
                if sign34[1]<0 and point_c3[0]==point_c4[0]:
                    break
                elif sort(dist)[k+l]>maxdist:
                    break
                l+=1
            if sort(dist)[k+l]>maxdist:
                l=1
                k+=1
                continue
               
            break
        k+=1
    '''
    interpolate
    '''
    points=[point_c1, point_c2, point_c3, point_c4]
    f=Bilint(beta, alpha, points)
    return(f)

        

    
'''
Compare interpolation to simulation at random points
'''
#e_int=[]
#e_sim=[]
#a_int=[]
#a_sim=[]
#alph_plot=[]
#beta_plot=[]
#for i in range(1):
#    
#    beta=random.uniform(-1, 4)
#    alpha=random.uniform(0.1, 0.95)
#    #print(i, beta)
#    f=interpolate(alpha, beta)
#    print(f)
#    if type(f)!=str:
#        a_int.append(f[0])
#        e_int.append(f[1])
#        alph_plot.append(alpha)
#        beta_plot.append(beta)
#        sim=TP.TestParticle(alpha=alpha, beta=10**beta)
#        sim.runrk4()
#        a_sim.append(log10(sim.GetA()))
#
#plt.figure()
#plt.ymin=0
#plt.ymax=1
#plt.xmin=-1
#plt.xmax=4
#plt.scatter(beta_plot, alph_plot, c=array(a_int)/array(a_sim))
#plt.xlabel(r'$\log\beta$')
#plt.ylabel(r'$\alpha$')
#plt.colorbar(label='(a_interpolated/a_simulated)')
#plt.show()
'''
Make contour plots
'''

x=linspace(-1, 3.9, 100)
y=linspace(0.1, 0.95, 100)
za=[]
ze=[]
for i in x:
    zya=[]
    zye=[]
    for j in y:
        z=interpolate(j, i)
        zya.append(z[0])
        zye.append(z[1])
    za.append(zya)
    ze.append(zye)
za=array(za)
ze=array(ze)

plt.figure()
plt.xlabel(r'$\log\beta$')
plt.ylabel(r'$\alpha$')
#plt.scatter(beta_list, alph_list, c=a_list,vmin=0, vmax=6)
#plt.colorbar(label=r'$\loga_data$')
plt.imshow(za.T,vmin=0, vmax=6, extent=(min(x), max(x), min(y), max(y)), origin='lower', aspect='auto')
plt.colorbar(label=r'$\loga_in$')
plt.contour(za.T, extent=(min(x), max(x), min(y), max(y)))
plt.show()

plt.figure()
plt.xlabel(r'$\log\beta$')
plt.ylabel(r'$\alpha$')
#plt.scatter(beta_list, alph_list, c=e_list,vmin=0, vmax=1)
#plt.colorbar(label=r'$e_data$')
plt.imshow(ze.T,vmin=0, vmax=1, extent=(min(x), max(x), min(y), max(y)), origin='lower', aspect='auto')
plt.colorbar(label=r'$e_int$')
plt.contour(ze.T, extent=(min(x), max(x), min(y), max(y)))
plt.show()

'''
troubleshoot
'''

#print(interpolate(0.194444444444,1.17777777778))
























 
    
    
