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
    # def check_for_syn(self):
    def __init__(self):
        self.tcp_flow_list = {}
        self.udp_flow_list = {}

    def add_tcp_flow(self, tcp_flow_key, tcp_flow_value):
        self.tcp_flow_list[tcp_flow_key] = tcp_flow_value

    def add_udp_flow(self, udp_flow_key, udp_flow_value):
        self.udp_flow_list[udp_flow_key] = udp_flow_value

