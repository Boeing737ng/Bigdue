#!/usr/bin/env python3

import csv
import time
import os
try:
    import Write_packet
except ImportError:
    from app.bigdue_app import Write_packet

# class 나누기
class Export_csv_file:
    
    time_list = list()
    def __init__(self):
        self.data = list()
        self.file_name = ""
        data_root = "static/data/"

        if not(os.path.isdir("static/")):
            os.mkdir("static/")
        if not(os.path.isdir(data_root)):
            os.mkdir(data_root)
        if not(os.path.isdir(data_root + "packet/")):
            os.mkdir(data_root + "packet/")

        self.write_packet = Write_packet.Write_packet()

    def feed(self, data):
        self.data.append(data)

    def rename_csv(self):
        if self.file_name[-4:] != '.csv':
            self.file_name = self.file_name+".csv"

    def set_file_name(self, file_name):
        self.file_name = file_name
        self.rename_csv()
    
    def get_data_length(self):
        return len(self.data)
    
    def create_folder(self, file_name=None):                  
        print("create packet, graph, map folder & file (in static/data/timestamp folder)")
        self.file_name = file_name
        if file_name == None:
            self.file_name = str(time.time()).split('.')[0]
        if not self.file_name in self.time_list:
            self.time_list.append(self.file_name)
            print(self.time_list)

    def write_csv_file(self, file_name=None):
            self.create_folder(file_name)
            self.write_packet.write_packet(self.file_name, self.data)
            self.data = list()