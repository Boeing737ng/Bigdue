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
        self.file_name = file_name
        if file_name == None:
            self.file_name = str(time.time()).split('.')[0]
        # self.set_file_name(file_name)
        os.mkdir(self.file_name)

        self.edge_vis()
        self.node_vis()
        # csv_file = open(self.file_name, 'w', newline='')
        # writer = csv.writer(csv_file)
        # # writer.writerow(['timestamp', 'src_ipaddress', 'src_port', 'dst_ipaddress', 'dst_port'])
        # writer.writerow(['timestamp', 'src_lat', 'src_lng', 'src_contry', 'dst_lat', 'dst_lng', 'dst_contry', 'weight'])
        # for row in self.data:
        #     writer.writerow(row)
        # csv_file.close()
        self.data = list()

    def set_file_name(self, file_name):
        self.file_name = file_name
        self.rename_csv()
    
    def get_data_length(self):
        return len(self.data)

    def edge_vis(self):
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< edge_vis "+self.file_name+"/node.csv"+">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        csv_file = open(self.file_name+"/edge.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        writer.writerow(['src_lat', 'src_lng', 'dst_lat', 'dst_lng', 'weight'])
        
        for read_data in self.data:
            # writer.writerow(self.urlGeoloc.get_url_geoloc(read_data[1]))
            # writer.writerow(self.urlGeoloc.get_url_geoloc(read_data[2]))
            src_edge = self.urlGeoloc.get_url_geoloc(read_data[1])
            dst_edge = self.urlGeoloc.get_url_geoloc(read_data[2])
            # edge_data = self.urlGeoloc.get_url_geoloc(read_data[1])[0]
            # edge_data.extend(self.urlGeoloc.get_url_geoloc(read_data[2])[0])
            # edge_data.append(read_data[3])
            edge_data = [src_edge[0], src_edge[1], dst_edge[0], dst_edge[1], read_data[3]]
            writer.writerow(edge_data)
        
        csv_file.close()


    def node_vis(self):
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< node_vis "+self.file_name+"/node.csv"+">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        csv_file = open(self.file_name+"/node.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        # # writer.writerow(['timestamp', 'src_ipaddress', 'src_port', 'dst_ipaddress', 'dst_port'])
        writer.writerow(['node_lat', 'node_lng', 'contry'])
        
        for read_data in self.data:
            # print("------------------------------ read_data ------------------------------")
            # print(read_data)
            # print(self.urlGeoloc.get_url_geoloc(read_data[1]))
            # print(self.urlGeoloc.get_url_geoloc(read_data[2]))
            writer.writerow(self.urlGeoloc.get_url_geoloc(read_data[1]))
            writer.writerow(self.urlGeoloc.get_url_geoloc(read_data[2]))
            # geoloc = self.urlGeoloc.get_url_geoloc(read_data[1])
        
        csv_file.close()