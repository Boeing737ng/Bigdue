import sys
import ReadPacket
import export_csv_file
import ManipulatePackets

CONST_MAX_LEN = 100

def main():
    packet = ReadPacket.ReadPacket()
    manipulated_packet = ManipulatePackets.ManipulatePackets()
    read_whole_packet = packet.get_whole_packet()
    csv_file = export_csv_file.export_csv_file()
    i = 0
    for timestamp, read_data in read_whole_packet:
        retrieved_data = manipulated_packet.wireshark(timestamp, read_data)
        # retrieved_data = manipulated_packet.retrieve_data(timestamp, read_data)
        # print("No. "+str(i)+str(retrieved_data))
        if not(None in retrieved_data):
            i = i+1
            print("No. "+str(i)+" "+str(retrieved_data))
            csv_file.feed(retrieved_data)
        # else:
            # print("dst port or src port is None")
            
        if(csv_file.get_data_length() >= CONST_MAX_LEN):
            print("!!!!!!!write!!!!!!")
            csv_file.write_csv_file()
            print("!!!!!!!write end!!!!!!!")
            i = 0
    return

if __name__ == '__main__':
    sys.exit(main())