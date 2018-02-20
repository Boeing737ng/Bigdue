import dpkt
import sys
try:
    import ManipulatePackets
except ImportError:
    from app.bigdue_app import ManipulatePackets

def main():
    manipulated_packet = ManipulatePackets.ManipulatePackets()

    with open('/Users/gimseungtae/Desktop/test.pcap', 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for timestamp, read_data in pcap:
            retrieved_data = manipulated_packet.retrieve_data(timestamp, read_data)
            print(retrieved_data)
            

if __name__ == '__main__':
    sys.exit(main())