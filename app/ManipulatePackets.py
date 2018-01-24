class ManipulatePackets:
from Layer import l4_Layer

    def __init__(self):
        receive = l4_Layer.l4_Layer(packet_data)
        return


    def retrieve_data(self, timestamp, packet_data):
        src_ipaddress = receive.get_src_ipaddress()
        dst_ipaddress = receive.get_dst_ipaddress()
        src_port = receive.get_src_port()
        dst_port = receive.get_dst_port()
        # receive.get_control_flag()

        return [str(timestamp).split(".")[0], src_ipaddress, src_port,
                dst_ipaddress, dst_port]

    def wireshark(self, timestamp, packet_data):
        src_ipaddress = receive.get_src_ipaddress()
        dst_ipaddress = receive.get_dst_ipaddress()
        src_port = receive.get_src_port()
        dst_port = receive.get_dst_port()
        packet_type = receive.check_type()
        packet_protocol = receive.check_protocol()

        return [str(timestamp).split(".")[0], src_ipaddress, src_port,
                dst_ipaddress, dst_port, packet_type, packet_protocol,
                len(packet_data)]
