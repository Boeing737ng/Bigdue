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
    packet_types = {'l2': packet.L2UNKNOWN,
                    'l3': packet.L3UNKNOWN}
    if len(data) < 1:
        raise Exception('The size of data to using create packet below 0')

    cursor = data
    if sys.platform != 'win32':
        l2_type = struct.unpack('!6s6sH', cursor[0:14])[2]
        if l2_type == packet.L2IP:
            packet_types['l2'] = packet.L2IP
        else:
            return packet_types
        cursor = data[14:]

    if len(cursor) < 20:
        return packet_types

    l3_protocol = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[6]
    if l3_protocol == packet.L3TCP:
        packet_types['l3'] = packet.L3TCP
    elif l3_protocol == packet.L3UDP:
        packet_types['l3'] = packet.L3UDP
    else:
        return packet_types

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

    def test_l3unknown(self):
        data = bytes.fromhex(('ffffffffffff' 
                            + 'ffffffffffff' 
                            + '0800'
                            + 'ffffffff'
                            + 'ffffffff'
                            + 'ff00ffff'
                            + 'ffffffff'
                            + 'ffffffff'))
        self.assertEqual(get_packet_from_bytes(data)['l3'],
                         packet.L3UNKNOWN)
        data = bytes.fromhex(('ffffffffffff' 
                            + 'ffffffffffff' 
                            + '0800'
                            + 'ffffffff'
                            + 'ffffffff'
                            + 'ff06ffff'
                            + 'ffffffff'
                            + 'ffffffff'))
        self.assertNotEqual(get_packet_from_bytes(data)['l3'], 
                            packet.L3UNKNOWN)
        data = bytes.fromhex(('ffffffffffff' 
                            + 'ffffffffffff' 
                            + '0800'
                            + 'ffffffff'
                            + 'ffffffff'
                            + 'ff11ffff'
                            + 'ffffffff'
                            + 'ffffffff'))
        self.assertNotEqual(get_packet_from_bytes(data)['l3'], 
                            packet.L3UNKNOWN)
        
    def test_l3tcp(self):
        data = bytes.fromhex(('ffffffffffff' 
                            + 'ffffffffffff' 
                            + '0800'
                            + 'ffffffff'
                            + 'ffffffff'
                            + 'ff06ffff'
                            + 'ffffffff'
                            + 'ffffffff'))
        self.assertEqual(get_packet_from_bytes(data)['l3'],
                         packet.L3TCP)
        data = bytes.fromhex(('ffffffffffff' 
                            + 'ffffffffffff' 
                            + '0800'
                            + 'ffffffff'
                            + 'ffffffff'
                            + 'ff11ffff'
                            + 'ffffffff'
                            + 'ffffffff'))
        self.assertNotEqual(get_packet_from_bytes(data)['l3'], 
                            packet.L3TCP)

    def test_l3udp(self):
        data = bytes.fromhex(('ffffffffffff' 
                            + 'ffffffffffff' 
                            + '0800'
                            + 'ffffffff'
                            + 'ffffffff'
                            + 'ff11ffff'
                            + 'ffffffff'
                            + 'ffffffff'))
        self.assertEqual(get_packet_from_bytes(data)['l3'],
                         packet.L3UDP)
        data = bytes.fromhex(('ffffffffffff' 
                            + 'ffffffffffff' 
                            + '0800'
                            + 'ffffffff'
                            + 'ffffffff'
                            + 'ff06ffff'
                            + 'ffffffff'
                            + 'ffffffff'))
        self.assertNotEqual(get_packet_from_bytes(data)['l3'], 
                            packet.L3UDP)
