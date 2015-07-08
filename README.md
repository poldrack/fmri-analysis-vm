# fmri-analysis-vm
A VM setup for use in fMRI analysis and education.

## Setting up the virtual machine

1. Install [VirtualBox] (https://www.virtualbox.org/wiki/Downloads)

2. Install [Vagrant] (http://www.vagrantup.com/downloads) - Vagrant is a provisioning system that sets up the virtual machine.

3. If you don't already have it, install [git] (https://git-scm.com/downloads)

4.  cd to the directory where you want to house the project, and then clone the myconnectome vagrant setup:
`git clone https://github.com/poldrack/myconnectome-vm.git`

5. cd into the vm directory: `cd myconnectome-vm`

6. set up the vagrant VM (which may take a little while):
`vagrant up`

7.  Step 6 will automatically start the analysis processes, which will take several hours to complete.  Using a web browser on your local machine, view the results at [http://192.128.0.20:5000](http://192.128.0.20:5000)

## Digging deeper

If you wish to log into the virtual machine and look more closely at the results, you can do so from within the directory containing the Vagrantfile, using this command:

`vagrant ssh`

The code for the analyses along with all of the results are located in the myconnectome directory.

## Copying the data

If you wish to copy the data and results from the virtual machine to your host machine, you can do so by logging into the VM (using "vagrant ssh") and executing the following command:

`cp -r myconnectome /vagrant/`

This will place a copy of the results in the directory where the Vagrantfile is located on your host machine.

## If things go wrong

If the VM crashes for some reason (which can occur if there is a network hiccup when it is trying to download data), the best thing to do is to destroy the VM using the command:

`vagrant destroy`

And then restart it as outlined above.  

