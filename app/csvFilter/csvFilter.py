#!/usr/bin/env python3

import sys
import csv
from csvFilter import node_vis
from csvFilter import edge_vis

def main(argv):
    count = 0

    Node = node_vis.Node_vis()
    Edge = edge_vis.Edge_vis()

    f = open('save_1.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)

    for line in rdr:
        if count != 0:
            # print(line[1],line[3])
            # print([line[1],line[3]])
            Edge.feed(line[1]+","+line[3])
            Node.feed(line[1])
            Node.feed(line[3])
        count = count + 1
    f.close()

    Edge.export_csv()
    Node.export_csv()
    # addNode.print_data()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
