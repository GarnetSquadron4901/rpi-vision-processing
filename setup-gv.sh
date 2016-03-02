#!/bin/bash

# Get dependacies
echo "Installing dependancies..."
sudo apt-get install git htop scons cmake libjpeg8-dev python3 python-pip oracle-java8-jdk build-essential python-dev swig
sudo pip install pyro4 pynetworktables psutil

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

echo "~/gv-service.sh &" >> ~/.profile



