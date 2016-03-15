rpi-vision-processing
=====================

Garnet Squadron 4901 Vision Processing for the Raspberry Pi 2 using GRIP, WS2812B LEDs and the Raspberry Pi Camera

## Install Raspbian Jessie Lite onto Micro-SD Card
Download from https://www.raspberrypi.org/downloads/raspbian/

Install using directions found here: https://www.raspberrypi.org/documentation/installation/installing-images/windows.md

# First Boot
* Username:pi
* Password:raspberry

# Raspberry Pi Configuration
## Start raspi-config
sudo raspi-config
## Configuration Steps
1. Expand Filesystem
2. Boot Options -> B2 - Console Autologin
3. Wait for Network at Boot -> Fast Boot without waiting for network connection
4. International Options -> Change Keyboard Layout -> Generic 105-key (Intl) PC -> Other -> English (US) -> English (US) -> The default for the keyboard layout -> No compose key
5. Enable Camera -> Enable
6. Overclock -> High
7. (Optional, but recommended) Change the password.
8. Finish -> Reboot? Yes

# Vision Processing Setup Steps
1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo apt-get install subversion rpi-update
4. sudo rpi-update
5. sudo reboot
6. svn co https://github.com/GarnetSquardon4901/rpi-vision-processing.git/trunk/ ~/
7. chmod 755 setup-gv.sh
8. ./setup-gv.sh
9. At this point, you can deploy GRIP to /home/pi/vision/grip using GRIP on your computer.
10. sudo reboot
