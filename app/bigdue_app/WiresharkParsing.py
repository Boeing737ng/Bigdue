import dpkt
import sys
import os
try:
    import Export_csv_file
except ImportError:
    from app.bigdue_app import Export_csv_file
try:
    import ManipulatePackets
except ImportError:
    from app.bigdue_app import ManipulatePackets

def get_pcap_list():
    pacplist = list()
    file_path = os.getcwd()+'/static/wiresharkFolder/'
    for file in os.listdir(file_path):
        if file.endswith('.pcap'):
            pacplist.append(file)

    pacplist.sort(key=lambda f: str(''.join(filter(str.isalpha, f))))
    return pacplist

def main():
    manipulated_packet = ManipulatePackets.ManipulatePackets()
    csv_file = Export_csv_file.Export_csv_file()
    
    wireshark_file_list = get_pcap_list()
    for wireshark_file_name in wireshark_file_list:
        print(wireshark_file_name)

    file_path = os.getcwd()+'/static/wiresharkFolder/'
    for wireshark_file_name in wireshark_file_list:
        with open(file_path + wireshark_file_name, 'rb') as f:
            pcap = dpkt.pcap.Reader(f)
            for timestamp, read_data in pcap:
                retrieved_data = manipulated_packet.retrieve_data(timestamp, read_data)
                if not(None in retrieved_data.values()):
                    csv_file.feed(retrieved_data)
            print(wireshark_file_name.split('.pcap')[0])
            csv_file.write_csv_file(wireshark_file_name.split('.pcap')[0])

if __name__ == '__main__':
    sys.exit(main())