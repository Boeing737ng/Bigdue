import sys
import read_packet
import export_csv_file

CONST_MAX_LEN = 1000

def main(argv):
    packet = read_packet.read_packet()
    read_whole_packet = packet.get_whole_packet()
    csv_file = export_csv_file.export_csv_file()
    i = 0
    for timestamp, read_data in read_whole_packet:
        retrieved_data = packet.retrieve_data(timestamp, read_data)
        i = i+1
        if not(None in retrieved_data):
            print("No. "+str(i)+str(retrieved_data))
            csv_file.feed(retrieved_data)
        else:
            print("dst port or src port is None")
            
        if(csv_file.get_data_length() >= CONST_MAX_LEN):
            print("!!!!!!!write!!!!!!")
            csv_file.write_csv_file()
            i = i+1
    return

if __name__ == '__main__':
    sys.exit(main(sys.argv))