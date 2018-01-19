import sys
import read_packet

def main(argv):
    packet = read_packet.read_packet()
    read_whole_packet = packet.get_whole_packet()

    for ts, pkt in read_whole_packet:
        print(pkt)

    return

if __name__ == '__main__':
    sys.exit(main(sys.argv))