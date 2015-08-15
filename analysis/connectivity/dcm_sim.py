
# coding: utf-8

# In this notebook we will implement a simplified version of the DCM model, in order to generate data for subsequent examples.

# In[13]:

import numpy
import os,sys
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy.integrate import odeint
import math
from nipy.modalities.fmri.hemodynamic_models import spm_hrf,compute_regressor


def dcm_model(t,z,A,B,C,u,timepoints):
    ut=numpy.abs(timepoints - t).argmin()
    return (A.dot(z)+ u[ut]*B.dot(z) + C.dot(u[ut]).T)[0]

def mk_dcm_dataset(A,B,C,u,timepoints,noise_sd,stepsize=.01):
    data=numpy.zeros((len(timepoints),A.shape[0]))
    for i in range(1,len(timepoints)):
        data[i,:]=data[i-1,:] + dcm_model(timepoints[i],data[i-1,:],A,B,C,u,timepoints)  + numpy.random.randn(A.shape[0])*noise_sd
    hrf=spm_hrf(stepsize,oversampling=1)
    data_conv=numpy.zeros(data.shape)
    for i in range(A.shape[0]):
        data_conv[:,i]=numpy.convolve(data[:,i],hrf)[:data.shape[0]]
    return data,data_conv

def sim_dcm_dataset():

    sys.path.insert(0,'../utils')
    from mkdesign import create_design_singlecondition


    # first let's build the model without the bilinear influence (aka PPI)
    # after http://spm.martinpyka.de/?p=81
    nregions=5
    z=numpy.zeros(nregions)

    # intrinsic connectivity
    A=numpy.zeros((z.shape[0],z.shape[0]))
    A=numpy.diag(numpy.ones(z.shape[0])*-1)
    # add some structure
    #A=A + numpy.diag(numpy.ones(z.shape[0]-1),k=-1)
    A[2,1]=1
    A[3,1]=1
    B=numpy.zeros(A.shape)
    B[2,0]=1
    B[4,0]=1

    C=numpy.zeros((z.shape[0],1))
    C[0]=1
    u=0

    print A
    print B
    print C

    # we are assuming a 1 second TR for the resulting data
    # but the neural data are at a 1/16 millisecond time resolution

    tslength=300
    stepsize=.01
    timepoints=numpy.arange(0,tslength,stepsize)
    noise_sd=10

    # create a blocked design
    d,design=create_design_singlecondition(blockiness=1.0,deslength=tslength,blocklength=20,offset=20)

    u=scipy.interpolate.griddata(numpy.arange(1,d.shape[0]),d,timepoints,fill_value=0)
    data,data_conv=mk_dcm_dataset(A,B,C,u,timepoints,noise_sd,stepsize=stepsize)
    return data,data_conv

if __name__ == "main":
    d=sim_dcm_dataset()
