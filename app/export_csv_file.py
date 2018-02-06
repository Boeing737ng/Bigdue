#!/usr/bin/env python3

import csv
import time
import os
import UrlGeoloc

# class 나누기
class export_csv_file:

    time_list = list()
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
        print("make packet, graph, map file")
        self.file_name = file_name
        if file_name == None:
            self.file_name = str(time.time()).split('.')[0]

        self.file_name = "static/data/"+self.file_name
        # self.set_file_name(file_name)
        os.mkdir(self.file_name)
        os.mkdir(self.file_name+"/packet")
        os.mkdir(self.file_name+"/graph")
        os.mkdir(self.file_name+"/map")

        self.time_list.append(self.file_name)

        print("packet write")
        csv_file = open(self.file_name+"/packet/packet.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        writer.writerow(['timestamp', 'src_ipaddress', 'src_port', 'dst_ipaddress', 'dst_port', 'packet_size'])\

        for row in self.data:
            writer.writerow(row)
        csv_file.close()

        self.map_edge_vis()
        self.map_node_vis()

        self.data = list()

    def set_file_name(self, file_name):
        self.file_name = file_name
        self.rename_csv()
    
    def get_data_length(self):
        return len(self.data)

    def graph_edge_vis(self):
        print("graph_edge write")
        duplicate = {}
        for read_data in self.data:
            dup_key = read_data[1]+","+read_data[3]

            try:
                duplicate[dup_key] += 1
            except:
                duplicate[dup_key] = 1
        
        csv_file = open(self.file_name+"/graph/edge1.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        
        writer.writerow(['src_ipaddress', 'dst_ipaddress', 'packet_num'])

        max_value = max(duplicate.values())

        for key, value in duplicate.items():
            value_ratio = value/max_value * 10
            splited = key.split(',')
            writer.writerow([splited[0], splited[1], value_ratio])

        csv_file.close()

        return duplicate

    def graph_node_vis(self):
        print("graph_node write")
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
        
        csv_file = open(self.file_name+"/graph/node.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        
        writer.writerow(['node', 'weight'])

        for key, value in duplicate.items():
            writer.writerow([key, value])

        csv_file.close()

        return duplicate

    def map_edge_vis(self):
        print("map_edge write")
        graph_edge = self.graph_edge_vis()

        duplicate = {}
        for key, value in graph_edge.items():
            splited = key.split(',')
            geoloc = self.urlGeoloc.get_url_geoloc(splited[0])
            geoloc2 = self.urlGeoloc.get_url_geoloc(splited[1])
            dup_key = str(geoloc[0])+','+str(geoloc[1])+','+str(geoloc2[0])+','+str(geoloc2[1])
            try:
                duplicate[dup_key] += value
            except:
                duplicate[dup_key] = value
        
        csv_file = open(self.file_name+"/map/edge.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        
        writer.writerow(['src_lat', 'src_lng', 'dst_lat', 'dst_lng', 'packet_size'])

        for key, value in duplicate.items():
            splited = key.split(',')
            writer.writerow([splited[0], splited[1], splited[2], splited[3], value])

        csv_file.close()

    def map_node_vis(self):
        print("map_node write")
        graph_node = self.graph_node_vis()

        duplicate = {}
        for key, value in graph_node.items():
            geoloc = self.urlGeoloc.get_url_geoloc(key)
            dup_key = str(geoloc[0])+','+str(geoloc[1])
            try:
                duplicate[dup_key] = value
            except:
                duplicate[dup_key] = value

        csv_file = open(self.file_name+"/map/node.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        
        writer.writerow(['node_lat', 'node_lng', 'contry'])

        for key, value in duplicate.items():
            splited = key.split(',')
            writer.writerow([splited[0], splited[1], value])

        csv_file.close()