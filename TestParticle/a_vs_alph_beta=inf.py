#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 19:36:03 2018

@author: John
"""

import TestParticle as TP
from scipy import*
from matplotlib import pyplot as plt


#test=TP.TestParticle(circular=1,alpha=1, beta=10000)
#data=test.run(0.001, mloss=1, plot=1)



fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_aspect('equal')
ax.grid()
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
ax.plot(0,0,'ro', data[1][:100000], data[2][:100000],'b-')
#fig.savefig('Figures/TestParticle/TP_Trajectory_a={}_b={}.png'.format(self.alpha,self.beta))
fig.show()