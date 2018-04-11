#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:39:40 2018

@author: John
"""

import TestParticle as TP
from matplotlib import pyplot as plt

a=TP.TestParticle(alpha=0.5, beta=10, circular=1)

b=a.adrk4()
plt.plot(b[:,1], b[:,2])