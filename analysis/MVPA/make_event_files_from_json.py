# -*- coding: utf-8 -*-
"""
Make event files from model.json for using with SpecifyModel
Created on Mon Jul 13 15:03:15 2015

@author: poldrack
"""

import os

def MakeEventFilesFromJSON(j,outdir):

    if not os.path.exists(outdir):
        os.makedirs(outdir)
    variables=[int(i) for i in j['Variables'].keys()]
    variables.sort()
    
    for i in variables:
        v=j['Variables'][str(i)]
        f=open(os.path.join(outdir,'%s.run001.txt'%v['VariableName']),'w')
        for ons in v['onsets']:
            f.write("%s\n"%'\t'.join([str(x) for x in ons]))
        f.close()