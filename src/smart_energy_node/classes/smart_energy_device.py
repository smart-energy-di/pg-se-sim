""" SmartEnergyDevice class definition
    role: 'consumer', 'producer', 'prosumer'
    comms: 'listen', 'talk'
"""

import json
import uuid
import time
import threading
import queue

class SmartEnergyDevice:
    """ class data """
    __instance_count = 0
    
    # --- instance management ------------------------------------------------
    
    def __init__(self, name, description=None):
        """ Class update """
        self.DEBUG = True
        SmartEnergyDevice.__instance_count += 1
        if self.DEBUG:
            print("DEBUG SmartEnergyDevice() instance nr.",
                SmartEnergyDevice.__instance_count)
        """ instance data """
        self.CONNECT = 'connect'
        self.DISCONNECT = 'disconnect'
        self.INITKEY = '01234567890'
        self.QTIMEOUT = 5 # seconds
        self.HBEAT = 0.25 # seconds
        # SED data
        uid = uuid.uuid4()
        self.id = name + '><' + str(uid)
        self.description = description
        self.uuid = uid
        self.name = name
        self.description = description
        self.role = 'consumer'
        self.comms = 'listen'
        self.status = 'disconnect'
        self.msgq = queue.Queue() # message queue 
        self.SENstore = {} # connected SME nodes
        self.key = self.INITKEY
        self.data = {
            'id': self.id,
            'name': self.name,
            'uuid': self.uuid,
            'role': self.role,
            'comms': self.comms,
        }      
        # Start working
        self.run = True
        self.thread = threading.Thread( target=self.heartbeat )
        self.thread.start()
        
    def __del__(self):
        """ Destruction """
        pass
                
    # --- internal operations ------------------------------------------------

    def heartbeat(self):
        """ Cyclic worker """
        while self.run:
            msg = self.recv_message()
            if {} != msg:
                self.proc_message(msg)
            time.sleep(self.HBEAT)
        
    def halt(self):
        """ Stop and join """
        self.run = False
        self.thread.join()
        if self.DEBUG:
            print("DEBUG SMEdevice", self.id , "halted.")
    
    def new_key(self):
        """ create a new key """
        #TODO implement secure key generation
        return 'new_key_template'
    
    # --- connectivity -------------------------------------------------------

    def connect(self, SEN_id, initial_key):
        """ Connect device to node """
        DSTRING = "DEBUG " + self.name + ".connect(" + SEN_id + ") "
        if self.DEBUG:
            print(DSTRING + "START")
        if self.CONNECT == self.status:
            msg = { 'worked': False, 'msg': 'Already connected' }
        elif self.key != initial_key:
            msg = { 'worked': False, 'msg': 'Wrong key passed'}
        else:
            self.key = self.new_key()
            self.SENstore[SEN_id] = { 'status': self.CONNECT }
            msg = {
                'worked': True,
                'id': self.id,
                'key': self.key,
                'msgq': self.msgq,
                'msg': '' 
            }
        if self.DEBUG:
            print(DSTRING + "COMPLETE, msg=" + str(msg))
        return msg
        
    def disconnect(self, SEN_id):
        """ Disconnect device from node """
        DSTRING = "DEBUG " + self.name + ".disconnect(" + SEN_id + ") "
        if SEN_id in self.SENstore:
            self.SENstore[SEN_id] = { 'status': self.DISCONNECT }
            msg = { 'worked': True, 'msg': '' }
        else:
            msg = { 'worked': False, 'msg': 'Unknown SEN ' + str(SEN_id) }
        if self.DEBUG:
            print(DSTRING + "COMPLETE, msg=" + str(msg))
        return msg
    
    # --- messaging ----------------------------------------------------------

    def send_message(self, msg):
        """ Send a message via out_queue """
        self.msgq.put(msg, timeout=self.QTIMEOUT)
        if self.DEBUG:
            print("DEBUG", self.name, "send_message() -->", msg)
        return True

    def recv_message(self):
        """ Receive a message via in_queue """
        msg = {}
        if not self.msgq.empty():
            msg = self.msgq.get(timeout=self.QTIMEOUT)
            if self.DEBUG:
                print("DEBUG", self.name, "recv_message() -->", msg)
        return msg
    
    def proc_message(self, msg):
        """ Process a message """
        if self.DEBUG:
            print("DEBUG", self.name, "proc_message()", msg)
        #TODO what to process?
        return True
    
    # --- data operations ----------------------------------------------------

    def get_id(self):
        """ Get object id """
        return self.id
    
    def get_data(self, key=None):
        """ Retrieve bulk data """
        if None == key:
            return self.data
        elif key in self.data:
            return self.data[key]
        else:
            return {}
    
    def set_data(self, key, value):
        """ Set data parameters """
        if not key in [ 'name', 'uuid', 'address', 'description' ]:
            self.data[key] = value
            if self.DEBUG:
                print("DEBUG", self.name, "set_data() -->", self.data)
            return True
        else:
            return False
    
    def get_role(self):
        """ Retrieve device role """
        return self.role
    
    def get_comms(self):
        """ Retrieve communication modes """
        return self.comms
        
if __name__ == "__main__":
    print("This file is intended as a module, and can't be run stand-alone.")