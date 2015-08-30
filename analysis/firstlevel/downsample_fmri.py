import nibabel
import numpy
import shutil

infile='/home/vagrant/data/ds031/sub00001/ses014/functional/sub00001_ses014_task002_run001_bold.nii.gz'

img=nibabel.load(infile)
data=img.get_data()
try:
	assert data.shape[3]==380
except:
	raise Exception('already corrected')

newdata=numpy.zeros(data.shape)
# NB: this is a poor way to resample!
ctr=0
for i in range(0,data.shape[3],2):
    print i
    newdata[:,:,:,ctr]=numpy.mean(data[:,:,:,i:i+2],3)
    ctr+=1
newdata=newdata[:,:,:,:ctr]
newimg=nibabel.Nifti1Image(newdata,img.get_affine(),img.get_header())
zooms=list(img.header.get_zooms())
zooms[3]=img.header.get_zooms()[3]*2
newimg.header.set_zooms(zooms)
shutil.move(infile,infile.replace('.nii.gz','_orig.nii.gz'))
newimg.to_filename(infile)
