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

    def add_packet(self, retrieved_data):
        protocol = retrieved_data["protocol"]
        if protocol == "TCP":
            self.add_tcp_flow(retrieved_data)
        elif protocol == "UDP":
            self.add_udp_flow(retrieved_data)

    def add_tcp_flow(self, retrieved_data):
        key_set = retrieved_data["key"]
        tcp_key_set = self.tcp_flow_list.keys()

        if key_set[0] in tcp_key_set:
            # print("key found")
            self.merge_tcp_flow_value(retrieved_data, key_set[0])
        elif key_set[1] in tcp_key_set:
            # print("reversed key found")
            self.merge_tcp_flow_value(retrieved_data, key_set[1])
        else:
            # print("key not found")
             self.tcp_flow_list[key_set[0]] = self.make_flow_value(
                 retrieved_data)

        print(self.tcp_flow_list)

    def add_udp_flow(self, retrieved_data):
        key_set = retrieved_data["key"]
        udp_key_set = self.udp_flow_list.keys()

        if key_set[0] in udp_key_set:
            self.merge_udp_flow_value(retrieved_data, key_set[0])
        elif key_set[1] in udp_key_set:
            self.merge_udp_flow_value(retrieved_data, key_set[1])
        else:
            self.udp_flow_list[key_set[0]] = self.make_flow_value(retrieved_data)
        
        print(self.udp_flow_list)

    def make_flow_value(self, retrieved_data):
        # start timestamp
        # end timestamp
        # src ip
        # src port
        # dst ip
        # dst port
        # No packets
        # length of data(bytes)
        flow_value = {}
        flow_value["s_time"] = retrieved_data["timestamp"]
        flow_value["e_time"] = retrieved_data["timestamp"]
        flow_value["src_ipaddress"] = retrieved_data["src_ipaddress"]
        flow_value["src_port"] = retrieved_data["src_port"]
        flow_value["dst_ipaddress"] = retrieved_data["dst_ipaddress"]
        flow_value["dst_port"] = retrieved_data["dst_port"]
        flow_value["no_packets"] = 1
        flow_value["bytes"] = retrieved_data["bytes"]

        return flow_value
    
    def merge_udp_flow_value(self, retrieved_data, key_set):
        udp_flow = self.udp_flow_list[key_set]
        udp_flow["e_time"] = retrieved_data["timestamp"]
        udp_flow["no_packets"] = udp_flow["no_packets"]+1
        udp_flow["bytes"] = udp_flow["bytes"] + retrieved_data["bytes"]
        self.udp_flow_list[key_set] = udp_flow

    def merge_tcp_flow_value(self, retrieved_data, key_set):
        tcp_flow = self.tcp_flow_list[key_set]
        tcp_flow["e_time"] = retrieved_data["timestamp"]
        tcp_flow["no_packets"] = tcp_flow ["no_packets"]+1
        tcp_flow["bytes"] = tcp_flow ["bytes"] + retrieved_data["bytes"]
        self.tcp_flow_list[key_set] = tcp_flow



