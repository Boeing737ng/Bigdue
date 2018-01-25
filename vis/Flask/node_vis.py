#!/usr/bin/env python3

import sys
import csv
import os


class Node_vis(object):
    def __init__(self):
        self.data = list()

    def feed(self, data: object) -> object:
        self.data.append(data)

    def setRootPath():
        APP_ROOT = os.path.dirname(os.path.abspath(__file__))
        target = os.path.join(APP_ROOT, 'static/data/')
        if not os.path.isdir(target):
            os.mkdir(target)
        return target

    def export_csv(self):
        root_path = Node_vis.setRootPath()
        data_process = {}
        filename = "node.csv"

        # removeDup = list(set(self.data))
        with open(root_path + filename, 'w') as csvfile:
            writer = csv.writer(csvfile, quoting = csv.QUOTE_MINIMAL)
            writer.writerow(['node', 'weight'])
            # writer.writerow([removeDup])
            # for read_data in removeDup:
            #     writer.writerow([read_data])
            for read_data in self.data:
                try:
                    data_process[read_data] += 1
                except:
                    data_process[read_data] = 1

            for key, value in data_process.items():
                writer.writerow([key,value])
                # writer.writerow([key, value])

    def print_removeDup(self):
        print(list(set(self.data)))\