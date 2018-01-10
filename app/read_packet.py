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
                          family = socket.AF_INET,
                          type = socket.SOCK_RAW)
        read_socket.bind(('wlp4s0', 0x0003))

        read_socket.settimeout(10)
    elif sys.platform == 'win32':
        # TODO(LuHa): create socket and bind it!
        # Get host
        host = socket.gethostbyname(socket.gethostname())
        print('IP: {}'.format(host))

        # Create a raw socket and bind it
        read_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        read_socket.bind((host, 0))

        # Include IP headers
        read_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        # Enable promiscuous mode
        read_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        pass

    try:
        while True:
            read_data = read_socket.recv(1580)
            # print(read_data.hex())
            print(handle_data(read_data))
            # break
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
    cursor = data
    # TODO(LuHa): get src port!
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



if __name__ == '__main__':
    sys.exit(main(sys.argv))
