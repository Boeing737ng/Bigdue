import struct
from Layer import l3_Layer

class l4_Layer(l3_Layer.l3_Layer):
    l4_header = []
    l4_payload = []

    def __init__(self, packet):
        super().__init__(packet)
        self.l4_header = struct.unpack('! H H', self.l3_payload[:4])
        self.l4_payload = self.l3_payload[4:]

    def get_src_port(self):
        if not(self.check_type()):
            return None
        if not(self.check_protocol()):
            return None
        return self.l4_header[0]

    def get_dst_port(self):
        if not(self.check_type()):
            return None
        if not(self.check_protocol()):
            return None
        return self.l4_header[1]