cd ~/data/ds031
if [ ! -d sub-01 ] 
then
   mkdir sub-01
fi
cd sub-01

if [ ! -f /home/vagrant/data/ds031/sub-01/ses-105/mcflirt/sub-01_ses-105_task-rest_run-001_bold_mcf.nii.gz ]
then
    wget --cut-dirs=6  http://web.stanford.edu/group/poldracklab/myconnectome-data/raw_rsfmri/rsfmri_nifti/ses-105.tgz
    tar zxvf ses-105.tgz
    rm ses-105.tgz
fi
if [ ! -d roidata ]
then
  mkdir roidata
fi
cd roidata
for ses in 014 015 016 017 018 019 
do
   if [ ! -f sub${ses}.txt ]
   then
       wget --cut-dirs=6 http://web.stanford.edu/group/poldracklab/myconnectome-data/base/combined_data_scrubbed/sub${ses}.txt
   fi
done
wget --cut-dirs=6 http://web.stanford.edu/group/poldracklab/myconnectome-data/base/parcellation/parcel_data.txt
