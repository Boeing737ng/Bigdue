#!/usr/bin/env python3

import csv
import time
import os
import UrlGeoloc

# class 나누기
class export_csv_file:
    
    # time_list = list()
    def __init__(self):
        self.data = list()
        self.urlGeoloc = UrlGeoloc.urlGeoloc()
        self.file_name = ""

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

    def write_packet(self):
        print("write packet")
        csv_file = open(self.file_name+"/packet/packet.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        writer.writerow(
            ['timestamp',
            'src_ipaddress',
            'src_port',
            'dst_ipaddress',
            'dst_port',
            'packet_size'])

        for row in self.data:
            writer.writerow(
                [row['timestamp'],
                row['src_ipaddress'],
                row['src_port'],
                row['dst_ipaddress'],
                row['dst_port'],
                row['bytes']])

        csv_file.close()

    def write_csv_file(self, file_name=None):
        self.create_folder(file_name)
        # self.time_list.append(self.file_name)

        self.write_packet()
        self.write_map_edge()
        self.write_map_node()
        self.write_map_edge_distance_count()
        self.write_map_edge_distance_size()

        self.data = list()



    def check_duplicate_of_graph_edge(self):
        duplicate = {}
        for read_data in self.data:
            dup_key = read_data[1]+","+read_data[3]

            try:
                duplicate[dup_key] += 1
            except:
                duplicate[dup_key] = 1
        return duplicate

    def write_graph_edge(self):
        print("write graph_edge")
        csv_file = open(self.file_name+"/graph/edge.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        
        writer.writerow(['src_ipaddress', 'dst_ipaddress', 'packet_num'])
        
        duplicate = self.check_duplicate_of_graph_edge()
        max_value = max(duplicate.values())

        for key, value in duplicate.items():
            value_ratio = value/max_value * 10
            splited = key.split(',')
            writer.writerow([splited[0], splited[1], value_ratio])

        csv_file.close()

        return duplicate

    def check_duplicate_of_graph_node(self):
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

    def write_graph_node(self):
        print("write graph_node")
        
        csv_file = open(self.file_name+"/graph/node.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        
        writer.writerow(['node', 'weight'])

        duplicate = self.check_duplicate_of_graph_node()

        for key, value in duplicate.items():
            writer.writerow([key, value])

        csv_file.close()

        return duplicate
    
    def check_duplicate_of_map_node(self):
        graph_node = self.write_graph_node()

        duplicate = {}
        for key, value in graph_node.items():
            geoloc = self.urlGeoloc.get_url_geoloc(key)
            dup_key = str(geoloc[0])+','+str(geoloc[1])
            try:
                duplicate[dup_key] = [geoloc[2], geoloc[3], geoloc[4]]
            except:
                duplicate[dup_key] = [geoloc[2], geoloc[3], geoloc[4]]
        return duplicate

    def write_map_node(self):
        print("write map_node")
        csv_file = open(self.file_name+"/map/node.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        
        writer.writerow(['node_lat', 'node_lng', 'contry', 'state', 'city'])

        duplicate = self.check_duplicate_of_map_node()
        
        for key, value in duplicate.items():
            splited = key.split(',')
            writer.writerow([splited[0], splited[1], value[0], value[1], value[2]])

        csv_file.close()



    def check_duplicate_of_map_edge(self):
        graph_edge = self.write_graph_edge()

        duplicate = {}
        for key, value in graph_edge.items():
            splited = key.split(',')
            geoloc = self.urlGeoloc.get_url_geoloc(splited[0])
            geoloc2 = self.urlGeoloc.get_url_geoloc(splited[1])
            dup_key = str(geoloc[0]) + ',' + str(geoloc[1]) + ',' + str(
                geoloc2[0]) + ',' + str(geoloc2[1])
            try:
                duplicate[dup_key] += value
            except:
                duplicate[dup_key] = value
        return duplicate

    def write_map_edge(self):
        print("write map_edge")
        csv_file = open(self.file_name + "/map/edge.csv", 'w', newline='')
        writer = csv.writer(csv_file)

        writer.writerow(
            ['src_lat', 'src_lng', 'dst_lat', 'dst_lng', 'count'])

        duplicate = self.check_duplicate_of_map_edge()

        for key, value in duplicate.items():
            splited = key.split(',')
            writer.writerow(
                [splited[0], splited[1], splited[2], splited[3], value])

        csv_file.close()

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
            dup_key = read_data[1]+","+read_data[3]

            try:
                duplicate[dup_key] += read_data[5]
            except:
                duplicate[dup_key] = read_data[5]
        return duplicate

    def check_duplicate_of_map_edge_size(self):
        graph_edge = self.check_duplicate_of_graph_edge_size()

        duplicate = {}
        for key, value in graph_edge.items():
            splited = key.split(',')
            geoloc = self.urlGeoloc.get_url_geoloc(splited[0])
            geoloc2 = self.urlGeoloc.get_url_geoloc(splited[1])
            dup_key = str(geoloc[0]) + ',' + str(geoloc[1]) + ',' + str(
                geoloc2[0]) + ',' + str(geoloc2[1])
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