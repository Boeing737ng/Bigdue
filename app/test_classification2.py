#!/usr/bin/env python3

import sys
import socket
import time
import struct
import ipaddress
import csv
from collections import deque
import pcap

CONST_MAX_LEN = 10

# class 나누기
class Test_read_packet:
    def __init__(self, CONST_MAX_LEN):
        packet_deque = deque(maxlen=CONST_MAX_LEN)
        nic_devs = pcap.findalldevs()

        if len(nic_devs) < 1:
            print("no network card")
            return

        print("My Network Card Names : ", nic_devs)

        #nic_name = input('Input the Network Card Names : ')

        self.nic_name = nic_devs[0]

    def get_whole_packet(self):
        read_whole_packet = pcap.pcap(name=self.nic_name, promisc=True, immediate=True, timeout_ms=50)
        return read_whole_packet

    # def retrieve_data(self, data, ts):
        # current_time = ts   
        # src_ipaddress = get_src_ipaddress(data)
        # dst_ipaddress = get_dst_ipaddress(data)
        # src_port = get_src_port(data)
        # dst_port = get_dst_port(data)

        # return [current_time, src_ipaddress, src_port, dst_ipaddress, dst_port]

def main(argv):
    test = Test_read_packet(CONST_MAX_LEN)
    print(test.get_whole_packet())
    return

if __name__ == '__main__':
    sys.exit(main(sys.argv))