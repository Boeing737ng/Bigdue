import sys
try:
    import ReadPacket
except ImportError:
    from app.bigdue_app import ReadPacket

try:
    import Export_csv_file
except ImportError:
    from app.bigdue_app import Export_csv_file
# import TcpFlow

try:
    import ManipulatePackets
except ImportError:
    from app.bigdue_app import ManipulatePackets

CONST_MAX_LEN = 1000000

def main():
    packet = ReadPacket.ReadPacket()
    manipulated_packet = ManipulatePackets.ManipulatePackets()
    # tcpFlow = TcpFlow.tcpFlow()
    read_whole_packet = packet.get_whole_packet()
    csv_file = Export_csv_file.Export_csv_file()
    i = 0
    for timestamp, read_data in read_whole_packet:
        # retrieved_data = manipulated_packet.wireshark(timestamp, read_data)

        try:
            retrieved_data = manipulated_packet.retrieve_data(timestamp, read_data)
        except KeyboardInterrupt:
            print("asdfasdfasdfasdf")

        # print("No. "+str(i)+str(retrieved_data))
        if not(None in retrieved_data.values()):
            i = i+1
            # tcpFlow.add_packet(retrieved_data)
            # print(manipulated_packet.get_src_dst_key())
            # print(manipulated_packet.get_dst_src_key())
            #print("No. "+str(i)+" "+str(retrieved_data))
            csv_file.feed(retrieved_data)
        # else:
            # print("dst port or src port is None")
            
        if(csv_file.get_data_length() >= CONST_MAX_LEN):
            print("!!!!!!!write!!!!!!")
            csv_file.write_csv_file()
            print("!!!!!!!write end!!!!!!!")
            i = 0
            #return
    return

if __name__ == '__main__':
    sys.exit(main())