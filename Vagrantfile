# this was adapted from nipype Vagrantfile

VAGRANTFILE_API_VERSION = "2"

$script = <<SCRIPT


# # Install neurodebian repo
bash <(wget -q -O- http://neuro.debian.net/_files/neurodebian-travis.sh)

wget -O- http://neuro.debian.net/lists/precise.us-ca.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
sudo apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9
sudo apt-get update > /dev/null

if [ ! -d $HOME/miniconda ]
then
 # install anaconda
 wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O miniconda.sh
 chmod +x miniconda.sh
 ./miniconda.sh -b
 echo "export PATH=$HOME/miniconda/bin:\\$PATH" >> .bashrc
 echo "export PATH=$HOME/miniconda/bin:\\$PATH" >> .env
fi

echo 'export FSLDIR=/usr/share/fsl/5.0' >> .bashrc
echo ". /usr/share/fsl/5.0/etc/fslconf/fsl.sh"  >> .bashrc

# install nipype dependencies
$HOME/miniconda/bin/conda update --yes conda
$HOME/miniconda/bin/pip install setuptools
$HOME/miniconda/bin/conda install --yes pip numpy scipy nose traits networkx
$HOME/miniconda/bin/conda install --yes dateutil ipython-notebook matplotlib
$HOME/miniconda/bin/conda install --yes statsmodels boto  pandas scikit-learn
$HOME/miniconda/bin/conda install --yes sypder-app
$HOME/miniconda/bin/pip install nibabel
$HOME/miniconda/bin/pip install nilearn

$HOME/miniconda/bin/easy_install nipype

echo 'deb http://cran.rstudio.com/bin/linux/ubuntu precise/' >/tmp/myppa.list
sudo cp /tmp/myppa.list /etc/apt/sources.list.d/
rm /tmp/myppa.list

sudo apt-get update > /dev/null
sudo apt-get install -y --force-yes libgd2-xpm
sudo apt-get install -y --force-yes libicu48
sudo apt-get install -y --force-yes r-base 
sudo apt-get install -y --force-yes git 
sudo apt-get install -y --force-yes fsl-complete
sudo apt-get install -y --force-yes xserver-xorg-core
sudo apt-get install -y --force-yes iceweasel
sudo apt-get install -y --force-yes xfce4 
sudo apt-get install -y --force-yes virtualbox-guest-dkms virtualbox-guest-utils virtualbox-guest-x11


if [ ! -d $HOME/R_libs ]
then
mkdir $HOME/R_libs
echo "export R_LIBS_USER=$HOME/R_libs" >> .bashrc
echo "export R_LIBS_USER=$HOME/R_libs" >> .env
fi

# get ds003 data
if [ ! -d $HOME/data ]
then
  mkdir $HOME/data
  wget http://openfmri.s3.amazonaws.com/tarballs/ds003_raw.tgz -O $HOME/data/ds003_raw.tgz
  tar zxvf $HOME/data/ds003_raw.tgz -C $HOME/data/
fi

sudo VBoxClient --display -d
sudo VBoxClient --clipboard -d
sudo VBoxManage setextradata global GUI/MaxGuestResolution any

SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.ssh.forward_x11 = true

  config.vm.define :engine do |engine_config|
    engine_config.vm.box = "precise64"
    engine_config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    engine_config.vm.network :private_network, ip: "192.128.0.20"
    engine_config.vm.hostname = 'fmri-analysis'
    #engine_config.vm.synced_folder "/tmp/myconnectome", "/home/vagrant/myconnectome", create: true

    engine_config.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      vb.customize ["modifyvm", :id, "--ioapic", "on"]
      vb.customize ["modifyvm", :id, "--memory", "8192"]
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.gui = true
    end

    engine_config.vm.provision "shell", :privileged => false, inline: $script
  end
end
