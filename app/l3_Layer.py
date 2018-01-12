import struct
import ipaddress
import l4_Layer

class l3_Layer:
    l3_header = []
    l3_payload = []

    def __init__(self, l2_payload):
        # TODO : 생성자 코드작성
        self.l3_header = struct.unpack('! B B H H H B B H 4s 4s', l2_payload[:20])
        self.l3_payload = l2_payload[20:]
    
    def get_l4_Layer(self):
        return l4_Layer.l4_Layer(self.l3_payload)

    def get_src_ipaddress(self):
        src_ipaddress = self.l3_header[8]
        return str(ipaddress.IPv4Address(src_ipaddress))

    def get_dst_ipaddress(self):
        src_ipaddress = self.l3_header[9]
        return str(ipaddress.IPv4Address(src_ipaddress))