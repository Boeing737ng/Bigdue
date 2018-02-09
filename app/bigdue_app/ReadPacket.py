#!/usr/bin/env python3
import pcap

class ReadPacket:
    nic_name = ""

    def __init__(self):
        main_nic_dev = self.find_main_nic_dev()
        self.set_nic_name(main_nic_dev)
        

    def set_nic_name(self, nic_name):
        self.nic_name = nic_name

    def get_whole_packet(self):
        return pcap.pcap(name=self.nic_name, promisc=False, timeout_ms=1000)

    def get_nic_name(self):
        return self.nic_name

    def find_all_nic_devs(self):
        return pcap.findalldevs()

    def find_main_nic_dev(self):
        try:
            nic_dev = pcap.lookupdev()
        except:
            nic_devs = self.find_all_nic_devs()
            
            if len(nic_devs) < 1:
                print("no network card")
                return
            
            print("My Network Card List")
            for i in range(len(nic_devs)):
                print(i, ":", nic_devs[i])

            my_dev_index = int(input("Select Your Network Card : \n"))
            nic_dev = nic_devs[my_dev_index]
        
        print("My Network Card Names : ", nic_dev)
        return nic_dev