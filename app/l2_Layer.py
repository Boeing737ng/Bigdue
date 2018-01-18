import struct
# import l3_Layer

class l2_Layer:
    l2_header = []
    l2_payload = []
    def __init__(self, packet_data):
        self.l2_header = struct.unpack('! 6s 6s H', packet_data[:14])
        self.l2_payload = packet_data[14:]
    
    def get_src_mac_addr(self):
        return self.l2_header[0]

    def get_dst_mac_addr(self):
        return self.l2_header[1]

    def get_type(self):
        return self.l2_header[2]
