cd ~/nilearn_data
if [ ! -d haxby2001 ] 
then
   mkdir haxby2001
fi
cd haxby2001

if [ ! -f /home/vagrant/nilearn_data/haxby2001/subj2/blockmodel ]
then
    wget --cut-dirs=3 https://www.dropbox.com/s/oraxxgas88khsjx/haxby_modeldata.tgz
    tar zxvf haxby_modeldata.tgz
    rm haxby_modeldata.tgz
fi
