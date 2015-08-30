import nibabel
import numpy


infile='sub00001_ses014_task002_run001_bold.nii.gz'

img=nibabel.load(infile)
data=img.get_data()

newdata=numpy.zeros(data.shape)
ctr=0
for i in range(0,data.shape[3],2):
    print i
    newdata[:,:,:,ctr]=numpy.mean(data[:,:,:,i:i+2],3)
    ctr+=1
newdata=newdata[:,:,:,:ctr]
newimg=nibabel.Nifti1Image(newdata,img.get_affine())
newimg.to_filename('resampled.nii.gz')
