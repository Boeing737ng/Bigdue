from Layer import l4_Layer

class ManipulatePackets:
    receive = ""
    def __init__(self):
        return

    def retrieve_data(self, timestamp, packet_data):
        receive = l4_Layer.l4_Layer(packet_data)
        src_ipaddress = receive.get_src_ipaddress()
        dst_ipaddress = receive.get_dst_ipaddress()
        src_port = receive.get_src_port()
        dst_port = receive.get_dst_port()
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

    def create_key(self, packet_data):
        receive = l4_Layer.l4_Layer(packet_data)
        packet_entry_key = str(receive.get_src_ipaddress())+str(receive.get_src_port())+str(receive.get_dst_ipaddress())+str(receive.get_dst_port())
        return packet_entry_key
