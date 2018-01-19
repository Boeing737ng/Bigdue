#!/usr/bin/env python3

import sys
import socket
import time
import struct
import ipaddress
import csv
from collections import deque
import pcap

# class 나누기
class export_csv_file:
    def __init__(self, file_name, data):  
        if file_name[-4:] != '.csv':
            file_name = file_name+".csv"

        csv_file = open(file_name, 'w', newline='')
        writer = csv.writer(csv_file)
        writer.writerow(['timestamp', 'src_ipaddress', 'src_port', 'dst_ipaddress', 'dst_port'])
        for row in data:
            writer.writerow(row)
        csv_file.close()

test_list = [['1', '2', '3', '4' ,'5']]
x = export_csv_file("save_1.csv", test_list)