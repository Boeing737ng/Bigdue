#!/usr/bin/env python3
import pcap

class ReadPacket:
    nic_name = ""

    def __init__(self):
        nic_devs = pcap.findalldevs()

        if len(nic_devs) < 1:
            print("no network card")
            return

        print("My Network Card Names : ", nic_devs)
        self.set_nic_name(nic_devs[0])

        

    def set_nic_name(self, nic_name):
        self.nic_name = nic_name

    def get_whole_packet(self):
        return pcap.pcap(name=self.nic_name, promisc=False, timeout_ms=1000)

    def get_nic_name(self):
        return self.nic_name