"""
fix repetitoin time in json for downsampled data
"""

import shutil

infile='/home/vagrant/data/ds031/sub00001/ses014/functional/sub00001_ses014_task002_run001_bold.json'

lines=open(infile).readlines()
newlines=[]
for l in lines:
	if l.find('RepetitionTime')>-1:
		if l.find('1.16')>-1:
			newlines.append(l.replace('1.16','2.32'))
		else:
			newlines.append(l)
		print newlines[-1]
	else:
		newlines.append(l)
shutil.move(infile,infile.replace('.json','_orig.json'))
f=open(infile,'w')
for l in newlines:
	f.write(l)
f.close()
		
