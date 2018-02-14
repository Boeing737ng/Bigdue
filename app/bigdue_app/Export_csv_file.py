#!/usr/bin/env python3

import csv
import time
import os
try:
    import Write_packet
except ImportError:
    from app.bigdue_app import Write_packet
try:
    import Write_graph
except ImportError:
    from app.bigdue_app import Write_graph
try:
    import Write_map
except ImportError:
    from app.bigdue_app import Write_map
try:
    import Write_distance
except ImportError:
    from app.bigdue_app import Write_distance

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
        # data_root = "static/data/"

        # if not(os.path.isdir("static/")):
        #     os.mkdir("static/")
        # if not(os.path.isdir(data_root)):
        #     os.mkdir(data_root)
        # if not(os.path.isdir(data_root + "packet/")):
        #     os.mkdir(data_root + "packet/")
        # if not(os.path.isdir(data_root+ "graph/")):
        #     os.mkdir(data_root + "graph/")
        # if not(os.path.isdir(data_root + "distance/")):
        #     os.mkdir(data_root + "distance/")
        # if not(os.path.isdir(data_root + "/map")):
        #     os.mkdir(data_root + "map/")
        print("create packet, graph, map folder & file (in static/data/timestamp folder)")
        self.file_name = file_name
        if file_name == None:
            self.file_name = str(time.time()).split('.')[0]
        if not self.file_name in self.time_list:
            self.time_list.append(self.file_name)
            print(self.time_list)
        # self.file_name = "static/data/"+self.file_name
        # self.set_file_name(file_name)
		####
        # os.mkdir(self.file_name)
        # os.mkdir(self.file_name+"/packet")
        # os.mkdir(self.file_name+"/graph")
        # os.mkdir(self.file_name+"/map")
        # os.mkdir(self.file_name+"/distance")

    def write_csv_file(self, file_name=None):
            self.create_folder(file_name)
            
            self.write_packet.write_packet(self.file_name, self.data)

            # graph_node = self.write_graph.write_graph_node(self.file_name, self.data)
            # graph_edge = self.write_graph.write_graph_edge(self.file_name, self.data)
            
            # self.write_map.write_map_node(self.file_name, graph_node)
            # self.write_map.write_map_edge(self.file_name, graph_edge)
            
            # duplicate_map_edge = self.write_map.check_duplicate_of_map_edge(graph_edge)
            
            # self.write_distance.write_map_edge_distance_count(self.file_name, duplicate_map_edge)
            # self.write_distance.write_map_edge_distance_size(self.file_name, self.data)

            self.data = list()