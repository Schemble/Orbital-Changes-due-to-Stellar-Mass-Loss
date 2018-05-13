#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 01:22:20 2018

@author: John
"""

import TestParticle as TP
from scipy import*
from matplotlib import pyplot as plt

#m=1
#x=1

def analyticalE(alph1, alph2):
    
    E=G*m/x*(alph2*(1-2*alph1)+alph1-1/2)
    return E



#print(analyticala(alph1, alph2))

def analyticale(alph1, alph2):
    return abs((2*alph1**2-2*alph1*alph2-alph1+alph2)/((1-2*alph1)*(alph1+alph2-1)))
def analyticala2(alph1):
    return 1/2
def analyticala2circ(alph1):
    return (2*alph1**2-alph1)/(2*alph1-1)

#alph1=0.2
#alph2=0.2

'''
a1=arange(0, 0.5, 0.001)
a2=arange(0, 0.5, 0.001)
x, y = meshgrid(a1, a2)
Z=analyticale(x, y)
im=plt.imshow(Z, origin='lower', extent=[0,0.5,0,0.5])
cset=plt.contour(Z, arange(0, 1.1, 0.1), cmap=plt.cm.Greys, extent=[0,0.5,0,0.5])
plt.xlabel(r'$\alpha_1$')
plt.ylabel(r'$\alpha_2$')
plt.title('Eccentricity after two mass loss')
plt.colorbar(im)
plt.show()
'''
#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.set_aspect('equal')
#ax.grid()
#plt.xlabel(r'$\alpha_1$')
#plt.ylabel(r'$\alpha_2$')
#plt.xlabel('x [AU]')
#plt.ylabel('y [AU]')
#plt.plot(0, 0,'r.')
#plt.plot(linspace(0,0.4999), analyticala2circ(linspace(0,0.4999)), label='Circular')
#plt.plot(linspace(0,0.4999), analyticala2(linspace(0,0.4999)), label='Unbound')

'''
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_aspect('equal')
ax.grid()
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
plt.plot(0, 0,'r.')
circ=TP.TestParticle(m, x, circular=1, alpha=alph1)
#E=TP.TestParticle(m, x, circular=1, alpha=a)
#print(ex.Etot())
x0, y0, r0, a0, e0 = circ.Orbit(0.001)
#print(a0)
plt.plot(x0, y0)
circ.InstMLoss()
#E.InstMLoss()
#print(ex.Etot())
x1, y1, r1, a1, e1 = circ.Orbit(0.001)
#print(a1)
plt.plot(x1, y1)
theta=circ.Theta()
while theta < pi:
    circ.timestep(0.001)
    #E.timestep(0.001)
    theta=circ.Theta()


#alph2E=analyticala2(a)
circ.alpha=alph2
#E.alpha=alph2E
circ.InstMLoss()
#E.InstMLoss()
#print(circ.Etot())
x2, y2, r2, a2, e2 = circ.Orbit(0.001)
print(a2, e2)
#plt.title(r'$\alpha_1={}, \alpha_2={}$'.format(a, alph2c))
plt.plot(x2, y2)
#plt.show()
#plt.plot(a, alph2c,'o')
#plt.plot(a, alph2E, 'o')
G=4*pi**2
#a1=x*(1-alph1)/(1-2*alph1)

#plt.grid()
#plt.legend()
#plt.show
'''    
'''
a1=arange(0, 0.5, 0.001)
a2=arange(0, 0.5, 0.001)
x, y = meshgrid(a1, a2)
Z=log10(analyticala(x, y))
im=plt.imshow(Z, origin='lower', extent=[0,0.5,0,0.5])
cset=plt.contour(Z, arange(0, 1.3, 0.2), cmap=plt.cm.Greys, extent=[0,0.5,0,0.5])
plt.xlabel(r'$\alpha_1$')
plt.ylabel(r'$\alpha_2$')
plt.title('Separation after two mass loss')
plt.colorbar(im, label=r'$\log(a/a_0)$')
plt.show()
'''
'''
t=sqrt(a1**3/(m-alph1))/2


C=TP.TestParticle(m ,x, alpha=alph1+alph2, beta=t, circular=1)
h=0.001
theta=C.Theta()
T, X, Y, M, E, A=C.run(h, mloss=1)
plt.plot()
print(C.Etot())
X_orb, Y_orb, r_orb, a_c, e_c=C.Orbit(0.001)
print(a_c, e_c)
#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.set_aspect('equal')
#ax.grid()
#plt.xlabel('x [AU]')
#plt.ylabel('y [AU]')
#plt.plot(0, 0,'r.')
plt.plot(X_orb, Y_orb)
plt.plot(X, Y, '--')
plt.show()
'''

#alpha1=arange(0, 0.5, 0.01)
#alpha2=arange(0, 0.5, 0.01)
#
#m=1
#
#def analyticalA(alpha):
#    return (alpha-1)/(2*alpha-1)
#
#a=zeros([len(alpha1), len(alpha2)])
#ec=zeros([len(alpha1), len(alpha2)])
#i=0
#for alph1 in alpha1:
#    j=0
#    a1=analyticalA(alph1)
#    t=sqrt(a1**3/(m-alph1))/2
#    for alph2 in alpha2:
#        test=TP.TestParticle(alpha=alph1+alph2, beta=t, circular=1)
#        test.runrk4()
#        ac=test.GetA()
#        if ac == 'Unbound':
#            ac=0.1
#            a[i, j]=ac
#        else:
#            a[i, j]=ac
#        
#        data=test.Orbit(0.01)
#        if data == 'Unbound':
#            e1=1
#            ec[i, j]=e1
#        else:
#            ec[i, j]=data[-1]
#        j+=1
#        print(i, j)
#    i+=1
#
#x, y = meshgrid(alpha1, alpha2)
#
#Ze=ec/analyticale(x, y)
#plt.figure()
#im=plt.imshow(Ze, origin='lower', extent=[0,0.5,0,0.5])
##cset=plt.contour(Ze, arange(0, 5, 0.5), cmap=plt.cm.Greys, extent=[0,0.5,0,0.5])
#plt.xlabel(r'$\alpha_1$')
#plt.ylabel(r'$\alpha_2$')
#
#plt.colorbar(im)
#plt.show()    
#
#Za=a/analyticala(x, y)
#
#plt.figure()
#im=plt.imshow(Za, origin='lower', extent=[0,0.5,0,0.5])
##cset=plt.contour(Za, arange(0, 1.1, 0.1), cmap=plt.cm.Greys, extent=[0,0.5,0,0.5])
#plt.xlabel(r'$\alpha_1$')
#plt.ylabel(r'$\alpha_2$')
#
#plt.colorbar(im)
#plt.show()

#alpha1=arange(0, 0.5, 0.01)
#alpha2=arange(0, 0.5, 0.01)
#
#m=1
#
#def analyticalA(alpha):
#    return (alpha-1)/(2*alpha-1)
#
#
#a=zeros([len(alpha1), len(alpha2)])
#i=0
#for alph1 in alpha1:
#    j=0
#    a1=analyticalA(alph1)
#    t=sqrt(a1**3/(m*(1-alph1)))/2
#    for alph2 in alpha2:
#        test=TP.TestParticle(alpha=alph1+alph2, beta=t, circular=1)
#        test.runrk4()
#        ac=test.GetA()
#        if ac == 'Unbound':
#            ac=0
#            a[i, j]=ac
#        else:
#            a[i, j]=ac
#        j+=1
#        print(i, j, ac)
#    i+=1
#
#x, y = meshgrid(alpha1, alpha2)
#
#Z=log10(a/analyticala(x, y))
#
#im=plt.imshow(Z, origin='lower', extent=[0,0.5,0,0.5])
#cset=plt.contour(Z, arange(0, 3, 0.2), cmap=plt.cm.Greys, extent=[0,0.5,0,0.5])
#plt.xlabel(r'$\alpha_1$')
#plt.ylabel(r'$\alpha_2$')
#
#plt.colorbar(im)
#plt.show()


#contour plots 2mass loss

        


def backlinint(value, x1, x2, f1, f2):
    f=value
    return (x1*(f2-f)+x2*(f-f1))/(f2-f1)
def contour(value, data):
    data=array(data)
    X=[]
    Y=[]
    x_uniq=list(set(data[:,0]))
    x_uniq.sort()
    y_uniq=list(set(data[:,1]))
    y_uniq.sort()
    for x in x_uniq:
        line=data[where(data[:,0]==x)]
        
        diff=line[:,2]-value
        if any(diff<=0) and any(diff>=0):
            diff=abs(diff)
            p1=line[where(diff==sort(diff)[0])][0]
            
            p2=line[where(diff==sort(diff)[1])][0]
            i=2
            while (p2[2]-value)*(p1[2]-value)>0:
                p2=line[where(diff==sort(diff)[i])][0]
                i+=1
        
            Y.append(backlinint(value, p1[1], p2[1], p1[2], p2[2]))
            X.append(x)

    for y in y_uniq:
        line=data[where(data[:,1]==y)]
        diff=line[:,2]-value
        if any(diff<=0) and any(diff>=0):
            diff=abs(diff)
            p1=line[where(diff==sort(diff)[0])][0]
            
            p2=line[where(diff==sort(diff)[1])][0]
            i=2
            while (p2[2]-value)*(p1[2]-value)>0:
                p2=line[where(diff==sort(diff)[i])][0]
                i+=1
        
            X.append(backlinint(value, p1[0], p2[0], p1[2], p2[2]))
            Y.append(y)


    return X, Y

alpha_1=linspace(0, 0.5, 100)
alpha_2=linspace(0, 0.5, 100)

def analyticalE(alph1, alph2):
    G=4*pi**2
    x=1
    m=1    
    E=G*m/x*(alph2*(1-2*alph1)+alph1-1/2)
    return E
points=[]
for a1 in alpha_1:
    for a2 in alpha_2:        
        E=analyticalE(a1, a2)
        points.append([a1, a2, E])
points=array(points)
E_list=linspace(-18, 0, 10)




#
#fig=plt.figure()
#ax = fig.add_subplot(111)
#ax.set_aspect('equal')
##plt.plot(x_fit, y_fit , [0,1], [0,0], 'g--', alpha, Etot, '.')
##plt.plot(alpha_crit, 0, 'ro', label=r'$\alpha_{crit}$'+'={:.1f}'.format(alpha_crit))
#for En in E_list:
#    xplot, yplot=contour(En, points)
#    yplot = [x for _,x in sorted(zip(xplot,yplot))]
#    xplot.sort()
#    plt.plot(xplot, yplot, label=r'$E={:.1f}$'.format(En))
#fig.legend(bbox_to_anchor=(0.85, 0.85), loc='upper right', ncol=1)
##plt.tight_layout(rect=[0,0,0.75,1])
#plt.xlabel(r'$\alpha_1$')
#plt.ylabel(r'$\alpha_2$')
#plt.xticks(arange(0, 1.1, 0.1))
#plt.xlim(xmin=0, xmax=0.51)
#plt.ylim(ymin=0,ymax=0.51)
#plt.subplots_adjust(right=0.7, bottom=0.3)
#ax.grid()
#plt.show()


def analyticala(alph1, alph2):
    a=(alph1+alph2-1)/(2*(alph2*(1-2*alph1)+alph1-1/2))
    return a


#alpha_1=linspace(0, 0.5, 100)
#alpha_2=linspace(0, 0.5, 100)
#
#
#points=[]
#for a1 in alpha_1[:-1]:
#    for a2 in alpha_2[:-1]:        
#        a=log10(analyticala(a1, a2))
#        points.append([a1, a2, a])
#points=array(points)
#a_list=linspace(0, log10(50), 10)
##a_list=array([2, 4, 8, 16, 32, 64])
##
##
##
#fig=plt.figure()
#ax = fig.add_subplot(111)
#ax.set_aspect('equal')
#for a in a_list:
#    xplot, yplot=contour(a, points)
#    yplot = [x for _,x in sorted(zip(xplot,yplot))]
#    xplot.sort()
#    plt.plot(xplot, yplot, label=r'$\log\frac{a}{a_0}$'+'={:.2f}'.format(a))
#fig.legend(bbox_to_anchor=(0.85, 0.9), loc='upper right', ncol=1)
#plt.xlabel(r'$\alpha_1$')
#plt.ylabel(r'$\alpha_2$')
#plt.xticks(arange(0, 1.1, 0.1))
#plt.xlim(xmin=0, xmax=0.51)
#plt.ylim(ymin=0,ymax=0.51)
#plt.subplots_adjust(right=0.7, bottom=0.3)
#ax.grid()
#plt.show()
    

def analyticale1(alph1, alph2):
    return (2*alph1**2-2*alph1*alph2-alph1+alph2)/((1-2*alph1)*(alph1+alph2-1))
def analyticale2(alph1, alph2):
    return -(2*alph1**2-2*alph1*alph2-alph1+alph2)/((1-2*alph1)*(alph1+alph2-1))


alpha_1=linspace(0, 0.5, 1000)
alpha_2=linspace(0, 0.5, 1000)


points1=[]
points2=[]
for a1 in alpha_1[:-1]:
    for a2 in alpha_2[:-1]:        
        e=analyticale1(a1, a2)
        points1.append([a1, a2, e])
        e=analyticale2(a1, a2)
        points2.append([a1, a2, e])
points1=array(points1)
points2=array(points2)
e_list=linspace(0, 0.9, 10)


#points=array(points1+points2)



fig=plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')
cmap = plt.get_cmap('jet')
for e in e_list:
    color=cmap(e)
    xplot, yplot=contour(e, points1)
    yplot = [x for _,x in sorted(zip(xplot,yplot))]
    xplot.sort()
    plt.plot(xplot, yplot,c=color,  label=r'$e$'+'={:.1f}'.format(e))
    xplot, yplot=contour(e, points2)
    yplot = [x for _,x in sorted(zip(xplot,yplot))]
    xplot.sort()
    plt.plot(xplot, yplot,c=color)
fig.legend(bbox_to_anchor=(0.8, 0.9), loc='upper right', ncol=1)
plt.xlabel(r'$\alpha_1$')
plt.ylabel(r'$\alpha_2$')
plt.xticks(arange(0, 1.1, 0.1))
plt.xlim(xmin=0, xmax=0.51)
plt.ylim(ymin=0,ymax=0.51)
plt.subplots_adjust(right=0.7, bottom=0.3)
ax.grid()
plt.show()




