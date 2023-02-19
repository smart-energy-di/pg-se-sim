""" SmartEnergyNode class definition
    roles: {}
"""

import json
import uuid
import time
import threading
import queue

class SmartEnergyNode:
    """ Class variables """
    __instance_count = 0

    # --- instance management ------------------------------------------------
    
    def __init__(self, name, address, description=None):
        """ Class update"""
        self.DEBUG = True
        SmartEnergyNode.__instance_count += 1
        if self.DEBUG:
            print("DEBUG SmartEnergyNode() instance nr.", 
                SmartEnergyNode.__instance_count)        
        """ Instance initialization """
        self.QTIMEOUT = 5 # seconds
        self.HBEAT = 0.25 # seconds
        # SEN data
        uid = uuid.uuid4()
        self.id = name + '><' + str(uid)
        self.address = address
        self.description = description
        self.msgq = queue.Queue() # message queue 
        self.SEDstore = {} # connected SME devices
        self.SENstore = {} # connected SME nodes
        self.data = {
            'id': self.id,
            'name': name,
            'address': address,
            'description': description,
            'uuid': uid,
        }
        self.roles = []
        # Start working
        self.run = True
        self.thread = threading.Thread( target=self.heartbeat )
        self.thread.start()
        
    #def __del__(self):
    #    """ Destruction """
    #    pass

    # --- internal operations ------------------------------------------------
        
    def heartbeat(self):
        """ Cyclic worker """
        while self.run:
            for dev_id in self.SEDstore.keys():
                msg = self.recv_device(dev_id)
                if {} != msg:
                    self.proc_device(dev_id, msg)
            for node_id in self.SENstore.keys():
                msg = self.recv_node(node_id)
                if {} != msg:
                    self.proc_node(node_id, msg)
            time.sleep(self.HBEAT)
            
    def halt(self):
        """ Stop and join """
        if self.DEBUG:
            print("DEBUG SMEnode", self.id , "halted.")
        self.run = False
        self.thread.join()
        
    # --- connectivity -------------------------------------------------------
    
    def connect_device(self, SED, initial_key):
        """ Connect an SME device """
        DSTRING = "DEBUG " + self.id + ".connect_device(" + str(SED) + ") "
        if self.DEBUG:
            print(DSTRING + " START")
        msg = SED.connect(self.id, initial_key)
        if msg['worked']:
            if self.DEBUG:
                print(DSTRING + "WORKED")
            ds = { 
                  'id': msg['id'],
                  'status': 'connect',
                  'key': msg['key'],
                  'msgq': msg['msgq'],
                  'address': SED
            }
            if not ds['id'] in self.SEDstore:
                self.SEDstore[ds['id']] = ds
            else:
                #TODO how to handle duplicate IDs?
                print("SEN connect_device ERROR: id already in SEDstore?")
        else:            
            #TODO how to handled failed connect attempts?
            if self.DEBUG:
                print(DSTRING + "FAILED: " + msg['msg'])
    
    def disconnect_device(self, id):
        """ Disconnect an SME device """
        DSTRING = "DEBUG " + self.id + ".disconnect_device(" + id + ") "
        msg = self.SEDstore[id]['address'].disconnect(self.id)
        if msg['worked']:
            self.SEDstore[id]['status'] = 'disconnect'
            if self.DEBUG:
                print(DSTRING, 'SUCCESS')
        else:
            if self.DEBUG:
                print(DSTRING, 'FAILURE: ', msg['msg'])
    
    def decomission_device(self, name):
        """ Decomission a device's data """
        pass
    
    def connect_node(self, name, address):
        """ Connect an SME node """
        pass
    
    def disconnect_node(self, name):
        """ Disconnect an SME node """
        pass
        
    def decomission_node(self, name):
        """ Decomission an SME node's data """
        pass
    
    # --- messaging ----------------------------------------------------------

    def send_device(self, device_id, msg):
        """ Send a message via out_queue """
        DSTRING  = "DEBUG " + self.id + ".send_device("
        DSTRING += device_id + ") --> " + str(msg)
        if self.DEBUG:
            print(DSTRING + "msg=" + str(msg))
        self.SEDstore[device_id]['msgq'].put(msg, timeout=self.QTIMEOUT)
        return True

    def send_node(self, node_id, msg):
        """ Send a message via out_queue """
        DSTRING  = "DEBUG " + self.id + ".send_node("
        DSTRING += node_id + ") "
        self.SENstore[node_id]['msgq'].put(msg, timeout=self.QTIMEOUT)
        if self.DEBUG:
            print(DSTRING + "msg=" + str(msg))
        return True

    def recv_device(self, device_id):
        """ Receive a message via in_queue """
        DSTRING  = "DEBUG " + self.id + ".recv_device("
        DSTRING += device_id + ") "
        msg = {}
        if not self.SEDstore[device_id]['msgq'].empty():
            msg = self.SEDstore[device_id]['msgq'].get(timeout=self.QTIMEOUT)
            if self.DEBUG:
                print(DSTRING + "msg=", str(msg))
        return msg
    
    def recv_node(self, node_id):
        """ Receive a message via in_queue """
        DSTRING  = "DEBUG " + self.id + ".recv_node("
        DSTRING += node_id + ") "
        msg = {}
        if not self.SENstore[node_id]['msgq'].empty():
            msg = self.SENstore[node_id]['msgq'].get(timeout=self.QTIMEOUT)
            if self.DEBUG:
                print(DSTRING + "msg=", str(msg))
        return msg

    def proc_device(self, device_id, msg):
        """ Process a message """
        DSTRING  = "DEBUG " + self.id + ".proc_node("
        DSTRING += device_id + ") "
        msg = {}
        if self.DEBUG:
            print(DSTRING + "msg=", str(msg))
        #TODO what to process?
        return msg

    def proc_node(self, node_id, msg):
        """ Process a message """
        DSTRING  = "DEBUG " + self.id + ".proc_node("
        DSTRING += node_id + ") "
        msg = {}
        if self.DEBUG:
            print(DSTRING + "msg=", str(msg))
        #TODO what to process?
        return msg

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
            return True
        else:
            return False
    
    def get_roles(self):
        """ Retrieve device role """
        return self.roles
        
if __name__ == "__main__":
    print("This file is intended as a module, and can't be run stand-alone.")