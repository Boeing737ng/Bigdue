import struct
import l3_Layer

class l2_Layer:
    l2_header = []
    l2_payload = []
    def __init__(self, packet_data):
        self.l2_header = struct.unpack('! 6s 6s H', packet_data[:14])
        self.l2_payload = packet_data[14:]

    def get_l2_header(self):
        return self.l2_header

    def get_l2_payload(self):
        return self.l2_payload

    def get_l3_Layer(self):
        return l3_Layer.l3_Layer(self.l2_payload)

    def get_l4_Layer(self):
        return self.get_l3_Layer().get_l4_Layer()

    def get_header(self):
        return self.l2_header
    
    def get_src_mac_addr(self):
        return self.l2_header[0]

    def get_dst_mac_addr(self):
        return self.l2_header[1]

    def get_type(self):
        return self.l2_header[2]
