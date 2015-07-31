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
spyder
$HOME/miniconda/bin/pip install nibabel nilearn nipype

wget -O- http://neuro.debian.net/lists/trusty.us-ca.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
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
chromium-browser

wget --quiet https://github.com/stnava/ANTs/releases/download/v2.1.0/Linux_Ubuntu14.04.tar.bz2
tar jxvf Linux_Ubuntu14.04.tar.bz2
echo "export PATH=$HOME/ANTs.2.1.0.Debian-Ubuntu_X64:\\$PATH" >> .bashrc
echo "export PATH=$HOME/ANTs.2.1.0.Debian-Ubuntu_X64:\\$PATH" >> .env
rm -rf Linux_Ubuntu14.04.tar.bz2

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

# get ds003 data
if [ ! -d $HOME/data ]
then
  mkdir $HOME/data
  wget http://openfmri.s3.amazonaws.com/tarballs/ds003_raw.tgz -O $HOME/data/ds003_raw.tgz -nv
  tar zxvf $HOME/data/ds003_raw.tgz -C $HOME/data/
  rm -rf $HOME/data/ds003_raw.tgz
  wget https://s3.amazonaws.com/openfmri/ds031/ds031_example_data.tgz -O $HOME/data/ds031_example.tgz -nv
  tar zxvf $HOME/data/ds031_example_data.tgz -C $HOME/data/
  rm -rf $HOME/data/ds031_example_data.tgz
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
  config.vm.network :private_network, ip: "192.128.0.20"
  config.vm.hostname = 'fmri-analysis'

   config.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--ioapic", "on"]
      vb.customize ["modifyvm", :id, "--memory", "5120"]
      vb.customize ["modifyvm", :id, "--cpus", "2"]
      vb.customize ["setextradata", :id, "GUI/MaxGuestResolution", "any"]
      vb.gui = true
      vb.name = "fmri-analysis"
  end

    config.vm.provision "shell", :privileged => false, inline: $script

    config.push.define "atlas" do |push|
      push.app = "poldracklab/fmri-analysis"
    end

end
