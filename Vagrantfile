# this was adapted from nipype Vagrantfile

VAGRANTFILE_API_VERSION = "2"

$script = <<SCRIPT

if [ ! -d $HOME/miniconda ]
then
 # install anaconda
 wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O miniconda.sh
 chmod +x miniconda.sh
 ./miniconda.sh -b
 rm -rf miniconda.sh
 echo "export PATH=$HOME/miniconda/bin:\\$PATH" >> .bashrc
 echo "export PATH=$HOME/miniconda/bin:\\$PATH" >> .env
fi

wget -O- http://neuro.debian.net/lists/trusty.us-nh.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
sudo apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9

echo 'deb http://cran.cnr.Berkeley.edu/bin/linux/ubuntu trusty/' > /tmp/cran.sources.list
sudo cp /tmp/cran.sources.list /etc/apt/sources.list.d/
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9

sudo rm -rf /var/lib/apt/lists /var/cache/apt/archives
sudo apt-get update -y
#sudo DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" dist-upgrade -y

# workaround http://forums.debian.net/viewtopic.php?f=10&t=101659
sudo /usr/share/debconf/fix_db.pl
sudo apt-get install -y dictionaries-common
sudo /usr/share/debconf/fix_db.pl

sudo apt-get install -y r-base \
git \
fsl-core \
fsl-atlases \
lxde \
lightdm \
chromium-browser \
wget \
tar \
unzip

# install nipype dependencies
$HOME/miniconda/bin/conda update --yes conda
$HOME/miniconda/bin/conda install --yes pip \
numpy \
scipy \
nose \
traits \
networkx \
dateutil \
ipython-notebook \
matplotlib \
statsmodels \
boto \
pandas \
scikit-learn \
spyder \
sympy
$HOME/miniconda/bin/pip install nibabel nilearn nipy
$HOME/miniconda/bin/pip install --upgrade https://github.com/nipy/nipype/archive/master.zip
$HOME/miniconda/bin/pip install --process-dependency-links git+https://github.com/pymc-devs/pymc3

if [ ! -d $HOME/mcr ]
then
  echo "destinationFolder=$HOME/mcr" > mcr_options.txt
  echo "agreeToLicense=yes" >> mcr_options.txt
  echo "outputFile=/tmp/matlabinstall_log" >> mcr_options.txt
  echo "mode=silent" >> mcr_options.txt
  mkdir -p matlab_installer
  echo "downloading matlab runtime..."
  wget -nc --quiet http://www.mathworks.com/supportfiles/downloads/R2015a/deployment_files/R2015a/installers/glnxa64/MCR_R2015a_glnxa64_installer.zip -O $HOME/matlab_installer/installer.zip
  unzip $HOME/matlab_installer/installer.zip -d $HOME/matlab_installer/
  ./matlab_installer/install -inputFile mcr_options.txt
  echo "export LD_LIBRARY_PATH=$HOME/mcr/v85/runtime/glnxa64:$HOME/mcr/v85/bin/glnxa64:$HOME/mcr/v85/sys/os/glnxa64:\\$LD_LIBRARY_PATH" >> .bashrc
  echo "export LD_LIBRARY_PATH=$HOME/mcr/v85/runtime/glnxa64:$HOME/mcr/v85/bin/glnxa64:$HOME/mcr/v85/sys/os/glnxa64:\\$LD_LIBRARY_PATH" >> .env
  echo "export PATH=$HOME/mcr/v85/bin/:\\$PATH" >> .bashrc
  echo "export PATH=$HOME/mcr/v85/bin/:\\$PATH" >> .env
  rm -rf matlab_installer mcr_options.txt
fi

if [ ! -d $HOME/spm12 ]
then
  echo "downloading SPM..."
  wget --quiet http://www.fil.ion.ucl.ac.uk/spm/download/restricted/utopia/dev/spm12_r6472_Linux_R2015a.zip -O spm12.zip
  unzip spm12.zip
  echo 'alias spm="$HOME/spm12/run_spm12.sh $HOME/mcr/v85/"' >> .bashrc
  echo 'alias spm="$HOME/spm12/run_spm12.sh $HOME/mcr/v85/"' >> .env
  rm -rf spm12.zip
fi

if [ ! -d $HOME/ANTs.2.1.0.Debian-Ubuntu_X64 ]
then
  echo "downloading ANTs"
  wget --quiet https://github.com/stnava/ANTs/releases/download/v2.1.0/Linux_Ubuntu14.04.tar.bz2
  tar jxvf Linux_Ubuntu14.04.tar.bz2
  echo "export PATH=$HOME/ANTs.2.1.0.Debian-Ubuntu_X64:\\$PATH" >> .bashrc
  echo "export PATH=$HOME/ANTs.2.1.0.Debian-Ubuntu_X64:\\$PATH" >> .env
  rm -rf Linux_Ubuntu14.04.tar.bz2
fi

sudo sh -c 'echo "[SeatDefaults]
user-session=LXDE
autologin-user=vagrant
autologin-user-timeout=0" >> /etc/lightdm/lightdm.conf'

echo 'export FSLDIR=/usr/share/fsl/5.0' >> .bashrc
echo ". /usr/share/fsl/5.0/etc/fslconf/fsl.sh"  >> .bashrc
echo "export FMRIDATADIR=$HOME/data" >> .bashrc

if [ ! -d $HOME/R_libs ]
then
  mkdir $HOME/R_libs
  echo "export R_LIBS_USER=$HOME/R_libs" >> .bashrc
  echo "export R_LIBS_USER=$HOME/R_libs" >> .env
fi

# get example data
if [ ! -d $HOME/data ]
then
  mkdir $HOME/data
fi

if [ ! -d $HOME/data/ds003 ]
then
  echo "getting ds003 data"
  wget --quiet http://openfmri.s3.amazonaws.com/tarballs/ds003_raw.tgz -O $HOME/data/ds003_raw.tgz -nv
  tar zxvf $HOME/data/ds003_raw.tgz -C $HOME/data/
  rm -rf $HOME/data/ds003_raw.tgz
fi

if [ ! -d $HOME/data/ds009 ]
then
  echo "getting ds009 data"
  mkdir $HOME/data/ds009
  wget --quiet https://s3.amazonaws.com/openfmri/ds009/ds009_task002_copes.tgz -O $HOME/data/ds009_raw.tgz -nv
  tar zxvf $HOME/data/ds009_raw.tgz -C $HOME/data/ds009/
  rm -rf $HOME/data/ds009_raw.tgz
fi


if [ ! -d $HOME/data/ds031 ]
then
  echo "getting ds031 data"
  wget --quiet https://s3.amazonaws.com/openfmri/ds031/ds031_example_data.tgz -O $HOME/data/ds031_example.tgz -nv
  tar zxvf $HOME/data/ds031_example.tgz -C $HOME/data/
  rm -rf $HOME/data/ds031_example.tgz
fi

if [ ! -d $HOME/data/ds009 ]
then
  echo "getting ds009 copes"
  mkdir $HOME/data/ds009
  wget --quiet https://s3.amazonaws.com/openfmri/ds009/ds009_task002_copes.tgz -O $HOME/data/ds009_copes.tgz -nv
  tar zxvf $HOME/data/ds009_copes.tgz -C $HOME/data/ds009
  rm -rf $HOME/data/ds009_copes.tgz
fi

if [ ! -d $HOME/tetrad ]
then
 echo "setting up tetrad"
 mkdir $HOME/tetrad
 wget --quiet  http://www.phil.cmu.edu/projects/tetrad_download/download/tetrad-4.3.10-7.jar -O $HOME/tetrad/tetrad-4.3.10-7.jar
fi

# get this repo
if [ ! -d $HOME/fmri-analysis-vm ]
then
	git clone https://github.com/poldrack/fmri-analysis-vm
fi


sudo apt-get clean -y
sudo apt-get autoclean -y
sudo apt-get autoremove -y

sudo VBoxClient --display -d
sudo VBoxClient --clipboard -d

SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.ssh.forward_x11 = true

  config.vm.box = "ubuntu/trusty64"

   config.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--ioapic", "on"]
      vb.customize ["modifyvm", :id, "--memory", "5120"]
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["setextradata", :id, "GUI/MaxGuestResolution", "any"]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
      vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
      vb.customize ["modifyvm", :id, "--vram", "64"]
      vb.gui = true
      vb.name = "fmri-analysis"
  end
    # uncomment following line to allow syncing to local machine
    #config.vm.synced_folder ".", "/vagrant"
    config.vm.provision "shell", :privileged => false, inline: $script

    config.push.define "atlas" do |push|
      push.app = "poldracklab/fmri-analysis"
    end

end
