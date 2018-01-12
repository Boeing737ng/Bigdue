import struct

class l4_Layer:
    l4_header = []
    l4_payload = []

    def __init__(self, l3_payload):
        # TODO : 생성자 코드작성
        self.l4_header = struct.unpack('! H H', l3_payload[:4])
        self.l4_payload = l3_payload[4:]
    
    def get_src_port(self):
        return self.l4_header[0]

    def get_dst_port(self):
        return self.l4_header[1]