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

from threading import Thread

CONST_MAX_LEN = 10000

def main():
    packet = ReadPacket.ReadPacket()
    manipulated_packet = ManipulatePackets.ManipulatePackets()
    read_whole_packet = packet.get_whole_packet()
    csv_file = Export_csv_file.Export_csv_file()

    i = 0
    print("Packet Read Start")
    try:
        for timestamp, read_data in read_whole_packet:
            retrieved_data = manipulated_packet.retrieve_data(timestamp, read_data)
            print(read_data)
            if not(None in retrieved_data.values()):
                csv_file.feed(retrieved_data)
                i = i+1
                if i % 1000 == 0:
                    print(str(i)+" packets appended before wrting csv file")
                
            if(csv_file.get_data_length() >= CONST_MAX_LEN):
                csv_file.write_csv_file()
                i = 0
                print("------------- packet Write End -------------")
                
    except KeyboardInterrupt:
        csv_file.write_csv_file()
        print("packet Write End")
        sys.exit(0)
    return

if __name__ == '__main__':
    sys.exit(main())