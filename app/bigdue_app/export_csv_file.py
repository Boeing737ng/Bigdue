#!/usr/bin/env python3

import csv
import time
import os
import Write_packet
import Write_graph
import Write_map
import Write_distance

# class 나누기
class Export_csv_file:
    
    # time_list = list()
    def __init__(self):
        self.data = list()
        self.file_name = ""

        self.write_packet = Write_packet.Write_packet()
        self.write_graph = Write_graph.Write_graph()
        self.write_map = Write_map.Write_map()
        self.write_distance = Write_distance.Write_distance()

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
            
            duplicate_map_edge = self.write_map.check_duplicate_of_map_edge(graph_edge)

            self.write_distance.write_map_edge_distance_count(self.file_name, duplicate_map_edge)
            self.write_distance.write_map_edge_distance_size(self.file_name, self.data)

            self.data = list()