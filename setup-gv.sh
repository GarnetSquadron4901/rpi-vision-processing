# Get dependacies
sudo apt-get update
sudo apt-get install htop scons cmake libjpeg8-dev python-pip oracle-java8-jdk
sudo pip install pyro

# Install mjpg-streamer
cd vision
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
sudo make clean
sudo make install

# Install WS2812B Python Driver
cd ..
git clone https://github.com/popoklopsi/rpi_ws281x.git
cd rpi_ws281x.git
sudo scons

# Make shell scripts executable
cd ..
chmod 755 *.sh




