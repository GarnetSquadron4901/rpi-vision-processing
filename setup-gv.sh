#!/bin/bash

# Get dependacies
echo "Updating apt-get..."
sudo apt-get update
echo "Installing dependancies..."
sudo apt-get install htop 
sudo apt-get install scons
sudo apt-get install cmake
sudo apt-get install libjpeg8-dev
sudo apt-get install python-pip
sudo apt-get install oracle-java8-jdk
sudo pip install pyro

# Install mjpg-streamer
cd vision
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
sudo make clean
sudo make install

# Install WS2812B Python Driver
cd ../../..
git clone https://github.com/popoklopsi/rpi_ws281x.git
cd rpi_ws281x.git
sudo scons

# Make shell scripts executable
cd ..
chmod 755 *.sh




