#!/usr/bin/env python3
#
# This is a NetworkTables client (eg, the DriverStation/coprocessor side).
# You need to tell it the IP address of the NetworkTables server (the
# robot or simulator).
#
# When running, this will continue incrementing the value 'dsTime', and the
# value should be visible to other networktables clients and the robot.
#

import sys
import time
from networktables import NetworkTable
import networktables.util
import networktables2
import psutil

# To see messages from networktables, you must setup logging
import logging
logging.basicConfig(level=logging.DEBUG)

NetworkTable.setIPAddress('roborio-4901-frc.local')
NetworkTable.setClientMode()
NetworkTable.initialize()
    
rpi = NetworkTable.getTable('RPi')

rpi.putBoolean('run', True)
while rpi.getBoolean('run') == False:
	rpi.putBoolean('run', True)
	time.sleep(5)
	

while rpi.getBoolean('run'):
    try:
        for cpu in range(psutil.cpu_count()):
            rpi.putNumber('cpu'+str(cpu), psutil.cpu_percent(interval=1, percpu=True)[cpu])
        rpi.putNumber('ram_total', psutil.virtual_memory().total)
        rpi.putNumber('ram_available', psutil.virtual_memory().available)
        rpi.putNumber('disk_total', psutil.disk_usage('/').total)
        rpi.putNumber('disk_available', psutil.disk_usage('/').free)
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print (e)
    time.sleep(0.2)
	


   
