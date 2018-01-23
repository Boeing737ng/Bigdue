#!/usr/bin/env python3

import sys
import csv
import node_vis

def main(argv):
    count = 0

    Node = node_vis.Node_vis()

    f = open('save_2.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)

    for line in rdr:
        if count != 0:
            Node.feed(line[1])
            Node.feed(line[3])
        count = count + 1
    f.close()

    Node.export_csv()
    # addNode.print_data()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
