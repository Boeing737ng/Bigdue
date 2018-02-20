import csv

class Write_packet:
    def __init__(self):
        pass

    def write_packet(self, file_name, data):
            # csv_file = open(file_name+"/packet/packet.csv", 'w', newline='')
            csv_file = open("static/data/packet/" + file_name + ".csv", 'w', newline='')
            writer = csv.writer(csv_file)
            writer.writerow(
                ['timestamp',
                'src_ipaddress',
                'src_port',
                'dst_ipaddress',
                'dst_port',
                'packet_size'])
            print("packet/"+file_name+" : "+str(len(data))+" packet write")
            
            for row in data:
                writer.writerow(
                    [row['timestamp'],
                    row['src_ipaddress'],
                    row['src_port'],
                    row['dst_ipaddress'],
                    row['dst_port'],
                    row['bytes']])

            csv_file.close()

    def write_wireshark_packet(self, file_name, data):
            # csv_file = open(file_name+"/packet/packet.csv", 'w', newline='')
            csv_file = open("static/data/wireshark/" + file_name + ".csv", 'w', newline='')
            writer = csv.writer(csv_file)
            writer.writerow(
                ['timestamp',
                'src_ipaddress',
                'src_port',
                'dst_ipaddress',
                'dst_port',
                'packet_size'])
                 
            print("wireshark/"+file_name+" : "+str(len(data))+" packet write")
            
            for row in data:
                writer.writerow(
                    [row['timestamp'],
                    row['src_ipaddress'],
                    row['src_port'],
                    row['dst_ipaddress'],
                    row['dst_port'],
                    row['bytes']])

            csv_file.close()