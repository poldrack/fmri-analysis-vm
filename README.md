# fmri-analysis-vm
A VM setup for use in fMRI analysis and education.

## Setting up the virtual machine

1. Install [VirtualBox] (https://www.virtualbox.org/wiki/Downloads)

2. Install [Vagrant] (http://www.vagrantup.com/downloads) - Vagrant is a provisioning system that sets up the virtual machine.

3. Make sure your machine has at least 8Gb of RAM and 10Gb or free space.

4. Open a terminal, cd to the directory where you want to house the project, and then run the VM:
`vagrant init poldracklab/fmri-analysis; vagrant up --provider virtualbox`

5. Once the VM is downloaded (total of 2.1 Gb), you can log into the machine from the same directory using:
`vagrant ssh`
Once you have done this, you can start the windowing system by typing:
`startxfce4`

## Digging deeper

If you wish to log into the virtual machine and look more closely at the results, you can do so from within the directory containing the Vagrantfile, using this command:

`vagrant ssh`

The code for the analyses along with all of the results are located in the myconnectome directory.

## Copying the data

If you wish to copy the data and results from the virtual machine to your host machine, you can do so by logging into the VM (using "vagrant ssh") and executing the following command:

`cp -r <directory to copy> /vagrant/`

This will place a copy of the results in the directory where the Vagrantfile is located on your host machine.

## If things go wrong

If the VM crashes for some reason (which can occur if there is a network hiccup when it is trying to download data), the best thing to do is to destroy the VM using the command:

`vagrant destroy`

And then restart it as outlined above.  

## Building the Vagrant box

1. `git clone https://github.com/poldrack/fmri-analysis-vm.git`

2. `cd fmri-analysis-vm`

3. `vagrant up`

4. To push the image to Atlas see https://atlas.hashicorp.com/help/vagrant/boxes/create

## Contributing to the IPython Notebooks

`$ chmod +x scripts/ipynb_drop_output`
`$ export PATH=$PWD/scripts/ipynb_drop_output:$PATH`
`$ git config --add include.path $PWD/.gitconfig`
