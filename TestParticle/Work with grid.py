#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:25:19 2018

@author: John
"""

import TestParticle as TP
from scipy import*
from matplotlib import pyplot as plt


alph_grid=[]
beta_grid=[]
a_grid=[]
e_grid=[]
E_grid=[]
th_grid=[]

alph_list=[]
beta_list=[]
a_list=[]
e_list=[]
E_list=[]
th_list=[]

with open('grid_data3.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_grid.append(float(l[0]))
        beta_grid.append(float(l[1]))
        a_grid.append(float(l[2]))
        e_grid.append(float(l[3]))
        E_grid.append(float(l[4]))
        th_grid.append(float(l[5]))
        
with open('grid_data3.1.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_grid.append(float(l[0]))
        beta_grid.append(float(l[1]))
        a_grid.append(float(l[2]))
        e_grid.append(float(l[3]))
        E_grid.append(float(l[4]))
        th_grid.append(float(l[5]))
        

        
alph_grid=array(alph_grid)
beta_grid=array(beta_grid)
a_grid=log10(array(a_grid))
e_grid=array(e_grid)
E_grid=array(E_grid)
th_grid=array(th_grid)



alph_uniq=list(set(alph_grid))
alph_uniq.sort()
beta_uniq=list(set(beta_grid))
beta_uniq.sort()

alph_uniq = [ round(elem, 2) for elem in alph_uniq ]

def Gather(f):
    a_list.append(f.GetA())
    e_list.append(f.GetEc())
    E_list.append(f.Etot())
    th_list.append(f.Theta())
    alph_list.append(f.alpha)
    beta_list.append(f.beta)

'''
a flattening
'''

#alph_uniq=list(set(alph_list))
#alph_uniq.sort()
#tol=0.1
#beta_flat=[]
#a_flat=[]
#plt.figure()
#plt.grid()
#for alph in alph_uniq:
#    beta_plot=[]
#    a_plot=[]
#    indices = [i for i, x in enumerate(alph_list) if x == alph]
#    ai=-inf
#    bi=-inf
#    c=0
#    for j in indices:
#        beta_plot.append(beta_list[j])
#        a_plot.append(a_list[j])
#        af=a_list[j]
#        h=abs(bi-beta_list[j])
#        der=(abs(ai - af)/h)
#        b=bi
#        if der<tol and c==0 and bi>=0:
#            c=1
#            h=abs(bi-beta_list[j])
#            
#
#            der=array([1, 1])
#            
#            
#            while any(der>tol):
#                h=h/2          
#                
#                ex=TP.TestParticle(alpha=alph, beta=10**(b+h))
#                ex.runrk4()
#                a=log10(ex.GetA())
#                der=array([(abs(ai - a)/h), abs(a-af)/h])
#                print(alph,a-af, der, b+h)
#                if der[0]<der[1]:
#                    c=0
#                    break
#                
#                b=b+h
#                ai=a
#            bflat=b  
#            
#        ai=af
#        bi=beta_list[j]
#    plt.plot(beta_plot, a_plot, '.-')
#    beta_flat.append(bflat)
#    a_flat.append(a)
#plt.plot(beta_flat, a_flat, '.-')
#plt.xlabel(r'$\beta$')
#plt.ylabel(r'$a$')
#plt.show()    
'''
Precision a(beta)
'''


tol=0.01
S=0.95

#alph_uniq=[0.9]


for alph in alph_uniq:
    indices = [i for i, x in enumerate(alph_grid) if x == alph]
    for j in range(len(indices)-1):
        if all([a_grid[indices[j]], a_grid[indices[j+1]]])!=inf and abs(a_grid[indices[j]]-a_grid[indices[j+1]])>tol:
            a=a_grid[indices[j]]
            b=beta_grid[indices[j]]
            b_max=beta_grid[indices[j+1]]
            h=0.01*b
            while a==inf:
                b+=h
                ex=TP.TestParticle(alpha=alph, beta=b, circular=1)
                ex.runrk4()
                Gather(ex)
                a=ex.GetA()
            while b<b_max: 
            
                y=[]
                
                for h0 in [h, h/2]:
                    
                    ex=TP.TestParticle(alpha=alph, beta=b+h0, circular=1)
                    ex.runrk4()       
                    Gather(ex)
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
                    Gather(ex)
                    if b+h>b_max:
                        b=b_max
                        break
                        
                else:
                    if b+h>b_max:
                        b=b_max
                        break
                    
                    b+=h
                    #Gather(ex)
                    h *= S*(tol/diff)**(1/5)
                print(alph, b, diff)

with open('extra_a_data(4).csv', 'w') as f:
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

'''
precision a(alpha)
'''


#
#beta_uniq=list(set(beta_grid))
#alph_uniq=list(set(alph_grid))
#beta_uniq.sort()
#alph_uniq.sort()
#tol=0.1
#S=0.95
#
#
#for b in beta_uniq:
#    indices = [i for i, x in enumerate(beta_grid) if x == b]
#    for j in range(len(indices)-1):
#        if all(array([a_grid[indices[j]], a_grid[indices[j+1]]])!=inf) and abs(a_grid[indices[j]]-a_grid[indices[j+1]])>tol:            
#            a=a_grid[indices[j]]
#            alph=alph_grid[indices[j]]
#            alph_max=alph_grid[indices[j+1]]
#            h=0.01*alph
#            while alph<alph_max: 
#                if h<1e-3:
#                    break
#                y=[]
#                
#                for h0 in [h, h/2]:
#                    
#                    ex=TP.TestParticle(alpha=alph+h0, beta=b, circular=1)
#                    ex.runrk4()                
#                    y.append(ex.GetA())
#                y=array(y)
#                if any(y==inf):
#                    break
#                diff=abs(log10(y[0])-log10(y[1]))
#                if diff>tol:
#                    h *= S*(tol/diff)**(1/5)
#                    if h<1e-6:
#                        break
#                    if alph+h>alph_max:
#                        alph=alph_max
#                        break
#                    alph+=h
#                    ex=TP.TestParticle(alpha=alph, beta=b, circular=1)
#                    ex.runrk4()
#                    Gather(ex)
#                    if alph+h>alph_max:
#                        alph=alph_max
#                        break
#                        
#                else:
#                    if alph+h>alph_max:
#                        alph=alph_max
#                        break
#                    
#                    alph+=h
#                    Gather(ex)
#                    h *= S*(tol/diff)**(1/5)
#                print(alph, b)
#
#with open('extra2_a_data(4).csv', 'w') as f:
#    for i in range(len(alph_list)):
#        out_string=''
#        out_string+=str(alph_list[i])
#        out_string+=','+str(beta_list[i])
#        out_string+=','+str(a_list[i])
#        out_string+=','+str(e_list[i])
#        out_string+=','+str(E_list[i])
#        out_string+=','+str(th_list[i])
#        out_string+='\n'
#        f.write(out_string)

'''
more alpha around 0.5
'''
#alph05=arange(0.46, 0.55, 0.01)
#tol=0.01
#S=0.95
#
#
#indices = [i for i, x in enumerate(alph_grid) if x == 0.5]
#for alph in alph05:
#    for j in range(len(indices)-1):
#        
#        if abs(a_grid[indices[j]]-a_grid[indices[j+1]])>tol:
#            b=beta_grid[indices[j]]
#            ex=TP.TestParticle(alpha=alph, beta=b, circular=1)
#            ex.runrk4()
#            a=ex.GetA()
#            #a=a_grid[indices[j]]
#            
#            b_max=beta_grid[indices[j+1]]
#            h=0.001*b
#            while a==inf:
#                b+=h
#                ex=TP.TestParticle(alpha=alph, beta=b, circular=1)
#                ex.runrk4()
#                a=ex.GetA()
#                
#            Gather(ex)
#            print(a, b)
#            while b<b_max: 
#            
#                y=[]
#                
#                for h0 in [h, h/2]:
#                    
#                    ex=TP.TestParticle(alpha=alph, beta=b+h0, circular=1)
#                    ex.runrk4()                
#                    y.append(ex.GetA())
#                    print(y[-1], b+h0)
#                diff=abs(log10(y[0])-log10(y[1]))
#                
#                if diff>tol:
#                    h *= S*(tol/diff)**(1/5)
#                    if b+h>b_max:
#                        h=b_max-b
#                        
#                    b+=h
#                    ex=TP.TestParticle(alpha=alph, beta=b, circular=1)
#                    ex.runrk4()
#                    Gather(ex)
#                    if b+h>b_max:
#                        h=b_max-b
#                        
#                        
#                else:
#                    if b+h>b_max:
#                        h=b_max-b
#                    
#                    b+=h
#                    Gather(ex)
#                    h *= S*(tol/diff)**(1/5)
#                print(alph, b)
#
#with open('0.5_a_data(4).csv', 'w') as f:
#    for i in range(len(alph_list)):
#        out_string=''
#        out_string+=str(alph_list[i])
#        out_string+=','+str(beta_list[i])
#        out_string+=','+str(a_list[i])
#        out_string+=','+str(e_list[i])
#        out_string+=','+str(E_list[i])
#        out_string+=','+str(th_list[i])
#        out_string+='\n'
#        f.write(out_string)
'''
Precision e
'''
#tol=0.05
#S=0.95
#print(alph_uniq)
#for alph in alph_uniq:
#    
#    indices = [i for i, x in enumerate(alph_grid) if x == alph]
#
#    for j in range(len(indices)-1):
#        
#        if abs(e_grid[indices[j]]-e_grid[indices[j+1]])>tol:
#            a=a_grid[indices[j]]
#            e=e_grid[indices[j]]
#            b=beta_grid[indices[j]]
#            b_max=beta_grid[indices[j+1]]
#            h=0.01*b
#            while a==inf:
#                b+=h
#                ex=TP.TestParticle(alpha=alph, beta=b, circular=1)
#                ex.runrk4()
#                a=ex.GetA()
#            while b<b_max: 
#            
#                y=[]
#                
#                for h0 in [h, h/2]:
#                    
#                    ex=TP.TestParticle(alpha=alph, beta=b+h0, circular=1)
#                    ex.runrk4()                
#                    y.append(ex.GetEc())
#                diff=abs(y[0]-y[1])
#                
#                if diff>tol:
#                    h *= S*(tol/diff)**(1/5)
#                    if b+h>b_max:
#                        b=b_max
#                        break
#                    b+=h
#                    ex=TP.TestParticle(alpha=alph, beta=b, circular=1)
#                    ex.runrk4()
#                    Gather(ex)
#                    if b+h>b_max:
#                        b=b_max
#                        break
#                        
#                else:
#                    if b+h>b_max:
#                        b=b_max
#                        break
#                    
#                    b+=h
#                    Gather(ex)
#                    h *= S*(tol/diff)**(1/5)
#                print(alph, b)
#
#with open('extra_e_data2(4).csv', 'w') as f:
#    for i in range(len(alph_list)):
#        out_string=''
#        out_string+=str(alph_list[i])
#        out_string+=','+str(beta_list[i])
#        out_string+=','+str(a_list[i])
#        out_string+=','+str(e_list[i])
#        out_string+=','+str(E_list[i])
#        out_string+=','+str(th_list[i])
#        out_string+='\n'
#        f.write(out_string)