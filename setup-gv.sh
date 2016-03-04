#!/bin/bash

# Get dependacies
echo "Installing dependancies..."
sudo apt-get install build-essential cmake git htop imagemagick libjpeg8-dev oracle-java8-jdk python-dev python-pip python3 scons swig
sudo pip install psutil pynetworktables pyro4

# Install mjpg-streamer
echo "Installing mjpg-streamer"
cd ~/vision
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make clean all
sudo make install

# Install WS2812B Python Driver
echo "Installing WS2812B Python Driver"
cd ~/
git clone https://github.com/popoklopsi/rpi_ws281x.git
cd rpi_ws281x 
scons
cd python
sudo python setup.py install

# Make shell scripts executable
cd ~/
chmod 755 *.sh

if (cat ~/.profile | grep gv-service.sh); then
	echo "gv-service already added to user profile login script."
else    
	echo "~/gv-service.sh &" >> ~/.profile
fi



