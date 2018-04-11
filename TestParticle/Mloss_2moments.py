#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 01:22:20 2018

@author: John
"""

import TestParticle as TP
from scipy import*
from matplotlib import pyplot as plt

m=1
x=1

def analyticalE(alph1, alph2):
    
    E=G*m/x*(alph2*(1-2*alph1)+alph1-1/2)
    return E

def analyticala(alph1, alph2):
    a=(alph1+alph2-1)/(2*(alph2*(1-2*alph1)+alph1-1/2))
    return a

#print(analyticala(alph1, alph2))

def analyticale(alph1, alph2):
    return abs((2*alph1**2-2*alph1*alph2-alph1+alph2)/((1-2*alph1)*(alph1+alph2-1)))
def analyticala2(alph1):
    return 1/2
def analyticala2circ(alph1):
    return (2*alph1**2-alph1)/(2*alph1-1)

alph1=0.2
alph2=0.2

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

alpha1=arange(0, 0.4, 0.01)
alpha2=arange(0, 0.4, 0.01)

m=1

def analyticalA(alpha):
    return (alpha-1)/(2*alpha-1)


e=zeros([len(alpha1), len(alpha2)])
i=0
for alph1 in alpha1:
    j=0
    a1=analyticalA(alph1)
    t=sqrt(a1**3/(m-alph1))/2
    for alph2 in alpha2:
        test=TP.TestParticle(alpha=alph1+alph2, beta=t, circular=1)
        test.runrk4()
        e1=test.Orbit(0.001)[-1]
        if e1 == 'Unbound':
            e1=1
        e[i, j]=e1
        j+=1
        print(i, j)
    i+=1

x, y = meshgrid(alph1, alph2)
Z=e
im=plt.imshow(Z, origin='lower', extent=[0,0.5,0,0.5])
cset=plt.contour(Z, arange(0, 1.1, 0.1), cmap=plt.cm.Greys, extent=[0,0.5,0,0.5])
plt.xlabel(r'$\alpha_1$')
plt.ylabel(r'$\alpha_2$')
plt.title('Eccentricity after two mass loss, Continuous')
plt.colorbar(im)
plt.show()    




