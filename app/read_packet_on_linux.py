#!/usr/bin/env python3



import sys
import socket
import time



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

    except Exception as exp:
        print('i will out')
        print(exp)



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
    current_time = (time.time()).split('.')[0]

    return current_time



def get_src_ipaddress(data):
    """
    return src ip address

    return string
    """
    return ''



def get_dst_ipaddress(data):
    """
    return dst ip address

    return string
    """
    return ''



def get_src_port(data):
    """
    return src port number

    return string
    """
    return ''



def get_dst_port(data):
    """
    return dst port number

    return string
    """
    return ''



if __name__ == '__main__':
    sys.exit(main(sys.argv))
