#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:02:28 2018

@author: John
"""
from matplotlib import pyplot as plt
from scipy import interpolate
import numpy as np
from scipy import*

alph_list=[]
beta_list=[]
a_list=[]
e_list=[]
E_list=[]
th_list=[]
data_points=[]




with open('grid_data3.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_list.append(float(l[0]))
        beta_list.append(log10(float(l[1])))
        a_list.append(log10(float(l[2])))
        e_list.append(float(l[3]))
        E_list.append(float(l[4]))
        th_list.append(float(l[5]))
        data_points.append([float(l[0]),log10(float(l[1])),log10(float(l[2])),float(l[3]),float(l[4]),float(l[5])])
        
with open('grid_data3.1.csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_list.append(float(l[0]))
        beta_list.append(log10(float(l[1])))
        a_list.append(log10(float(l[2])))
        e_list.append(float(l[3]))
        E_list.append(float(l[4]))
        th_list.append(float(l[5]))
        data_points.append([float(l[0]),log10(float(l[1])),log10(float(l[2])),float(l[3]),float(l[4]),float(l[5])])
#
#with open('grid_data2,7.csv') as f:
#    for line in f.readlines():
#        l=line.split(',')
#        alph_list.append(float(l[0]))
#        beta_list.append(log10(float(l[1])))
#        a_list.append(log10(float(l[2])))
#        e_list.append(float(l[3]))
#        E_list.append(float(l[4]))
#        th_list.append(float(l[5]))
#        data_points.append([float(l[0]),log10(float(l[1])),log10(float(l[2])),float(l[3]),float(l[4]),float(l[5])])


alph_grid=alph_list.copy()
beta_grid=beta_list.copy()
a_grid=a_list.copy()
e_grid=e_list.copy()
E_grid=E_list.copy()
th_grid=th_list.copy()
grid_points=data_points.copy()

with open('extra_a_data(4).csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_list.append(float(l[0]))
        beta_list.append(log10(float(l[1])))
        a_list.append(log10(float(l[2])))
        e_list.append(float(l[3]))
        E_list.append(float(l[4]))
        th_list.append(float(l[5]))
        data_points.append([float(l[0]),log10(float(l[1])),log10(float(l[2])),float(l[3]),float(l[4]),float(l[5])])
        
with open('extra2_a_data(4).csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_list.append(float(l[0]))
        beta_list.append(log10(float(l[1])))
        a_list.append(log10(float(l[2])))
        e_list.append(float(l[3]))
        E_list.append(float(l[4]))
        th_list.append(float(l[5]))
        data_points.append([float(l[0]),log10(float(l[1])),log10(float(l[2])),float(l[3]),float(l[4]),float(l[5])])

with open('0.5_a_data(4).csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_list.append(float(l[0]))
        beta_list.append(log10(float(l[1])))
        a_list.append(log10(float(l[2])))
        e_list.append(float(l[3]))
        E_list.append(float(l[4]))
        th_list.append(float(l[5]))
        data_points.append([float(l[0]),log10(float(l[1])),log10(float(l[2])),float(l[3]),float(l[4]),float(l[5])])

with open('extra_e_data2(4).csv') as f:
    for line in f.readlines():
        l=line.split(',')
        alph_list.append(float(l[0]))
        beta_list.append(log10(float(l[1])))
        a_list.append(log10(float(l[2])))
        e_list.append(float(l[3]))
        E_list.append(float(l[4]))
        th_list.append(float(l[5]))
        data_points.append([float(l[0]),log10(float(l[1])),log10(float(l[2])),float(l[3]),float(l[4]),float(l[5])])


data_points = array(sorted(data_points, key=lambda x: x[0]))
data_points = array(sorted(data_points, key=lambda x: x[1]))

'''
Plot E vs alpha
'''
#beta_list=array(beta_grid)
#beta_uniq=sort(list(set(beta_grid)))
#
##beta_uniq=arange(-1, 2.5, 0.5)
#beta_uniq=beta_uniq[10:-10]
#fig=plt.figure()
#ax = fig.add_subplot(111)
#cmap = plt.get_cmap('jet_r')
#for b in beta_uniq[::2]:
#    alph_plot=[]
#    E_plot=[]
#    indices = [i for i, x in enumerate(beta_grid) if x == b]
#    for i in indices:
#        alph_plot.append(alph_grid[i])
#        E_plot.append(E_grid[i])
#    order=argsort(alph_plot)
#    alph_plot=array(alph_plot)[order]
#    E_plot=array(E_plot)[order]
#    plt.plot(alph_plot, E_plot,'.-', c=cmap((b-min(beta_uniq))/(max(beta_uniq)-min(beta_uniq))), label=r'$\log\beta={:.2f}$'.format(b))
#fig.legend(bbox_to_anchor=(1, 0.89), loc='upper right', ncol=1)
#plt.xlabel(r'$\alpha$')
#plt.ylabel(r'$E_{tot}$')
#plt.xticks(arange(0, 1.1, 0.1))
#plt.xlim(xmin=0, xmax=1)
#plt.ylim(ymin=-20,ymax=20)
#plt.subplots_adjust(right=0.75)
#ax.grid()
#plt.show()

'''
Plot ac vs beta
'''

#beta_list=array(beta_list)
#beta_uniq=sort(list(set(data_points[:,1])))
#
#def findzero(x, y):
#    linreg=linregress(x, y)
#    return -linreg.intercept/linreg.slope
#
##beta_uniq=arange(-1, 2.5, 0.5)
##beta_uniq=beta_uniq[10:-10]
#fig=plt.figure()
#ax = fig.add_subplot(111)
#cmap = plt.get_cmap('jet_r')
#beta_plot=[]
#ac_plot=[]
#theta_plot=[]
#for b in beta_uniq:
#    print(b)
#    indices = [i for i, x in enumerate(data_points[:,1]) if x == b]
#    for j in range(len(indices[:-1])):
#        if data_points[indices[j], 4]*data_points[indices[j+1], 4]<0:
#            ac_plot.append(findzero([data_points[indices[j],0],data_points[indices[j+1], 0]], [data_points[indices[j], 4], data_points[indices[j+1],4]]))
#            beta_plot.append(b)
#            theta_plot.append(data_points[indices[j],5])
#plt.scatter(log10(beta_plot), ac_plot, c=theta_plot)
##fig.legend(bbox_to_anchor=(1, 0.89), loc='upper right', ncol=1)
#plt.xlabel(r'$\log\beta$')
#plt.ylabel(r'$\alpha_c$')
##plt.xticks(arange(0, 1.1, 0.1))
##plt.xlim(xmin=0, xmax=1)
##plt.ylim(ymin=-20,ymax=20)
##plt.subplots_adjust(right=0.75)
#ax.grid()
#plt.show()



'''
a vs beta
'''
#alph_uniq=sort(list(set(alph_grid)))
#alph_plot=arange(0.05, 1, 0.05)
#
#fig=plt.figure()
#ax = fig.add_subplot(111)
#cmap = plt.get_cmap('jet_r')
#beta_plot=[]
#ac_plot=[]
#theta_plot=[]
#
#for alph in alph_plot:
#    beta_plot=[]
#    a_plot=[]
#    indices = [i for i, x in enumerate(alph_list) if x == round(alph,2)]
#    for j in indices:
#        beta_plot.append(beta_list[j])
#        a_plot.append(a_list[j])
#        print(beta_list[j], 1)
#    order=argsort(beta_plot)
#    beta_plot=array(beta_plot)[order]
#    a_plot=array(a_plot)[order]
#    plt.plot(beta_plot, a_plot, '.-',c=cmap(alph), label=r'$\alpha={}$'.format(round(alph,2)))
#fig.legend(bbox_to_anchor=(1, 0.89), loc='upper right', ncol=1)
#plt.xlabel(r'$\log\beta$')
#plt.ylabel(r'$\log a$')
##plt.xticks(arange(0, 1.1, 0.1))
##plt.xlim(xmin=0, xmax=1)
#plt.ylim(ymin=0, ymax=2)
#plt.subplots_adjust(right=0.75)
#ax.grid()
#plt.show()






'''
a vs alpha
'''

#beta_uniq=sort(list(set(beta_grid)))
#beta_plot=arange(-2, 4.1, 0.5)
#fig=plt.figure()
#ax = fig.add_subplot(111)
#cmap = plt.get_cmap('jet_r')
#for b in beta_plot:
#    alph_plot=[]
#    a_plot=[]
#    indices = [i for i, x in enumerate(beta_list) if round(x, 5) == b]
#    for j in indices:
#        alph_plot.append(alph_list[j])
#        a_plot.append(a_list[j])
#    order=argsort(alph_plot)
#    alph_plot=array(alph_plot)[order]
#    a_plot=array(a_plot)[order]
#    plt.plot(alph_plot, a_plot, '.-',c=cmap((b-min(beta_list))/(max(beta_list)-min(beta_list))),label=r'$\beta={}$'.format(b))
#fig.legend(bbox_to_anchor=(1, 0.89), loc='upper right', ncol=1)
#plt.xlabel(r'$\alpha$')
#plt.ylabel(r'$\log a$')
#plt.xticks(arange(0, 1.1, 0.1))
#plt.xlim(xmin=0, xmax=1)
#plt.ylim(ymin=0, ymax=2)
#plt.subplots_adjust(right=0.75)
#ax.grid()
#plt.show()
'''
'''
beta_plot=arange(-2, 4.5, 0.5)
#
#
#plt.figure()
#plt.grid()
#cmap = plt.get_cmap('jet_r')
#for b in beta_plot:
#    alph_plot=[]
#    e_plot=[]
#    indices = [i for i, x in enumerate(beta_list) if round(x, 2) == b]
#    for j in indices:
#        if e_list[j]<1:
#            alph_plot.append(alph_list[j])
#            e_plot.append(e_list[j])
#    order=argsort(alph_plot)
#    alph_plot=array(alph_plot)[order]
#    e_plot=array(e_plot)[order]
#    plt.plot(alph_plot, e_plot, '.-',c=cmap((b-min(beta_list))/(max(beta_list)-min(beta_list))),label=r'$\beta={:.2f}$'.format(b))
#plt.legend(bbox_to_anchor=(1.35, 1), loc='upper right', ncol=1)
#plt.ylim(ymax=1, ymin=0)
#plt.xlabel(r'$\alpha$')
#plt.ylabel(r'$e$')
#plt.subplots_adjust(right=0.75)
#plt.show()
#
#
alph_plot=arange(0.05, 1, 0.05)
#plt.figure()
#plt.grid()
#cmap = plt.get_cmap('jet_r')
#for alph in alph_plot:
#    beta_plot=[]
#    e_plot=[]
#    indices = [i for i, x in enumerate(alph_list) if x == round(alph, 2)]
#    for j in indices:
#        if e_list[j]<1:
#            beta_plot.append(beta_list[j])
#            e_plot.append(e_list[j])
#    order=argsort(beta_plot)
#    beta_plot=array(beta_plot)[order]
#    e_plot=array(e_plot)[order]
#    plt.plot(beta_plot, e_plot, '.-',c=cmap(alph), label=r'$\alpha={}$'.format(round(alph, 2)))
#plt.legend(bbox_to_anchor=(1.3, 1.01), loc='upper right', ncol=1)
#plt.xlabel(r'$\log\beta$')
#plt.ylabel(r'$e$')
#plt.subplots_adjust(right=0.75)
#plt.ylim(ymax=1, ymin=0)
#plt.show()
#
#
#plt.figure()
#plt.grid()
#cmap = plt.get_cmap('jet_r')
#for b in beta_plot:
#    alph_plot=[]
#    e_plot=[]
#    indices = [i for i, x in enumerate(beta_list) if round(x, 5) == b]
#    for j in indices:
#        if e_list[j]<1:
#            alph_plot.append(alph_list[j])
#            e_plot.append(e_list[j])
#    order=argsort(alph_plot)
#    alph_plot=array(alph_plot)[order]
#    e_plot=array(e_plot)[order]
#    plt.plot(alph_plot, log10(e_plot), '.-', c=cmap((b-min(beta_list))/(max(beta_list)-min(beta_list))),label=r'$\beta={:.2f}$'.format(b))
#plt.legend(bbox_to_anchor=(1.35, 1.), loc='upper right', ncol=1)
#plt.xlabel(r'$\alpha$')
#plt.ylabel(r'$\loge$')
#plt.subplots_adjust(right=0.75)
#plt.ylim(ymax=0)
#plt.show()
#
#
#plt.figure()
#plt.grid()
#cmap = plt.get_cmap('jet_r')
#for alph in alph_plot:
#    beta_plot=[]
#    e_plot=[]
#    indices = [i for i, x in enumerate(alph_list) if x == round(alph,2)]
#    for j in indices:
#        if e_list[j]<1:
#            beta_plot.append(beta_list[j])
#            e_plot.append(e_list[j])
#    order=argsort(beta_plot)
#    beta_plot=array(beta_plot)[order]
#    e_plot=array(e_plot)[order]
#    plt.plot(beta_plot, log10(e_plot), '.-',c=cmap(alph), label=r'$\alpha={}$'.format(round(alph, 2)))
#plt.legend(bbox_to_anchor=(1.3, 1.01), loc='upper right', ncol=1)
#plt.xlabel(r'$\log\beta$')
#plt.ylabel(r'$\loge$')
#plt.ylim(ymax=0)
#plt.subplots_adjust(right=0.75)
#plt.show()




#
#grid_x, grid_y = np.mgrid[min(beta_list):max(beta_list):500j, min(alph_list):max(alph_list):500j]
#points=column_stack((beta_list, alph_list))
#grid_za = interpolate.griddata(points, a_list, (grid_x, grid_y), method='linear')
#
#plt.figure()
#plt.xlabel(r'$\log\beta$')
#plt.ylabel(r'$\alpha$')
##plt.xscale('log')
##plt.scatter(beta_list, alph_list, c=a_list, vmin=0, vmax=6)
##plt.colorbar(label=r'$\log a_data$')
#plt.imshow(grid_za.T, vmin=0, vmax=6, extent=(min(beta_list),max(beta_list),min(alph_list),max(alph_list)), origin='lower', aspect='auto')
#plt.colorbar(label=r'$\log a_int$')
#cset=plt.contour(grid_za.T, arange(0, 2, 0.2), cmap=plt.cm.Greys, extent=(min(beta_list),max(beta_list),min(alph_list),max(alph_list)))
#
#
#plt.show()
#
#grid_ze = interpolate.griddata(points, e_list, (grid_x, grid_y), method='linear')

#plt.figure()
##plt.xscale('log')
##plt.scatter(beta_list, alph_list, c=e_list, vmin=0, vmax=1)
##plt.colorbar(label=r'$e_data$')
##plt.imshow(grid_ze.T,vmin=0, vmax=1, extent=(min(beta_list),max(beta_list),min(alph_list),max(alph_list)), origin='lower', aspect='auto')
#plt.colorbar(label='$e_int$')
#cset=plt.contour(grid_ze.T, arange(0, 1, 0.1), cmap=plt.cm.Greys, extent=(min(beta_list),max(beta_list),min(alph_list),max(alph_list)))
#plt.xlabel(r'$\log\beta$')
#plt.ylabel(r'$\alpha$')
#
#plt.show()


#alph_uniq=list(set(alph_list))
#plt.figure()
#plt.grid()
#for alph in alph_uniq:
#    beta_plot=[]
#    a_plot=[]
#    indices = [i for i, x in enumerate(alph_list) if x == alph]
#    for j in indices:
#        beta_plot.append(beta_list[j])
#        a_plot.append(a_list[j])
#    order=argsort(beta_plot)
#    beta_plot=array(beta_plot)[order]
#    a_plot=array(a_plot)[order]
#    plt.plot(beta_plot, a_plot, '.-', label=r'$\alpha={}$'.format(alph))
#plt.legend()
#plt.xlim(xmax=1)
#plt.xlabel(r'$\log\beta$')
#plt.ylabel(r'$a$')
#plt.show()

#    
#alph_uniq=list(set(alph_grid))
#alph_uniq.sort()
#plt.figure()
#plt.grid()
#for alph in [alph_uniq[0]]:
#    beta_plot=[]
#    e_plot=[]
#    th_plot=[]
#    indices = [i for i, x in enumerate(alph_list) if x == alph]
#    for j in indices:
#        beta_plot.append(beta_list[j])
#        e_plot.append(e_list[j])
#        th_plot.append(th_list[j])
#    order=argsort(beta_plot)
#    beta_plot=array(beta_plot)[order]
#    e_plot=array(e_plot)[order]
#    plt.scatter(beta_plot, log10(e_plot), c=th_plot)
#    plt.plot(beta_plot, log10(e_plot))
##plt.legend()
#plt.xlabel(r'$\log\beta$')
#plt.ylabel(r'$\log e$')
#plt.show()
'''
'''
#def analyticale(alpha):
#    return 1-(1-2*alpha)/(1-alpha)
#
#beta_uniq=list(set(beta_grid))
#plt.figure()
#plt.grid()
#for b in [min(beta_uniq)]:
#    anal_plot=[]
#    e_plot=[]
#    alph_plot=[]
#    indices = [i for i, x in enumerate(beta_list) if x == b]
#    for j in indices:
#        if alph_list[j]<0.5:
#            anal_plot.append(analyticale(alph_list[j]))
#            e_plot.append(e_list[j])
#            alph_plot.append(alph_list[j])
#    order=argsort(anal_plot)
#    anal_plot=array(anal_plot)[order]
#    alph_plot=array(alph_plot)[order]
#    e_plot=array(e_plot)[order]
#    plt.scatter(anal_plot, array(e_plot)/array(anal_plot), c=alph_plot)
#    plt.colorbar(label=r'$\alpha$')
##plt.legend()
#plt.xlabel(r'analytical $e$')
#plt.ylabel(r'$e_{\beta=0.1}/e_{analytical}$')
#plt.show()  
#
#def analyticala(alpha):
#    return (alpha-1)/(2*alpha-1)
#
#beta_uniq=list(set(beta_list))
#plt.figure()
#plt.grid()
#for b in [min(beta_uniq)]:
#    anal_plot=[]
#    a_plot=[]
#    alph_plot=[]
#    indices = [i for i, x in enumerate(beta_list) if x == b]
#    for j in indices:
#        if alph_list[j]<0.5:
#            anal_plot.append(log10(analyticala(alph_list[j])))
#            a_plot.append(a_list[j])
#            alph_plot.append(alph_list[j])
#    order=argsort(anal_plot)
#    anal_plot=array(anal_plot)[order]
#    alph_plot=array(alph_plot)[order]
#    a_plot=array(a_plot)[order]
#    plt.scatter(anal_plot, array(a_plot)/array(anal_plot), c=alph_plot)
#    plt.colorbar(label=r'$\alpha$')
##plt.legend()
#plt.xlabel(r'analytical $a$')
#plt.ylabel(r'$a_{\beta=0.1}/a_{analytical}$')
#plt.show()
#
#def analyticalainf(alpha):
#    return 1/(1-alpha)
#
#beta_uniq=list(set(beta_list))
#plt.figure()
#plt.grid()
#for b in [max(beta_uniq)]:
#    anal_plot=[]
#    a_plot=[]
#    alph_plot=[]
#    indices = [i for i, x in enumerate(beta_list) if x == b]
#    for j in indices:
#        if alph_list[j]<0.5:
#            anal_plot.append(log10(analyticalainf(alph_list[j])))
#            a_plot.append(a_list[j])
#            alph_plot.append(alph_list[j])
#    order=argsort(anal_plot)
#    anal_plot=array(anal_plot)[order]
#    alph_plot=array(alph_plot)[order]
#    a_plot=array(a_plot)[order]
#    plt.scatter(anal_plot, array(a_plot)/array(anal_plot), c=alph_plot)
#    plt.colorbar(label=r'$\alpha$')
##plt.legend()
#plt.xlabel(r'analytical $a$')
#plt.ylabel(r'$a_{\beta=0.1}/a_{analytical}$')
#plt.show()
  

def analyticalE(alpha):
    return 2*pi*(alpha-1/2)
#    
#beta_uniq=list(set(beta_grid))
#plt.figure()
#plt.grid()
#for b in [min(beta_uniq)]:
#    anal_plot=[]
#    E_plot=[]
#    alph_plot=[]
#    indices = [i for i, x in enumerate(beta_list) if x == b]
#    for j in indices:
#        anal_plot.append(analyticalE(alph_list[j]))
#        E_plot.append(a_list[j])
#        alph_plot.append(alph_list[j])
#    order=argsort(anal_plot)
#    anal_plot=array(anal_plot)[order]
#    alph_plot=array(alph_plot)[order]
#    E_plot=array(E_plot)[order]
#    plt.scatter(anal_plot, array(E_plot)/array(anal_plot), c=alph_plot)
#    plt.colorbar(label=r'$\alpha$')
##plt.legend()
#plt.xlabel(r'analytical $a$')
#plt.ylabel(r'$E_{\beta=0.1}/E_{analytical}$')
#plt.show()  
    