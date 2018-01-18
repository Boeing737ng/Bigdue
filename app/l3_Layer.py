import struct
import ipaddress
import l2_Layer

class l3_Layer(l2_Layer.l2_Layer):
    l3_header = []
    l3_payload = []

    def __init__(self, packet):
        # TODO : 생성자 코드작성
        l2_Layer.l2_Layer.__init__(self, packet)
        self.l3_header = struct.unpack('! B B H H H B B H 4s 4s', self.l2_payload[:20])
        self.l3_payload = self.l2_payload[20:]
    
    def get_l3_header(self):
        return self.l3_header

    def get_l3_payload(self):
        return self.l3_payload

    def get_src_ipaddress(self):
        src_ipaddress = self.l3_header[8]
        return str(ipaddress.IPv4Address(src_ipaddress))

    def get_dst_ipaddress(self):
        src_ipaddress = self.l3_header[9]
        return str(ipaddress.IPv4Address(src_ipaddress))