import struct
import ipaddress
from Layer import l2_Layer

class l3_Layer(l2_Layer.l2_Layer):
    l3_header = []
    l3_payload = []

    def __init__(self, packet):
        super().__init__(packet)
        if not self.check_type():
            pass

        self.l3_header = struct.unpack('! B B H H H B B H 4s 4s', self.l2_payload[:20])
        l3_headersize = self.get_l3_headersize()
        self.l3_payload = self.l2_payload[l3_headersize:]

    def get_l3_headersize(self):
        l3_headersize = self.l3_header[0]
        l3_headersize = l3_headersize & 0b00001111
        l3_headersize = l3_headersize * 4
        return l3_headersize

    def get_protocol(self):
        return self.l3_header[6]

    def get_src_ipaddress(self):
        src_ipaddress = self.l3_header[8]
        return str(ipaddress.IPv4Address(src_ipaddress))

    def get_dst_ipaddress(self):
        src_ipaddress = self.l3_header[9]
        return str(ipaddress.IPv4Address(src_ipaddress))

    def check_protocol(self):
        protocol_list = {
            0x06 : True,
            0x11 : True
        }
        return protocol_list.get(self.get_protocol(), False)