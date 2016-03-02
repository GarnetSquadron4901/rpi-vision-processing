# rpi-vision-processing
Garnet Squadron 4901 Vision Processing for the Raspberry Pi 2 using GRIP, WS2812B LEDs and the Raspberry Pi Camera

Steps:

Install Raspbian Jessie Lite onto Micro-SD Card.

Login: Username:pi; Password:raspberry

1) Run raspi-config:

  sudo raspi-config
  
  a) Expand Filesystem
  
  b) Boot Options -> B2 - Console Autologin
 
  c) Wait for Network at Boot -> Fast Boot without waiting for network connection
  
  d) International Options -> Change Keyboard Layout -> Generic 105-key (Intl) PC -> Other -> English (US) -> English (US) -> The default for the keyboard layout -> No compose key
  
  e) Enable Camera -> Enable
  
  f) Overlock -> High
  
  g) Finish -> Reboot? Yes

2) sudo apt-get update

3) sudo apt-get upgrade

4) sudo apt-get install subversion

5) sudo rpi-update

6) sudo reboot

7) svn co https://github.com/GarnetSquardon4901/rpi-vision-processing.git/trunk/ ~/

8) chmod 755 setup-gv.sh

9) ./setup-gv.sh

10) Deploy GRIP to /home/pi/vision/grip

11) sudo reboot
