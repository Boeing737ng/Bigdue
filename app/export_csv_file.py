#!/usr/bin/env python3

import csv
import time
import os
import UrlGeoloc

# class 나누기
class export_csv_file:

    def __init__(self):
        self.data = list()
        self.urlGeoloc = UrlGeoloc.urlGeoloc()
        self.file_name = ""
    
    def feed(self, data):
        self.data.append(data)

    def rename_csv(self):
        if self.file_name[-4:] != '.csv':
            self.file_name = self.file_name+".csv"

    def write_csv_file(self, file_name=None):
        print(self.map_edge_vis())
        print(self.map_node_vis())
        # self.file_name = file_name
        # if file_name == None:
        #     self.file_name = str(time.time()).split('.')[0]
        # # self.set_file_name(file_name)
        # os.mkdir(self.file_name)
        # os.mkdir(self.file_name+"/packet")
        # os.mkdir(self.file_name+"/graph")
        # os.mkdir(self.file_name+"/map")
        
        # csv_file = open(self.file_name+"/packet/packet.csv", 'w', newline='')
        # writer = csv.writer(csv_file)
        # writer.writerow(['timestamp', 'src_ipaddress', 'src_port', 'dst_ipaddress', 'dst_port', 'packet_size'])
        # # writer.writerow(['timestamp', 'src_lat', 'src_lng', 'src_contry', 'dst_lat', 'dst_lng', 'dst_contry', 'weight'])
        # for row in self.data:
        #     writer.writerow(row)
        # csv_file.close()

        self.data = list()

    def set_file_name(self, file_name):
        self.file_name = file_name
        self.rename_csv()
    
    def get_data_length(self):
        return len(self.data)

    def graph_edge_vis(self):
        duplicate = {}
        for read_data in self.data:
            dup_key = read_data[1]+","+read_data[3]

            try:
                duplicate[dup_key] += read_data[5] 
            except:
                duplicate[dup_key] = read_data[5]
                
        return duplicate

    def graph_node_vis(self):
        duplicate = {}
        for read_data in self.data:
            dup_key = read_data[1]

            try:
                duplicate[dup_key] += 1
            except:
                duplicate[dup_key] = 1

            dup_key = read_data[3]
            try:
                duplicate[dup_key] += 1
            except:
                duplicate[dup_key] = 1
        
        return duplicate

    def map_edge_vis(self):
        graph_edge = self.graph_edge_vis()
        map_edge = []
        for key, value in graph_edge.items():
            splited = key.split(',')
            geoloc = self.urlGeoloc.get_url_geoloc(splited[0])
            geoloc2 = self.urlGeoloc.get_url_geoloc(splited[1])
            map_edge.append([geoloc[0], geoloc[1], geoloc2[0], geoloc2[1], value])
        
        return map_edge

    def map_node_vis(self):
        graph_node = self.graph_node_vis()

        map_node = []
        for key, value in graph_node.items():

            geoloc = self.urlGeoloc.get_url_geoloc(key)
            map_node.append([geoloc[0], geoloc[1], geoloc[2]])
        
        return map_node