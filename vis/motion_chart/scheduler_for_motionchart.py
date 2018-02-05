import sys
import csv
import src_vis, dst_vis

def main(argv):
    count = 0

    Src = src_vis.Src_vis()
    Dst = dst_vis.Dst_vis()

    f = open('csvfile/save_1.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)

    for line in rdr:
        if count != 0:
            Src.feed(line)
            Dst.feed(line)
        count = count + 1
    f.close()

    Src.export_csv()
    Dst.export_csv()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
