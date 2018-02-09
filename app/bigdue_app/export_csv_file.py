#!/usr/bin/env python3

import csv
import time
import os
import Write_packet
import Write_graph
import Write_map
import UrlGeoloc

# class 나누기
class Export_csv_file:
    
    # time_list = list()
    def __init__(self):
        self.data = list()
        self.urlGeoloc = UrlGeoloc.UrlGeoloc()
        self.file_name = ""

        self.write_packet = Write_packet.Write_packet()
        self.write_graph = Write_graph.Write_graph()
        self.write_map = Write_map.Write_map()

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
        if not(os.path.isdir("csv")):
            print("create csv folder")
            os.mkdir("csv")
        
        print("create packet, graph, map folder & file (in csv/timestamp folder)")
        self.file_name = file_name
        if file_name == None:
            self.file_name = str(time.time()).split('.')[0]

        self.file_name = "csv/"+self.file_name
        # self.set_file_name(file_name)

        os.mkdir(self.file_name)
        os.mkdir(self.file_name+"/packet")
        os.mkdir(self.file_name+"/graph")
        os.mkdir(self.file_name+"/map")
        os.mkdir(self.file_name+"/distance")


    def write_csv_file(self, file_name=None):
            self.create_folder(file_name)
            # self.time_list.append(self.file_name)
            
            self.write_packet.write_packet(self.file_name, self.data)

            graph_node = self.write_graph.write_graph_node(self.file_name, self.data)
            graph_edge = self.write_graph.write_graph_edge(self.file_name, self.data)
            
            self.write_map.write_map_node(self.file_name, graph_node)
            self.write_map.write_map_edge(self.file_name, graph_edge)
            
            # self.write_map_edge_distance_count()
            # self.write_map_edge_distance_size()

            self.data = list()

    def write_map_edge_distance_count(self):
        print("write map edge distance")
        csv_file = open(self.file_name + "/distance/edge_distance_count.csv", 'w', newline='')
        writer = csv.writer(csv_file)

        writer.writerow(
            ['src_lat', 'src_lng', 'dst_lat', 'dst_lng', 'count', 'distance'])

        duplicate = self.check_duplicate_of_map_edge()

        for key, value in duplicate.items():
            splited = key.split(',')
            distance = self.urlGeoloc.calculate_distance_btw_two_geoloc([splited[0], splited[1]], [splited[2], splited[3]])
            writer.writerow(
                [splited[0], splited[1], splited[2], splited[3], value, distance])

        csv_file.close()

    def check_duplicate_of_graph_edge_size(self):
        duplicate = {}
        for read_data in self.data:
            dup_key = read_data['src_ipaddress']+","+read_data['dst_ipaddress']

            try:
                duplicate[dup_key] += read_data['bytes']
            except:
                duplicate[dup_key] = read_data['bytes']
        return duplicate

    def check_duplicate_of_map_edge_size(self):
        graph_edge = self.check_duplicate_of_graph_edge_size()

        duplicate = {}
        for key, value in graph_edge.items():
            splited = key.split(',')
            geoloc = self.urlGeoloc.get_url_geoloc(splited[0])
            geoloc2 = self.urlGeoloc.get_url_geoloc(splited[1])
            dup_key = str(geoloc['lat']) + ',' + str(geoloc['lng']) + ',' + str(
                geoloc2['lat']) + ',' + str(geoloc2['lng'])
            try:
                duplicate[dup_key] += value
            except:
                duplicate[dup_key] = value
        return duplicate

    def write_map_edge_distance_size(self):
        print("write map edge distance")
        csv_file = open(self.file_name + "/distance/edge_distance_size.csv", 'w', newline='')
        writer = csv.writer(csv_file)

        writer.writerow(
            ['src_lat', 'src_lng', 'dst_lat', 'dst_lng', 'size', 'distance'])

        duplicate = self.check_duplicate_of_map_edge_size()

        for key, value in duplicate.items():
            splited = key.split(',')
            distance = self.urlGeoloc.calculate_distance_btw_two_geoloc([splited[0], splited[1]], [splited[2], splited[3]])
            writer.writerow(
                [splited[0], splited[1], splited[2], splited[3], value, distance])

        csv_file.close()