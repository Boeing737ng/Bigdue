#!/usr/bin/env python3

import sys
import csv


class Vis2(object):
    def __init__(self):
        self.data = list()

    def feed(self, data: object) -> object:
        self.data.append(data)

    def export_csv(self):
        with open('vis2.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, quoting = csv.QUOTE_MINIMAL)
            writer.writerow(['data'])
            for read_data in self.data:
                writer.writerow([read_data])
