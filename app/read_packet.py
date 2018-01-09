#!/usr/bin/env python3



import sys
import socket
import time
import struct
import ipaddress


def main(argv):
    """
    capturing packet on any interfaces.
    """
    if sys.platform == 'linux':
        read_socket = socket.socket(
                          family = socket.AF_PACKET,
                          type = socket.SOCK_RAW)
        read_socket.bind(('wlp4s0', 0x0003))

        read_socket.settimeout(10)
    elif sys.platform == 'win32':
        # TODO(LuHa): create socket and bind it!
        pass

    try:
        while True:
            read_data = read_socket.recv(1580)
            print(read_data.hex())
            print(handle_data(read_data))
            break
    except socket.timeout:
        print('i will out')
        return


def handle_data(data):
    """
    """
    current_time = get_time()
    src_ipaddress = get_src_ipaddress(data)
    dst_ipaddress = get_dst_ipaddress(data)
    src_port = get_src_port(data)
    dst_port = get_dst_port(data)

    return (current_time, src_ipaddress, src_port, dst_ipaddress, dst_port)



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

    return str(ipaddress.IPv4Address(l3_srcaddress))






def get_dst_ipaddress(data):
    """
    return dst ip address

    return string
    """
    cursor = data
    # TODO(LuHa): get dst ip address!
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
    # TODO(LuHa): get src port!
    return ''



def get_dst_port(data):
    """
    return dst port number

    return string
    """
    # TODO(LuHa): get dst port!
    return ''



if __name__ == '__main__':
    sys.exit(main(sys.argv))
