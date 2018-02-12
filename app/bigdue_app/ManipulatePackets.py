try:
    from Layer import l4_Layer
except ImportError:
    from app.bigdue_app.Layer import l4_Layer

"""
src_ipaddress
dst_ipaddress
src_port
dst_port
packet_len
packet_protocol
timestamp
key [src_dst_key, dst_src_key]
"""

class ManipulatePackets:
    
    def __init__(self):
        self.packet_data = {}

    def retrieve_data(self, timestamp, packet_data):
        receive = l4_Layer.l4_Layer(packet_data)
        self.packet_data = {}
        self.packet_data["src_ipaddress"] = receive.get_src_ipaddress()
        self.packet_data["dst_ipaddress"] = receive.get_dst_ipaddress()
        self.packet_data["src_port"] = receive.get_src_port()
        self.packet_data["dst_port"] = receive.get_dst_port()
        self.packet_data["bytes"] = receive.get_byte_length()
        self.packet_data["protocol"] = receive.check_protocol()
        # self.packet_data["timestamp"] = str(timestamp).split(".")[0]
        self.packet_data["timestamp"] = timestamp

        if self.packet_data["protocol"] == "TCP":
            self.packet_data["control_flag"] = receive.get_control_flag()
            self.set_key_value()
        elif self.packet_data["protocol"] == "UDP":
            self.set_key_value()
         
        return self.packet_data

    def wireshark(self, timestamp, packet_data):
        receive = l4_Layer.l4_Layer(packet_data)
        src_ipaddress = receive.get_src_ipaddress()
        dst_ipaddress = receive.get_dst_ipaddress()
        src_port = receive.get_src_port()
        dst_port = receive.get_dst_port()
        packet_size = receive.get_byte_length()

        return [str(timestamp).split(".")[0], src_ipaddress, src_port,
                dst_ipaddress, dst_port, packet_size]

    def set_key_value(self):
        self.packet_data["key"] = [self.get_src_dst_key(), self.get_dst_src_key()]

    def get_src_dst_key(self):
        packet_entry_key = self.packet_data["src_ipaddress"] + ":" \
                           + str(self.packet_data["src_port"]) + " "\
                           + self.packet_data["dst_ipaddress"] + ":"\
                           + str(self.packet_data["dst_port"])
        return packet_entry_key

    def get_dst_src_key(self):
        packet_entry_key = self.packet_data["dst_ipaddress"] + ":" \
                           + str(self.packet_data["dst_port"]) + " " \
                           + self.packet_data["src_ipaddress"] + ":" \
                           + str(self.packet_data["src_port"])
        return packet_entry_key        