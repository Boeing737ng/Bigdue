import csv
import os

class Read_packet:
    
    def __init__(self):
        self.dirpath = 'static/data/packet/'
        self.packet_list = []
        # print(os.getcwd())
        self.create_folder()
        # self.csvlist = os.listdir(self.dirpath)
        self.get_csv_file_list()
        # for index, csvs in enumerate(self.csvlist):
        #     print(str(index)+' : '+csvs)
        
        # start = int(input("Enter a start csv file num : "))
        # end = int(input("Enter a end csv file num : "))+1

        # self.csvlist = self.csvlist[start:end]
        pass


    def read_packet(self, start, end):
            print("write packet")
            for csvs in self.csvlist[int(start):int(end)]:
                with open(self.dirpath+csvs, newline='') as csvfile:
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

            print(len(self.packet_list))
            return self.packet_list

    def create_folder(self, file_name=None):                                                                                                            
        data_root = "static/data/"

        if not(os.path.isdir("static/")):
            os.mkdir("static/")
        if not(os.path.isdir(data_root)):
            os.mkdir(data_root)
        if not(os.path.isdir(data_root+ "graph/")):
            os.mkdir(data_root + "graph/")
        if not(os.path.isdir(data_root + "distance/")):
            os.mkdir(data_root + "distance/")
        if not(os.path.isdir(data_root + "/map")):
            os.mkdir(data_root + "map/")

        print("create packet, graph, map folder & file (in static/data/timestamp folder)")

    def get_csv_file_list(self):
        file_path = os.getcwd()+'/static/data/packet/'
        for file in os.listdir(file_path):
            if file.endswith('.csv'):
                self.csvlist.push(file)
                #self.csvlist = os.listdir(file_path)
        if '.DS_Store' in self.csvList:
            self.csvList.remove('.DS_Store')
        print(self.csvList)
        return self.csvlist