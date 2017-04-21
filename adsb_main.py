"""
Author: C.A.Valliappan
Description: main function for ADS-B decoding
"""

import numpy as np
import base_util as bu
ADSB_message_type=""

def message_type(type_code):
    """ ADS-B message types"""

    if((type_code>=1)and(type_code<=4)):
        print "Type_code: %d Aircraft identification" %(type_code)
        message_type="Aircraft identification"
    if((type_code>=5)and(type_code<=8)):
        print "Type_code: %d Surface position" %(type_code)
        message_type="Surface position"
    if((type_code>=9)and(type_code<=18)):
        print "Type_code: %d Airborne position (w/ Baro Altitude)" %(type_code)
        message_type="Airborne position (w/ Baro Altitude)"
    if(type_code==19):
        print "Type_code: %d Airbone Velocity" %(type_code)
        message_type="Airborne Velocity"
    if((type_code>=20)and(type_code<=22)):
        print "Type_code: %d Airborne position (w/ GNSS Height)" %(type_code)
        message_type="Airborne position (w/ GNSS Height)"
    if((type_code>=23)and(type_code<=31)):
        print "Type_code: %d Reserved for other uses" %(type_code)
        message_type="Reserved for other uses"

def aircraft_identification(data):
    """ Retuns the Aircaft ID """
    Emitter_category=0
    character='#ABCDEFGHIJKLMNOPQRSTUVWXYZ#####_###############0123456789######'
    if len(data)!=56:
        raise RuntimeError("Not enough Data from the message %d" %len(data))
    if(bu.bin2int(data[0:5])!=4):
        raise RuntimeError("Wrong type_code %d" %bu.bin2int(data[0:5]))
    Emitter_category=bu.bin2int(data[5:8])
    Aircaft_ID=''
    Aircaft_ID+=character[bu.bin2int(data[8:14])]
    Aircaft_ID+=character[bu.bin2int(data[14:20])]
    Aircaft_ID+=character[bu.bin2int(data[20:26])]
    Aircaft_ID+=character[bu.bin2int(data[26:32])]
    Aircaft_ID+=character[bu.bin2int(data[32:38])]
    Aircaft_ID+=character[bu.bin2int(data[38:44])]
    Aircaft_ID+=character[bu.bin2int(data[44:50])]
    Aircaft_ID+=character[bu.bin2int(data[50:56])]
    print Aircaft_ID

    
