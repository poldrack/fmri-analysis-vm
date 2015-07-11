#!/usr/bin/env python
"""
implement the frame displacement measure described by Power et al. (2011)
"""


import numpy as N
import os,sys

# load the datafile
def compute_fd(motpars):

    # compute absolute displacement
    dmotpars=N.zeros(motpars.shape)
    
    dmotpars[1:,:]=N.abs(motpars[1:,:] - motpars[:-1,:])
    
    # convert rotation to displacement on a 50 mm sphere
    # mcflirt returns rotation in radians
    # from Jonathan Power:
    #The conversion is simple - you just want the length of an arc that a rotational
    # displacement causes at some radius. Circumference is pi*diameter, and we used a 5
    # 0 mm radius. Multiply that circumference by (degrees/360) or (radians/2*pi) to get the 
    # length of the arc produced by a rotation.
    
    
    headradius=50
    disp=dmotpars.copy()
    disp[:,0:3]=N.pi*headradius*2*(disp[:,0:3]/(2*N.pi))
    
    FD=N.sum(disp,1)
    
    
    return FD

def compute_dvars(maskmean):
    mean_running_diff=N.zeros(len(maskmean))
    mean_running_diff=(maskmean[1:]-maskmean[:-1])/((maskmean[1:]+maskmean[:-1])/2.0)
    DVARS=N.zeros(len(maskmean))
    DVARS[1:]=N.sqrt(mean_running_diff**2)*100.0
    return DVARS
    