"""
start timestamp
end timestamp
src ip
src port
dst ip
dst port
No packets
length of data(bytes)
"""

class tcpFlow:
    tcp_flow_list = {}
    # def check_for_syn(self):
    def __init__(self):
        self.start = 0
        self.end = 0
        self.src_ip = ""
        self.src_port = 0
        self.dst_ip = ""
        self.dst_port = 0
        self.packet_num = 0
        self.data_length = 0

    def add_tcp_flow(self, tcp_flow_key, tcp_flow_value):
        tcp_flow_key[tcp_flow_key] = tcp_flow_value

