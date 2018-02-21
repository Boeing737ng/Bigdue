import csv
import os

class Read_packet:
    
    def __init__(self):
        self.dirpath = 'static/data/packet/'
        self.wireshark_dirpath = 'static/data/wireshark/'
        self.packet_list = []
        
        self.create_folder()
        
        self.csvlist = list()
        self.get_csv_file_list()

    def read_packet(self, start, end):
        print('packets reading start')
        for csvs in self.csvlist[int(start):int(end)]:
            with open(self.dirpath+csvs, encoding = 'utf-8') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in list(spamreader)[1:]:
                    packets = row[0].split(',')
                    self.packet_list.append({
                        'timestamp' : packets[0],
                        'src_ipaddress' : packets[1],
                        'src_port' : packets[2],
                        'dst_ipaddress' : packets[3],
                        'dst_port' : packets[4],
                        'packet_size' : packets[5]})

        print('read '+str(len(self.packet_list))+'packets')
        return self.packet_list

    def wireshark_read_packet(self, data):
        print('wireshark packets reading start')
        for csvs in data:
            with open(self.wireshark_dirpath+csvs, encoding = 'utf-8') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in list(spamreader)[1:]:
                    packets = row[0].split(',')
                    self.packet_list.append({
                        'timestamp' : packets[0],
                        'src_ipaddress' : packets[1],
                        'src_port' : packets[2],
                        'dst_ipaddress' : packets[3],
                        'dst_port' : packets[4],
                        'packet_size' : packets[5]})

        print('read '+str(len(self.packet_list))+'packets')
        return self.packet_list

    def create_folder(self, file_name=None):                                                                                                            
        data_root = "static/data/"

        if not(os.path.isdir("static/")):
            print("create static folder")
            os.mkdir("static/")
        if not(os.path.isdir(data_root)):
            print("create static/data folder")
            os.mkdir(data_root)
        if not(os.path.isdir(data_root+ "graph/")):
            print("create static/data/graph folder")
            os.mkdir(data_root + "graph/")
        if not(os.path.isdir(data_root + "distance/")):
            print("create static/data/distance folder")
            os.mkdir(data_root + "distance/")
        if not(os.path.isdir(data_root + "/map")):
            print("create static/data/map folder")
            os.mkdir(data_root + "map/")
        if not(os.path.isdir(data_root + "/time")):
            print("create static/data/time folder")
            os.mkdir(data_root + "time/")

    def get_csv_file_list(self):
        file_path = os.getcwd()+'/static/data/packet/'
        for file in os.listdir(file_path):
            if file.endswith('.csv'):
                self.csvlist.append(file)
        self.csvlist.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
        return self.csvlist