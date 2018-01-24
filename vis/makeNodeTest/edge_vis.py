#!/usr/bin/env python3

import sys
import csv


class Edge_vis(object):
    def __init__(self):
        self.data = list()

    def feed(self, data: object) -> object:
        self.data.append(data)

    def export_csv(self):
        data_process = {}
        # removeDup = list(set(self.data))
        with open('edge.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, quoting = csv.QUOTE_MINIMAL)
            writer.writerow(['edge', 'weight'])
            # writer.writerow([removeDup])
            # for read_data in removeDup:
            #     writer.writerow([read_data])
            for read_data in self.data:
                try:
                    data_process[read_data] += 1
                except:
                    data_process[read_data] = 1
            max_value = max(data_process.values())

            for key, value in data_process.items():
                value_ratio = value/max_value * 10
                splited = key.split(',')
                writer.writerow([splited[0],splited[1],value_ratio])

    def print(self):
        data_process = {}

        for read_data in self.data:
            try:
                data_process[read_data] += 1
            except:
                data_process[read_data] = 1
            for key, value in data_process.items():
                print([key, value])

    def print_removeDup(self):
        print(list(set(self.data)))