#!/usr/bin/env python3

import csv
import time

# class 나누기
class export_csv_file:

    def __init__(self):
        self.data = list()
        self.file_name = ""
    
    def feed(self, data):
        self.data.append(data)

    def rename_csv(self):
        if self.file_name[-4:] != '.csv':
            self.file_name = self.file_name+".csv"

    def write_csv_file(self, file_name=None):
        if file_name == None:
            file_name = str(time.time()).split('.')[0]
        self.set_file_name(file_name)

        csv_file = open(self.file_name, 'w', newline='')
        writer = csv.writer(csv_file)
        # writer.writerow(['timestamp', 'src_ipaddress', 'src_port', 'dst_ipaddress', 'dst_port'])
        writer.writerow(['timestamp', 'src_lat', 'src_lng', 'src_contry', 'dst_lat', 'dst_lng', 'dst_contry', 'weight'])
        for row in self.data:
            writer.writerow(row)
        csv_file.close()
        self.data = list()

    def set_file_name(self, file_name):
        self.file_name = file_name
        self.rename_csv()
    
    def get_data_length(self):
        return len(self.data)