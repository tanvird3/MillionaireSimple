# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:52:58 2018

@author: Tanvir Khan
"""

import pandas as pd
import numpy as np
import math as mt
import scipy as sc

id=[50000, 100000, 200000]

int=.09

y=[2,3,5]

target=1000000

def mismil(id, y, int, target):
    # for initial deposit
    # fv=pv+pv*i*n
    idfv=id + id * int * y
    rdtarget=target - idfv
    
    # for recurring deposit
    # fv=(R+R*i*n) + (R+R*i*(n-1))+ (R+R*i*(n-2))+ .....+ (R+R*i*1)
    # fv=n*R+ iR ( n+(n*1)+(n*2)+.....+1)
    # fv=n*R+ iR * n(n+1)/2
    # fv= R {n+i* n(n+1)/2}
    # R= fv/ {n+i*n(n+1)/2}
    
    # so instalment size
    inst = rdtarget / ((y * 12 + int / 12 * (y * 12) * (y * 12 + 1) / 2))
    return inst

# Now calculate the instalment size
PP=[mismil(xx,yy,int, target) for xx in id for yy in y]

# All the combinations of Amount and Year
NN=[[ii,jj] for ii in id for jj in y]

# Now the required Data Frame
SS=pd.DataFrame({'Cond': NN, 'Inst': PP})
