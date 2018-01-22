#!/usr/bin/env python3
import pcap
from Layer import l4_Layer
class read_packet:
    nic_name = ""

    def __init__(self):
        nic_devs = pcap.findalldevs()

        if len(nic_devs) < 1:
            print("no network card")
            return

        print("My Network Card Names : ", nic_devs)
        self.set_nic_name(nic_devs[0])
        #nic_name = input('Input the Network Card Names : ')

        

    def set_nic_name(self, nic_name):
        self.nic_name = nic_name

    def get_whole_packet(self):
        return pcap.pcap(name=self.nic_name, promisc=False, timeout_ms=1000)

    def get_nic_name(self):
        return self.nic_name

    def retrieve_data(self, timestamp, packet_data):
        receive = l4_Layer.l4_Layer(packet_data)
        src_ipaddress = receive.get_src_ipaddress()
        dst_ipaddress = receive.get_dst_ipaddress()
        src_port = receive.get_src_port()
        dst_port = receive.get_dst_port()

        return [timestamp, src_ipaddress, src_port, dst_ipaddress, dst_port]