#!/usr/bin/env python3

import sys
import vis01, vis02

def main(argv):
    vis1 = vis01.Vis1()
    vis2 = vis02.Vis2()
    for index in range(0, 100):
        num = index
        char = str(index)
        vis1.feed(num)
        vis2.feed(char)

    vis1.export_csv()
    vis2.export_csv()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
