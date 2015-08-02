# -*- coding: utf-8 -*-
"""
Spyder Editor

get info about haxby data for classification/MVPA analysis

"""

import os
import numpy

class HaxbyData:

    def __init__(self,datadir):
        self.tr=2.5
        
        self.boldfile=os.path.join(datadir,'bold.nii.gz')
        self.boldbrainfile=os.path.join(datadir,'bold_brain.nii.gz')
        self.vtmaskfile=os.path.join(datadir,'mask4_vt.nii.gz')
        self.brainmaskfile=os.path.join(datadir,'bold_brain_mask.nii.gz')

        # load the event info
        labelfile=os.path.join(datadir,'labels.txt')
        lines=open(labelfile).readlines()
        lines=lines[1:] # drop header
        

        # find all block onsets
        self.conditions=[]
        self.condnums=[]
        self.onsets=[]
        self.durations=[]
        self.runs=[]
        cond=''
        
        self.cond_dict={'scissors':1,
         'face':2,
         'cat':3,
         'shoe':4,
         'house':5,
         'scrambledpix':6,
         'bottle':7,
         'chair':8}
        self.condlabels=['scissors','face','cat','shoe','house','scrambledpix','bottle','chair']
        
        for i in range(len(lines)):
            l_s=lines[i].strip().split()
            if l_s[0]=='rest':
                continue
            if not l_s[0]==cond:
                cond=l_s[0]
                self.runs.append(int(l_s[1]))
                self.conditions.append('-'.join(l_s))
                self.condnums.append(self.cond_dict[l_s[0]])
                self.onsets.append([self.tr*(i+1)])
                self.durations.append([22.5])
            
        self.condnums=numpy.array(self.condnums)
        self.runs=numpy.array(self.runs)
