cd ~/data/ds031
if [ ! -d sub-01 ] 
then
   mkdir sub-01
fi
cd sub-01

wget --cut-dirs=6  http://web.stanford.edu/group/poldracklab/myconnectome-data/raw_rsfmri/rsfmri_nifti/ses-105.tgz
#wget --cut-dirs=6 --recursive  http://web.stanford.edu/group/poldracklab/myconnectome-data/raw_rsfmri/rsfmri_nifti/ses-105/fmap
tar zxvf ses-105.tgz
rm ses-105.tgz
