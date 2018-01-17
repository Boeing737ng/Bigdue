#!/usr/bin/env python3

import sys
import struct
import unittest

# user defined class or library
from . import packet

def get_packet_from_bytes(data):
    """
    generate packet from byte
    arg:
        bytes data
    return:
        packet
    """
    packet_types = {'l2': None,
                    'l3': None}
    if len(data) < 1:
        raise Exception('The size of data to using create packet below 0')

    cursor = data
    if sys.platform != 'win32':
        l2_type = struct.unpack('!6s6sH', cursor[0:14])[2]
        if l2_type == packet.L2IP:
            packet_types['l2'] = packet.L2IP
        else:
            packet_types['l2'] = packet.L2UNKNOWN

    return packet_types




class PacketGetterTextCase(unittest.TestCase):
    def test_l2unknown(self):
        data = bytes.fromhex(('ffffffffffff' 
                            + 'ffffffffffff' 
                            + '0000'))
        self.assertEqual(get_packet_from_bytes(data)['l2'], 
                         packet.L2UNKNOWN)
        data = bytes.fromhex(('ffffffffffff' 
                            + 'ffffffffffff' 
                            + '0800'))
        self.assertNotEqual(get_packet_from_bytes(data)['l2'], 
                            packet.L2UNKNOWN)
    
    def test_l2ip(self):
        data = bytes.fromhex(('ffffffffffff' 
                            + 'ffffffffffff' 
                            + '0800'))
        self.assertEqual(get_packet_from_bytes(data)['l2'],
                         packet.L2IP)
        data = bytes.fromhex(('ffffffffffff' 
                            + 'ffffffffffff' 
                            + '1234'))
        self.assertNotEqual(get_packet_from_bytes(data)['l2'], 
                            packet.L2IP)
