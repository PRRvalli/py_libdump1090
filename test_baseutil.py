"""
Author: C.A.Valliappan
Description: Test for base utility function for ADSB and MODE-S
"""

import numpy as np
import scipy as sp
import base_util as bu
import math


msg='8D4840D6202CC371C32CE0576098'

if(bu.downlink_format(msg)==17):
    print 'Downlink_Format is working fine'
else:
    print 'Error with Downlink_Format '

if(bu.capability(msg)==5):
    print 'Capabilty indicator is working fine'
else:
    print 'Error with Capabilty indicator'

if(bu.ICAO_address(msg)=='4840D6'):
    print 'ICAO_address is working fine'
else:
    print 'Error with ICAO_address'

if(bu.Data(msg)=='202CC371C32CE0'):
    print 'Data function is working fine'
else:
    print 'Error with Data function'


if(bu.type_code(msg)==4):
    print 'type_code function is working fine'
else:
    print 'Error with type_code function'


if(bu.parity_id(msg)=='576098'):
    print 'parity_id function is working fine'
else:
    print 'Error with parity_id function'
