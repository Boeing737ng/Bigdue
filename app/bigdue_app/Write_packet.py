import csv

class Write_packet:
    def __init__(self):
        pass

    def write_packet(self, file_name, data):
            print("write packet")
            csv_file = open(file_name+"/packet/packet.csv", 'w', newline='')
            writer = csv.writer(csv_file)
            writer.writerow(
                ['timestamp',
                'src_ipaddress',
                'src_port',
                'dst_ipaddress',
                'dst_port',
                'packet_size'])

            for row in data:
                writer.writerow(
                    [row['timestamp'],
                    row['src_ipaddress'],
                    row['src_port'],
                    row['dst_ipaddress'],
                    row['dst_port'],
                    row['bytes']])

            csv_file.close()