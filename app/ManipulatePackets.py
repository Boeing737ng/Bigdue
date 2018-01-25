from Layer import l4_Layer


class ManipulatePackets:
    receive = ""

    def __init__(self):
        return

    def retrieve_data(self, timestamp, packet_data):
        receive = l4_Layer.l4_Layer(packet_data)
        self.src_ipaddress = receive.get_src_ipaddress()
        self.dst_ipaddress = receive.get_dst_ipaddress()
        self.src_port = receive.get_src_port()
        self.dst_port = receive.get_dst_port()
        self.packet_len = receive.get_byte_length()
        self.packet_protocol = receive.check_protocol()
        # receive.get_control_flag()

        return [str(timestamp).split(".")[0], src_ipaddress, src_port,
                dst_ipaddress, dst_port]

    def wireshark(self, timestamp, packet_data):
        receive = l4_Layer.l4_Layer(packet_data)
        src_ipaddress = receive.get_src_ipaddress()
        dst_ipaddress = receive.get_dst_ipaddress()
        src_port = receive.get_src_port()
        dst_port = receive.get_dst_port()
        packet_type = receive.check_type()
        packet_protocol = receive.check_protocol()

        return [str(timestamp).split(".")[0], src_ipaddress, src_port,
                dst_ipaddress, dst_port, packet_type, packet_protocol,
                len(packet_data)]
                
    def get_src_dst_key(self):
        packet_entry_key = str(self.src_ipaddress) + ":" \
                           + str(self.src_port) + " "\
                           + str(self.dst_ipaddress) + ":"\
                           + str(self.dst_port)
        return packet_entry_key

    def get_dst_src_key(self):
        packet_entry_key = str(self.dst_ipaddress) + ":" \
                           + str(self.dst_port) + " " \
                           + str(self.src_ipaddress) + ":" \
                           + str(self.src_port)
        return packet_entry_key

    def compare_key(self, key):
        if self.get_src_dst_key == key:
            return True
        if self.get_dst_src_key == key:
            return True
        return False

    # def create_key(self, packet_data):
    #     receive = l4_Layer.l4_Layer(packet_data)
    #     packet_entry_key = str(receive.get_src_ipaddress()) \
    #                        + str(receive.get_src_port()) \
    #                        + str(receive.get_dst_ipaddress()) \
    #                        + str(receive.get_dst_port())
    #     return packet_entry_key
