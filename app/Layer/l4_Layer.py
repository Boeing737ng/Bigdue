import struct
from Layer import l3_Layer

class l4_Layer(l3_Layer.l3_Layer):
    l4_header = []
    l4_payload = []

    def __init__(self, packet):
        super().__init__(packet)
        if self.l3_payload:
            if self.check_protocol() == "TCP":
                self.l4_header = struct.unpack('! H H 4s 4s H H H H', self.l3_payload[:20])
                self.l4_payload = self.l3_payload[20:]
            elif self.check_protocol() == "UDP":
                self.l4_header = struct.unpack('! H H H H', self.l3_payload[:8])
                self.l4_payload = self.l3_payload[8:]


    def get_src_port(self):
        if not self.l4_header:
            return None
        return self.l4_header[0]

    def get_dst_port(self):
        if not self.l4_header:
            return None
        return self.l4_header[1]

    def get_control_flag(self):
        if not self.l4_header:
            return None
        # print("header->"+str(self.l4_header[4]))
        raw_control_flag = self.l4_header[4] & 0x1FF
        control_flag = self.calculate_control_flag(raw_control_flag)
        return control_flag

    def get_byte_length(self):
        return len(self.l4_payload)
    
    def calculate_control_flag(self, raw_control_flag):
        control_flag = []
        control_flag_list = {
            0x1: "FIN",
            0x2: "SYN",
            0x4: "RST",
            0x8: "PSH",
            0x10: "ACK",
            0x20: "URG",
            0x40: "ECN",
            0x80: "CWR",
            0x100: "NON"
        }
        flag_mask = 0x1
        while flag_mask < 0x101:
            flag = control_flag_list.get(raw_control_flag & flag_mask, False)
            if flag:
                control_flag.append(flag)
            flag_mask = flag_mask << 0x1

        return control_flag