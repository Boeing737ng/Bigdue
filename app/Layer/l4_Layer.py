import struct
from Layer import l3_Layer

class l4_Layer(l3_Layer.l3_Layer):
    l4_header = []
    l4_payload = []

    def __init__(self, packet):
        super().__init__(packet)
        if self.l3_payload:
            if self.check_protocol():
                self.l4_header = struct.unpack('! H H 4s 4s H H H H', self.l3_payload[:20])
                self.l4_payload = self.l3_payload[4:]

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
        print("header->"+str(self.l4_header[4]))
        raw_control_flag = self.l4_header[4] & 0x1FF
        control_flag = self.calculate_control_flag(raw_control_flag)
        print("control flag->"+str(control_flag))
        return None

    def calculate_control_flag(self, raw_control_flag):
        control_flag = []
        control_flag_list = {
            1: "FIN",
            2: "SYN",
            4: "RST",
            8: "PSH",
            16: "ACK",
            32: "URG",
            64: "ECN",
            128: "CWR",
            256: "NON"
        }
        check_flag = 0x1
        while check_flag < 257:
            if control_flag_list.get(raw_control_flag & check_flag, False):
                control_flag.append(control_flag_list.get(raw_control_flag & check_flag, False))
                print(raw_control_flag)
            check_flag = check_flag << 0x1
        return control_flag