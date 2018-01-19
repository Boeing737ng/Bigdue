#!/usr/bin/env python3
import pcap

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
        read_whole_packet = pcap.pcap(name=self.nic_name, promisc=False, timeout_ms=1000)
        return read_whole_packet

    def get_nic_name(self):
        return self.nic_name