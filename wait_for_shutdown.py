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
import psutil

# To see messages from networktables, you must setup logging
import logging
logging.basicConfig(level=logging.DEBUG)

ip = 'roborio-4901-frc.local'

NetworkTable.setIPAddress(ip)
NetworkTable.setClientMode()
NetworkTable.initialize()

run = True

sd = NetworkTable.getTable("SmartDashboard")
sd.putBoolean('RaspberryPiRunCommand', run)

while run:
    try:
        run = sd.getNumber('robotTime')
        sd.getBoolean('RaspberryPiRunCommand', defaultValue=True)
        print 'RoboRIO Connected'
    except KeyError:
        print 'RoboRIO Disconnected'\
        
    try:
        coreUtilization = psutil.cpu_percent(interval=1, percpu=True)
        for coreNum in range(len(coreUtilzation)):
            sd.putNumber('/RPi/CPU Utilization/Core {}'.format(coreNum), coreUtilization[coreNum])
        sd.putNumber('/RPi/Memory/Total', psutil.virtual_memory().total)
        sd.putNumber('/RPi/Memory/Available', psutil.virtual_memory().available)
        sd.putNumber('/RPi/Disk/Total', psutil.disk_usage('/').total)
        sd.putNumber('/RPi/Disk/Available', psutil.disk_usage('/').available)
    except:
        pass
    
