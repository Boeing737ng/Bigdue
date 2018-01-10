#!/usr/bin/env python3

import sys
import socket
import time
import struct
import ipaddress
import csv
from collections import deque
import pcap

CONST_MAX_LEN = 1000

def main(argv):
    """
    capturing packet on any interfaces.
    """

    paket_deque = deque(maxlen=CONST_MAX_LEN)

    if sys.platform == 'linux':
        read_socket = socket.socket(
                          family = socket.AF_PACKET,
                          type = socket.SOCK_RAW)
        read_socket.bind(('wlp4s0', 0x0003))

    elif sys.platform == 'win32':
        # TODO(LuHa): create socket and bind it!
        niffer = pcap.pcap(name=None, promisc=True, immediate=True, timeout_ms=50)
        for ts, pkt in sniffer:
            handled_data = handle_data(pkt)
            if not(None in handled_data):
                paket_deque.append(handled_data)
                print(handled_data)

            if len(paket_deque) == CONST_MAX_LEN:
                print(paket_deque)
                # make_csv_file("save_"+str(i)+".csv", paket_deque)
                paket_deque.clear()

    elif sys.platform == 'darwin':
        # TODO : create socket and bind it!
        sniffer = pcap.pcap(name=None, promisc=True, immediate=True, timeout_ms=50)
        for ts, pkt in sniffer:
            handled_data = handle_data(pkt)
            if not(None in handled_data):
                paket_deque.append(handled_data)
                print(handled_data)

            if len(paket_deque) == CONST_MAX_LEN:
                print(paket_deque)
                # make_csv_file("save_"+str(i)+".csv", paket_deque)
                paket_deque.clear()

    try:
        i = 0
        while True:
            read_data = read_socket.recv(1500)
            handled_data = handle_data(read_data)

            if not(None in handled_data):
                paket_deque.append(handled_data)
                print(handled_data)

            if len(paket_deque) == CONST_MAX_LEN:
                i = i+1
                print(paket_deque)
                make_csv_file("save_"+str(i)+".csv", paket_deque)
                paket_deque.clear()
            print(handle_data(read_data))
            # break
    except socket.timeout:
        print('I will out')
        return

def handle_data(data):
    """
    """
    current_time = get_time()
    src_ipaddress = get_src_ipaddress(data)
    dst_ipaddress = get_dst_ipaddress(data)
    src_port = get_src_port(data)
    dst_port = get_dst_port(data)

    return [current_time, src_ipaddress, src_port, dst_ipaddress, dst_port]



def get_time():
    """
    return current time
    we use unixtime(epochtime)
    """
    current_time = int(time.time())

    return current_time



def get_src_ipaddress(data):
    """
    return src ip address

    return string
    """
    cursor = data
    # TODO(LuHa): get src ip address!
    if sys.platform != 'win32':
        l2_type = struct.unpack('!6s6sH', cursor[0:14])[2]
        if l2_type != 0x0800:
            return None
        cursor = cursor[14:]
    l3_headersize = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[0]
    l3_headersize = l3_headersize & 0b00001111
    l3_headersize = l3_headersize * 4
    l3_protocol = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[6]
    l3_srcaddress = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[8]
    # print(ipaddress.IPv4Address(l3_srcaddress))
    l3_dstaddress = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[9]

    return str(ipaddress.IPv4Address(l3_srcaddress))

def get_dst_ipaddress(data):
    """
    return dst ip address

    return string
    """
    cursor = data
    # TODO(LuHa): get dst ip address!
    if sys.platform != 'win32':
        l2_type = struct.unpack('!6s6sH', cursor[0:14])[2]
        if l2_type != 0x0800:
            return None
        cursor = cursor[14:]
    
    l3_headersize = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[0]
    l3_headersize = l3_headersize & 0b00001111
    l3_headersize = l3_headersize * 4
    l3_protocol = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[6]
    l3_srcaddress = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[8]
    l3_dstaddress = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[9]

    return str(ipaddress.IPv4Address(l3_dstaddress))



def get_src_port(data):
    """
    return src port number

    return string
    """
    cursor = data
    # TODO(LuHa): get src port!
    if sys.platform != 'win32':
        l2_type = struct.unpack('!6s6sH', cursor[0:14])[2]
        if l2_type != 0x0800:
            return None
        cursor = cursor[14:]
    l3_headersize = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[0]
    l3_headersize = l3_headersize & 0b00001111
    l3_headersize = l3_headersize * 4
    l3_protocol = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[6]
    if (l3_protocol != 0x06) and (l3_protocol !=0x11):
        return None
    cursor = cursor[l3_headersize:]
    l4_srcport = struct.unpack('!HH', cursor[0:4])[0]
    l4_dstport = struct.unpack('!HH', cursor[0:4])[1]

    return l4_srcport



def get_dst_port(data):
    """
    return dst port number

    return string
    """
    cursor = data
    # TODO(LuHa): get dst port!
    if sys.platform != 'win32':
        l2_type = struct.unpack('!6s6sH', cursor[0:14])[2]
        if l2_type != 0x0800:
            return None
        cursor = cursor[14:]
    
    l3_headersize = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[0]
    l3_headersize = l3_headersize & 0b00001111
    l3_headersize = l3_headersize * 4
    l3_protocol = struct.unpack('!BBHHHBBH4s4s', cursor[0:20])[6]
    if (l3_protocol != 0x06) and (l3_protocol !=0x11):
        return None
    cursor = cursor[l3_headersize:]
    l4_srcport = struct.unpack('!HH', cursor[0:4])[0]
    l4_dstport = struct.unpack('!HH', cursor[0:4])[1]

    return l4_dstport

def make_csv_file(file_name, data):
    if file_name.find('.csv') == -1:
        file_name = file_name+".csv"

    csv_file = open(file_name, 'w', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['timestamp', 'src_ipaddress', 'src_port', 'dst_ipaddress', 'dst_port'])
    for row in data:
        writer.writerow(row)
    csv_file.close()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
