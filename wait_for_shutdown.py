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

cpu_utilization_type = networktables2.type.NumberArray()

for core in range(psutil.cpu_count()):
    cpu_utilization_type.append(0)

# Setup variables
run =             networktables.util.ntproperty('/RPi/RunCommand', True, writeDefault = True)
cpu_utilization = networktables.util.ntproperty('/RPi/CPU Utilization/Cores', cpu_utilization_type, writeDefault = True)
ram_total =       networktables.util.ntproperty('/RPi/Memory/Total', 0, writeDefault = True)
ram_available =   networktables.util.ntproperty('/RPi/Memory/Available', 0, writeDefault = True)
disk_total =      networktables.util.ntproperty('/RPi/Disk/Total', 0, writeDefault = True)
disk_available =  networktables.util.ntproperty('/RPi/Disk/Available', 0, writeDefault = True)

while run:
    try:
        cpu_utilization = psutil.cpu_percent(interval=1, percpu=True)
        ram_total = psutil.virtual_memory().total
        ram_available = psutil.virtual_memory().available
        disk_total = psutil.disk_usage('/').total
        disk_available = psutil.disk_usage('/').free
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print (e)
    time.sleep(0.2)

   
