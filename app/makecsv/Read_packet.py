import csv
import os

class Read_packet:
    
    def __init__(self):
        self.dirpath = '../bigdue_app/static/data/packet'
        self.packet_list = []
        print(os.getcwd())
        self.csvlist = os.listdir(self.dirpath)

        for index, csvs in enumerate(self.csvlist):
            print(str(index)+' : '+csvs)
        
        start = int(input("Enter a start csv file num : "))
        end = int(input("Enter a end csv file num : "))+1

        self.csvlist = self.csvlist[start:end]


    def read_packet(self, ):
            print("write packet")
            for csvs in self.csvlist:
                with open(self.dirpath+csvs, newline='') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                    for row in spamreader:
                        # print(row)
                        packets = row[0].split(',')
                        self.packet_list.append({
                            'timestamp' : packets[0],
                            'src_ipaddress' : packets[1],
                            'src_port' : packets[2],
                            'dst_ipaddress' : packets[3],
                            'dst_port' : packets[4],
                            'packet_size' : packets[5]})

            print(len(self.packet_list))

s = Read_packet()
s.read_packet()