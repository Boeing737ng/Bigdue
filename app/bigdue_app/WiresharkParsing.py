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

def get_csv_list():
    csvlist = list()
    file_path = os.getcwd()+'/static/wiresharkFolder/'
    for file in os.listdir(file_path):
        if file.endswith('.pcap'):
            csvlist.append(file)

    csvlist.sort(key=lambda f: str(''.join(filter(str.isalpha, f))))
    return csvlist

def main():
    manipulated_packet = ManipulatePackets.ManipulatePackets()
    csv_file = Export_csv_file.Export_csv_file()
    print(get_csv_list())
    
    with open('/Users/gimseungtae/Desktop/test.pcap', 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for timestamp, read_data in pcap:
            retrieved_data = manipulated_packet.retrieve_data(timestamp, read_data)
            if not(None in retrieved_data.values()):
                csv_file.feed(retrieved_data)

        csv_file.write_csv_file(filename)

if __name__ == '__main__':
    sys.exit(main())