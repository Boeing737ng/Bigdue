#!/usr/bin/env python3

import sys
import csv
import node_vis

def main(argv):
    count = 0

    srcNode = node_vis.Node_vis()
    dstNode = node_vis.Node_vis()

    f = open('save_2.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)

    for line in rdr:
        if count != 0:
            srcNode.feed(line[1])
            dstNode.feed(line[3])
        count = count + 1
    f.close()

    srcNode.export_csv('src')
    dstNode.export_csv('dst')
    # addNode.print_data()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
