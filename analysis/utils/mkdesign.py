"""
make design for fmri
"""

import os
import numpy

# assume 1 second spacing for now
def create_design_singlecondition(deslength=400,blockiness=1.0,density=0.5,
    blocklength=30.,offset=None):
    """
    create a new design with a single condition
    return both the stick function and a set of (onset, duration, amplitude) triples
    """

    if not offset:
        offset=blocklength

    design=numpy.zeros(deslength)
    nevents=round(deslength*density)
    nblocks=(deslength*density)/blocklength
    baselength=(deslength*(1.-density))/nblocks
    blockstarts=numpy.arange(offset,deslength,blocklength+baselength)
    for b in blockstarts:
        design[b:b+blocklength]=1

    if blockiness<1.0:
        # add stochastic design by flipping trials into rest periods
        for i in range(int(nevents*(1.-blockiness))):
            events=numpy.where(design==1)[0]
            numpy.random.shuffle(events)
            nulls=numpy.where(design==0)[0]
            numpy.random.shuffle(nulls)
            design[nulls[0]]=1
            design[events[0]]=0

    onsets=numpy.where(design==1)[0]
    durations=numpy.ones(onsets.shape)
    amplitudes=numpy.ones(onsets.shape)
    return design,(onsets,durations,amplitudes)

def create_design_twocondition(deslength=400,correlation=0.0,density=0.5,blocklength=30):
    """
    create a new design with two conditions
    return a set of (onset, duration, amplitude) triples for each condition
    """
    offset=0
    design=numpy.zeros(deslength)
    nevents=round(deslength*density)
    nblocks=(deslength*density)/blocklength
    baselength=(deslength*(1.-density))/nblocks
    blockstarts=numpy.arange(offset,deslength,blocklength+baselength)
    for b in blockstarts:
        design[b:b+blocklength:2]=1
        design[b+1:b+blocklength:2]=2


    if correlation<1.0:
        # add stochastic design by flipping trials into rest periods
        for i in range(int(nevents*(1. - correlation))):
            events=numpy.where(design>0)[0]
            numpy.random.shuffle(events)
            nulls=numpy.where(design==0)[0]
            numpy.random.shuffle(nulls)
            design[nulls[0]]=design[events[0]]
            design[events[0]]=0

    onsets1=numpy.where(design==1)[0]
    durations1=numpy.ones(onsets1.shape)
    amplitudes1=numpy.ones(onsets1.shape)
    onsets2=numpy.where(design==2)[0]
    durations2=numpy.ones(onsets2.shape)
    amplitudes2=numpy.ones(onsets2.shape)
    return design,(onsets1,durations1,amplitudes1),(onsets2,durations2,amplitudes2)
