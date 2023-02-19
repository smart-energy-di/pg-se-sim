# Smart Energy Node (SEN)
In the SmartEnergy project's context, the Smart Energy Node ('SEN')  
is the server component reading, processing and forwarding the data.  
It is able to communicate with the following types of services:  
1. Smart Energy Devices
2. Smart Energy Nodes
Thus, it is possible and intended to form distributed  
hierarchies of devices and nodes.  
SENs must possess **ID** and **address**, and form  
the backbone of Smart Energy linking and data sharing.  
# Smart Energy Device (SED)
In the energy context, a Smart Energy Device (SED) can play  
the following roles:  
* consumer (***using*** electric energy)
* producer (***producing*** electric energy)
* prosumer (both ***using and producing*** energy)

In addition, SEDs can have the following capabilities:  
* talk (send data only)
* listen (send data and receive requests)

SEDs must possess **ID** and **address**, they are the terminal devices  
of Smart Energy. A single SED can be connected to a single SEN only,  
because of the possibility of receiving change requests. Different SENs  
could possibly request incompatible or contradictory changes,  
what we must avoid.  
# Smart Energy Node Protocol Format (SENPF)
SENs and SEDs are, once connected, and **ONLY** when connected,  
able to communicate sending and receiving messages. Theses messages  
are composed as dictionaries (aka 'dicts' in Python or 'hashes' in Perl),  
as thus are the perfect match for 'objects' in JSON aka ECMA. This is to  
provide for **IDIC** = Infinite Diversity in Infinite Combinations.  
Like in real life, we usually don't know the language capabilities  
of strangers we meet. Do they speak our language at all? What are  
their capabilities? And, if security is a concern, how to ensure  
we're talking to the right person, and keep this communication  
secure?  
## SENPF example: SEN connecting a SED
Minimum requirements for a SED-connect are:  
* SED address
* SED initial key

Essential returns are:  
* SED id
* new SED key
* SED message queue ('msgq') for communications

A protocol example:

    SEN --> SED:  
    connect_device(sed_address, sed_key)  
    
    SED --> SEN **SUCCESS:**  
    {  
        'worked': True,  
        'msg': {  
            'id': 'XXYY0123',  
            'key': '678876615hk.8917',  
            'msgq': <some_queue_id>  
        }  
    }  
    
    SED --> SEN **FAILURE**  
    {  
        'worked': False,  
        'msg': {  
            'err': 'wrong initial key'  
        }  
    }  
