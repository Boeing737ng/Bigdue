import sys
import ReadPacket
import export_csv_file
import TcpFlow
import ManipulatePackets

CONST_MAX_LEN = 100000

def main(argv):
    packet = ReadPacket.ReadPacket()
    manipulated_packet = ManipulatePackets.ManipulatePackets()
    tcpFlow = TcpFlow.tcpFlow()
    read_whole_packet = packet.get_whole_packet()
    csv_file = export_csv_file.export_csv_file()
    i = 0
    for timestamp, read_data in read_whole_packet:
        # retrieved_data = packet.retrieve_data(timestamp, read_data)
        retrieved_data = manipulated_packet.retrieve_data(timestamp, read_data)
        i = i+1
        # print("No. "+str(i)+str(retrieved_data))
        if not(None in retrieved_data.values()):
            tcpFlow.add_packet(retrieved_data)
            # print(manipulated_packet.get_src_dst_key())
            # print(manipulated_packet.get_dst_src_key())
            # print("No. "+str(i)+" "+str(retrieved_data))
            # csv_file.feed(retrieved_data)
        # else:
            # print("dst port or src port is None")
            
        if(csv_file.get_data_length() >= CONST_MAX_LEN):
            print("!!!!!!!write!!!!!!")
            csv_file.write_csv_file()
            i = 0
    return

if __name__ == '__main__':
    sys.exit(main(sys.argv))