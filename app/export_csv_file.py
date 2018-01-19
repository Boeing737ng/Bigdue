#!/usr/bin/env python3

import csv

# class 나누기
class export_csv_file:

    def __init__(self, file_name, data):  
        self.file_name = file_name
        self.data = data
    
    def check_csv_name(self):
        if self.file_name[-4:] != '.csv':
            self.file_name = self.file_name+".csv"

    def write_csv_file(self):
        self.check_csv_name()

        csv_file = open(self.file_name, 'w', newline='')
        writer = csv.writer(csv_file)
        writer.writerow(['timestamp', 'src_ipaddress', 'src_port', 'dst_ipaddress', 'dst_port'])
        for row in self.data:
            writer.writerow(row)
        csv_file.close()