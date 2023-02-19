""" Script for testing functionality of the SmartEnergyNode class.
"""

import datetime
import json
import time
import random
import signal
import sys

from classes.smart_energy_device import SmartEnergyDevice
from classes.smart_energy_node import SmartEnergyNode

DEBUG = True
LOOPTICK = 1 # seconds
RUN = True

SEDS = 3
SENS = 1
SED = []
SEN = []

def sig_handler(sig, frame):
    """ Signal handler to shutdown simulation """
    print("DEBUG Ctrl-C pressed.")
    RUN = False
    for sed in SED:
        sed.halt()
    for sen in SEN:
        sen.halt()
    sys.exit(0)
    
def random_opdata():
    """ Create a set of random 'op_data' """
    return {
        'power': round(random.uniform(3.3, 240), 2),
        'current': round(random.uniform(0.001, 16.7), 2),
        'temp': round(random.uniform(-25.0, 49.9), 2),
        'wind': round(random.uniform(0.0, 90.0), 2)
    }
    
def create_devices():
    """ Create simoulation devices"""
    for cnt in range(0, SEDS):
        sedname = 'sed' + str(cnt)
        sedaddress = 'bus00:line27:00' +  'sed' + str(cnt) 
        sed = SmartEnergyDevice(name = sedname, 
            description='Some device ' + str(cnt)
        )
        sed.set_data('op_data', random_opdata())
        SED.append(sed)
    print("SEDs created:")
    for dev in SED:
        print('\t', dev.get_id())
    
def create_nodes():
    """ Create simulation nodes"""
    for cnt in range(0, SENS):
        senname = 'sen' + str(cnt)
        sen = SmartEnergyNode(name=senname, 
            address='Serverschrank0:Patch1:' + str(cnt), 
            description='Haus-Server ' + str(cnt)
        )
        sen.connect_node(name='DE-NRW-KR-Fischeln-27-0813', 
            address='2a02:908:1398:9020:188e:1694:74e4:bdf'
        ) # Imaginary 'Munizipal-Server-KR1'
        SEN.append(sen)
    print("SENs created:")
    for node in SEN:
        print('\t', node.get_id())
        
def connect_devices():
    """ Connect simulated SEDs to SENs """
    for nr in range(0, SEDS):
        SEN[0].connect_device(SED[nr], '01234567890')

# --- main() -----------------------------------------------------------------
signal.signal(signal.SIGINT, sig_handler)
create_devices()
create_nodes()
connect_devices()

# Start simulation loop
tick = 0
while RUN:
    time.sleep(LOOPTICK)
    tick += 1
    if 0 == tick % 5 and DEBUG:
        print("DEBUG main() heartbeat @", datetime.datetime.now())
    # --- Simulation / single events -----------------------------------------
    if 10 == tick:
        # try: connect already connected SED
        SEN[0].connect_device(SED[0], '01234567890')
        # try: regular disconnect
    if 15 == tick:
        SEN[0].disconnect_device(SED[1].get_id())
    
    # --- Simulation / recurring events --------------------------------------
    if 0 == tick % 10:
        SEN[0].send_device(SED[0].get_id(), {'msg': 'send battery load'})
    if 0 == tick % 15:
        SEN[0].send_device(SED[1].get_id(), {'query': 'should I power up?'})