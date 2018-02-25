#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:45:09 2018

@author: John
"""

import TestParticle as TP
from scipy import*
from matplotlib import pyplot as plt


m=1
x=1
xs_list=array([0, 0.2, 0.4 ,0.6, 0.8])
vy_list=sqrt(4*pi**2*(2/(x-xs_list)-1))

fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_aspect('equal')
ax.grid()
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
for  vy, x_s in zip( vy_list, xs_list):
    orbit=TP.TestParticle(m, x, vy=vy, x_s=x_s)
    x_orb, y_orb = orbit.Orbit(0.0001)
    plt.plot(x_orb, y_orb, label='r_min={:.1f}, E={:.3f}'.format(x-x_s, orbit.Etot()))
    

plt.title('alpha=0, beta=0, m=1, v=v(r, a=constant)')
plt.legend()
#plt.savefig('TP_orbits_energy_with_constant_a.png')
plt.show()
    