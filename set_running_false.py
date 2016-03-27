import time
from networktables import NetworkTable

# To see messages from networktables, you must setup logging
import logging
logging.basicConfig(level=logging.DEBUG)

NetworkTable.setIPAddress('roborio-4901-frc.local')
NetworkTable.setClientMode()
NetworkTable.initialize()
    
rpi = NetworkTable.getTable('RPi')

while rpi.getBoolean('running') == True:
    rpi.putBoolean('running', False)
    time.sleep(1)