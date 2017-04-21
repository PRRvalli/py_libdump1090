"""
Author: C.A.Valliappan
Description:Main utility function for ADSB and MODE-S
"""

import numpy as np
import scipy as sp
import math

def hex2bin(hexstr):
    """Convert a hexdecimal string to binary string, with zero fillings. """
    num=hex2int(hexstr)
    x=[]
    n=len(hexstr)*4
    n1=len(np.base_repr(num, base=2))
    if(n>n1):
       x=np.base_repr(num, base=2,padding=n-n1)
    else:
       x=np.base_repr(num, base=2)
    return x

def bin2int(binstr):
    """Convert a binary string to integer. """
    return int(binstr, 2)


def hex2int(hexstr):
    """Convert a hexdecimal string to integer. """
    return int(hexstr, 16)

def downlink_format(msg):
    """Returns the downlink message from message bits 1 to 5  of the message """
    msg_binary=hex2bin(msg)
    #print 'string %s' %(msg_binary[0:5])
    return bin2int(msg_binary[0:5])

def capability(msg):
    """Returns the Capability (additional identifier) from message bits 6 to 8  of the message """
    msg_binary=hex2bin(msg)
    #print 'string %s' %(msg_binary[5:8])
    return bin2int(msg_binary[5:8])

def ICAO_address(msg):
    """Returns the ICAO_address from message bits 9 to 32  of the message """
    #print 'string %s' %(msg[2:8])
    return msg[2:8]

def Data(msg):
    """Returns the Data from message (only if the message has 112 bits as 56 bit message doesn't have data)"""
    if(len(msg)==28):
        #print 'string %s' %(msg[8:22])
        return msg[8:22]
    else:
        return "NULL"

def type_code(msg):
    """Returns the Type_code from message bits 33 to 37  of the message """
    msg_binary=hex2bin(msg)
    #print 'string %s' %(msg_binary[32:37])
    return bin2int(msg_binary[32:37])

def parity_id(msg):
    """Returns the Parity/Interrogator ID  from message bits 89 to 112  of the message """
    # print 'string %s' %(msg[22:28])
    return msg[22:28]
