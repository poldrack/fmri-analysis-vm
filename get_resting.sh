cd ~/data/ds031
if [ ! -d sub-01 ] 
then
   mkdir sub-01
fi
cd sub-01

if [ ! -d ses-105 ] 
then
   mkdir ses-105
   mkdir ses-105/func
fi
cd ses-105/func

wget http://web.stanford.edu/group/poldracklab/myconnectome-data/raw_rsfmri/rsfmri_nifti/ses-105/func/sub-01_ses-105_task-rest_run-001_bold.json 
wget http://web.stanford.edu/group/poldracklab/myconnectome-data/raw_rsfmri/rsfmri_nifti/ses-105/func/sub-01_ses-105_task-rest_run-001_bold.nii.gz 
