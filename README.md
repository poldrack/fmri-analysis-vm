# fmri-analysis-vm
A VM setup for use in fMRI analysis and education.

## How to build the machine

1. Install [VirtualBox >= 5.0] (https://www.virtualbox.org/wiki/Downloads)

2. Install [Vagrant] (http://www.vagrantup.com/downloads) - Vagrant is a provisioning system that sets up the virtual machine.

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

11. If you can use it shut it down and export it

  `VBoxManage export fmri-analysis --ovf20 --output /path/to/fmri_training_vm.ova`

12. Redistribute the .ova file via Dropbox or Google Drive.

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
To avoid conflicts when commiting IPython Notebook changes you need to run the following commands (from the roon the the repo):

1. `chmod +x scripts/ipynb_drop_output`
2. `export PATH=$PWD/scripts/:$PATH`
3. `git config --add include.path $PWD/.gitconfig`
