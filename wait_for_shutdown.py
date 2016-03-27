#!/usr/bin/env python3
#
# This is a NetworkTables client (eg, the DriverStation/coprocessor side).
# You need to tell it the IP address of the NetworkTables server (the
# robot or simulator).
#
# When running, this will continue incrementing the value 'dsTime', and the
# value should be visible to other networktables clients and the robot.
#

import time
from networktables import NetworkTable
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
        rpi.putBoolean('running', True)
        cpu_utilization = psutil.cpu_percent(interval=1, percpu=True)
        for cpu in range(psutil.cpu_count()):
            rpi.putNumber('cpu'+str(cpu), cpu_utilization[cpu])
        rpi.putNumber('ram_total', psutil.virtual_memory().total)
        rpi.putNumber('ram_available', psutil.virtual_memory().available)
        rpi.putNumber('disk_total', psutil.disk_usage('/').total)
        rpi.putNumber('disk_available', psutil.disk_usage('/').free)
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print (e)
    time.sleep(0.1)
    
rpi.putBoolean('running', False)
time.sleep(1)
    


   
