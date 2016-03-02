# Get dependacies
sudo apt-get update
sudo apt-get install htop scons cmake libjpeg8-dev oracle-java8-jdk

# Install mjpg-straemer
mkdir ~/vision
cd ~vision
git clone https://github.com/jacksonliam/mjpg-streamer.git

# Install WS2812B Python Driver
cd ~/
git clone https://github.com/popoklopsi/rpi_ws281x.git

# Install GRIP dependacies
mkdir ~/vision/grip


