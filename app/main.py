import sys
import read_packet

def main(argv):
    packet = read_packet.read_packet()
    read_whole_packet = packet.get_whole_packet()

    for timestamp, read_data in read_whole_packet:
        print(packet.retrieve_data(timestamp, read_data))
    return

if __name__ == '__main__':
    sys.exit(main(sys.argv))