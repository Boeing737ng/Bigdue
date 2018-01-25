from Layer import l4_Layer

class ManipulatePackets:
    def __init__(self, timestamp, packet_data):
        self.receive = l4_Layer.l4_Layer(packet_data)
        self.timestamp = timestamp
        self.src_ipaddress = receive.get_src_ipaddress()
        self.src_port = receive.get_src_port()
        self.dst_ipaddress = receive.get_dst_ipaddress()
        self.dst_port = receive.get_dst_port()
        self.packet_num = 1
        self.data_length = receive.get_byte_length()

    def get_src_dst_key(self):
        packet_entry_key = str(self.src_ipaddress)+":"
                            +str(self.src_port)+":"
                            +str(self.dst_ipaddress)+":"
                            +str(self.dst_port)
        return packet_entry_key

    def get_dst_src_key(self):
        packet_entry_key = str(self.dst_ipaddress)+":"
                            +str(self.dst_port)+":"
                            +str(self.src_ipaddress)+":"
                            +str(self.src_port)
        return packet_entry_key

    # def compare_key(self, other_packet):
    #     if self.get_src_dst_key 
