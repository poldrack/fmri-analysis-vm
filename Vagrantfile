# this was adapted from nipype Vagrantfile

VAGRANTFILE_API_VERSION = "2"

$script = <<SCRIPT

if [ ! -d $HOME/miniconda ]
then
 # install anaconda
 wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O miniconda.sh
 chmod +x miniconda.sh
 ./miniconda.sh -b
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
sudo DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" dist-upgrade -y
sudo apt-get install -y r-base \
git \
fsl-core \
fsl-atlases

echo 'export FSLDIR=/usr/share/fsl/5.0' >> .bashrc
echo ". /usr/share/fsl/5.0/etc/fslconf/fsl.sh"  >> .bashrc

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
fi

sudo VBoxClient --display -d
sudo VBoxClient --clipboard -d

SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    
  config.ssh.forward_x11 = true

  config.vm.box = "boxcutter/ubuntu1404-desktop"
  config.vm.network :private_network, ip: "192.128.0.20"
  config.vm.hostname = 'fmri-analysis'
    
  if Vagrant.has_plugin?("vagrant-cachier")
        # Configure cached packages to be shared between instances of the same base box.
        # More info on http://fgrehm.viewdocs.io/vagrant-cachier/usage
        config.cache.scope = :box

        # OPTIONAL: If you are using VirtualBox, you might want to use that to enable
        # NFS for shared folders. This is also very useful for vagrant-libvirt if you
        # want bi-directional sync
        config.cache.synced_folder_opts = {
          type: :nfs,
          # The nolock option can be useful for an NFSv3 client that wants to avoid the
          # NLM sideband protocol. Without this option, apt-get might hang if it tries
          # to lock files needed for /var/cache/* operations. All of this can be avoided
          # by using NFSv4 everywhere. Please note that the tcp option is not the default.
          mount_options: ['rw', 'vers=3', 'tcp', 'nolock']
        }
        # For more information please check http://docs.vagrantup.com/v2/synced-folders/basic_usage.html
  end

   config.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--ioapic", "on"]
      vb.customize ["modifyvm", :id, "--memory", "4096"]
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
