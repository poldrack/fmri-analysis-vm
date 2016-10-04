# fmri-analysis-vm
A VM setup for use in fMRI analysis and education.

# Communication
To ask questions during the class use gitter: https://gitter.im/poldrack/fmri-analysis-vm (you will need GitHub account).

## How to install the machine
Warning: to be able to run this software you will need at least 8Gb of RAM and 20Gb of free hard drive space.

1. Install [VirtualBox >= 5.0] (https://www.virtualbox.org/wiki/Downloads)
2. Download the snapshot of the VM from http://web.stanford.edu/group/poldracklab/fmri-analysis-vm/fmri-analysis.ova
3. Install the VM using "File->Import Appliance" within VirtualBox.
4. Once it is installed, start the VM using the "start" button within VirtualBox.
5. This should bring up a virtual machine window.  Start a terminal using the menu at the bottom left "Accessories->LXTerm".
6. Update the analysis code.  first, cd into "fmri-analysis-vm", then type "git pull origin master"
7. Run the jupyter notebook server using the command "jupyter notebook"

## Errata

There are a few things that you need to do to address some missing files in the VM image.

1. Open the terminal from the menu at the bottom left: Accessories->LXTerminal.
2. Type $HOME/fmri-analysis-vm/run_me.sh


## How to build the machine

If you have trouble downloading the machine image above, you may want to try building the machine from scratch instead.

1. Install [VirtualBox >= 5.0] (https://www.virtualbox.org/wiki/Downloads)

2. Install [Vagrant] (https://www.vagrantup.com/downloads.html) - Vagrant is a provisioning system that sets up the virtual machine.

3. Make sure your machine has at least 8Gb of RAM and 10Gb or free space.

4. Open a terminal, cd to the directory where you want to house the project:

  `git clone https://github.com/poldrack/fmri-analysis-vm.git`

5. `cd fmri-analysis-vm`

6. Install guest vagrant plugins for guest additions and caching (those can fail on the first try - try again in such case):

  `vagrant plugin install vagrant-vbguest; vagrant plugin install vagrant-cachier`

7. Build the VM (this may take some time depending on your Internet connection):

  `vagrant up 2>&1 | tee -a provision.log`

8. Reinstall virtual box guest additions:

  `vagrant vbguest --do install`

9. Inspect `provision.log` looking for errors. Some download locations periodically go down.

10. If everything is ok reboot the machine and see if you can use it.

## How to export the machine

1. Shut down the machine and export it

  `VBoxManage export fmri-analysis --ovf20 --output /path/to/fmri_training_vm.ova`

2. Redistribute the .ova file via Dropbox or Google Drive.

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

## Contributing to the IPython Notebooks
To avoid conflicts when commiting IPython Notebook changes you need to run the following commands (from the root the the repo):

1. `chmod +x scripts/ipynb_drop_output`
2. `export PATH=$PWD/scripts/:$PATH`
3. `git config --add include.path $PWD/.gitconfig`
