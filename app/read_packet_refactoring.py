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

# socket을 통해 packet capture (window용) 
# 추후 pcap 사용시 제거
def connect_socket():
    """
    connect socket and bind
    """
       
    # TODO(LuHa): create socket and bind it!
    # Get host
    host = socket.gethostbyname(socket.gethostname())
    # print('IP: {}'.format(host))
        
    # Create a raw socket and bind it
    read_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW)
    read_socket.bind((host, 0))

    # Include IP headers
    read_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # Enable promiscuous mode
    read_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    return read_socket

def retrieve_data(data):
    current_time = get_time()
    src_ipaddress = get_src_ipaddress(data)
    dst_ipaddress = get_dst_ipaddress(data)
    src_port = get_src_port(data)
    dst_port = get_dst_port(data)

    return [current_time, src_ipaddress, src_port, dst_ipaddress, dst_port]

def get_src_ipaddress(data):
    src_ipaddress=l3_header(data)[8]
    return str(ipaddress.IPv4Address(src_ipaddress))

def get_dst_ipaddress(data):
    dst_ipaddress = l3_header(data)[9]
    return str(ipaddress.IPv4Address(dst_ipaddress))

def get_src_port(data):
    src_port = l4_header(data)[0]
    return src_port

def get_dst_port(data):
    dst_port = l4_header(data)[1]
    return dst_port

def get_time():
    """
    return current time(unixtime:epochtime)
    """
    current_time = int(time.time())
    return current_time

def l2_header(data):
    cursor = data
    return struct.unpack('! 6s 6s H', cursor[:14])

def l3_header(data):
    cursor = data[14:]
    return struct.unpack('! B B H H H B B H 4s 4s', cursor[:20])

def l4_header(data):
    cursor = data[34:] #later change index to ruturn of function
    return struct.unpack('! H H', cursor[:4])

def export_csv_file(file_name, data):
    if file_name.find('.csv') == -1:
        file_name = file_name+".csv"

    csv_file = open(file_name, 'w', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['timestamp', 'src_ipaddress', 'src_port', 'dst_ipaddress', 'dst_port'])
    for row in data:
        writer.writerow(row)
    csv_file.close()
    return

def read_packet():
    packet_deque = deque(maxlen=CONST_MAX_LEN)
    if sys.platform == "win32":
        try:
            csv_counter = 0
            read_whole_packet = connect_socket()
            while True:
                read_whole_packet = read_whole_packet.recv(1500)
                retrieved_data=retrieve_data(read_whole_packet)
                if not (None in retrieved_data):
                    store_packet_in_buffer(packet_deque, retrieved_data)
                if len(packet_deque) == CONST_MAX_LEN:
                    csv_counter = csv_counter + 1
                    export_csv_file("save_" + str(csv_counter) + ".csv", packet_deque)
                    flush_packets_in_buffer(packet_deque)
                # print(retrieve_data(read_whole_packet))
                # break

        except socket.timeout:
            print('!Message: Socket time-out')
            return
    else:
        read_whole_packet = pcap.pcap(name=None, promisc=True, immediate=True, timeout_ms=50)
        for ts, pkt in read_whole_packet:
            retrieved_data = retrieve_data(pkt)
            if not(None in retrieved_data):
                packet_deque.append(retrieved_data)
                print(retrieved_data)

            if len(packet_deque) == CONST_MAX_LEN:
                print(packet_deque)
                # make_csv_file("save_"+str(i)+".csv", packet_deque)
                packet_deque.clear()

def store_packet_in_buffer(packet_deque, retrieved_data):
    packet_deque.append(retrieved_data)
    # print(packet_deque)

def flush_packets_in_buffer(packet_deque):
    packet_deque.clear()

def main(argv):
    read_packet()
    return

if __name__ == '__main__':
    sys.exit(main(sys.argv))


