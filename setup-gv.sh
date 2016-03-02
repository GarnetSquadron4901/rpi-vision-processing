#!/bin/bash

# Get dependacies
echo "Updating apt-get..."
sudo apt-get update
echo "Installing dependancies..."
sudo apt-get install htop scons cmake libjpeg8-dev python-pip oracle-java8-jdk
sudo pip install pyro

# Install mjpg-streamer
echo "Installing mjpg-streamer"
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make clean all
sudo make install

# Install WS2812B Python Driver
echo "Installing WS2812B Python Driver"
cd -
git clone https://github.com/popoklopsi/rpi_ws281x.git
cd rpi_ws281x 
sudo scons

# Make shell scripts executable
cd -
chmod 755 *.sh




