import sys
import read_packet

def main(argv):
    packet = read_packet.read_packet()
    read_whole_packet = packet.get_whole_packet()

    for timestamp, read_data in read_whole_packet:
        retrieved_data = packet.retrieve_data(timestamp, read_data)
        if not(None in retrieved_data):
            print(retrieved_data)
        else:
            print("dst port or src port is None")
    return

if __name__ == '__main__':
    sys.exit(main(sys.argv))