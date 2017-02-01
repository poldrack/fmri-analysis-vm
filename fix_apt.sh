sudo rm -rf /var/lib/apt/lists
sudo mkdir -p /var/lib/apt/lists/partial
sudo rm -rf /var/cache/apt/archives
sudo mkdir -p /var/cache/apt/archives
sudo apt-get update
sudo apt-get install swig
pip install --upgrade pip
pip install pymvpa2

