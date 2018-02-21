import csv
import sys
import os

def main():
    dirpath = 'static/data/packet/'
    wireshark_dirpath = 'static/data/wireshark/'
    file_name = input("file name : ")
    packet_list = list()
    csvlist = get_csv_list()

    print(str(csvlist)+'csv reading start')
    for csvs in csvlist:
        with open(dirpath+csvs, encoding = 'utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in list(spamreader)[1:]:
                packets = row[0].split(',')
                packet_list.append({
                    'timestamp' : packets[0],
                    'src_ipaddress' : packets[1],
                    'src_port' : packets[2],
                    'dst_ipaddress' : packets[3],
                    'dst_port' : packets[4],
                    'packet_size' : packets[5]})

    print('read '+str(len(packet_list))+'packets')

    print(file_name +".csv file writting start")
    csv_file = open(wireshark_dirpath+file_name + ".csv", 'w', newline='')
    writer = csv.writer(csv_file)

    for row in packet_list:
        writer.writerow(
            [row['timestamp'],
            row['src_ipaddress'],
            row['src_port'],
            row['dst_ipaddress'],
            row['dst_port'],
            row['packet_size']])
    
    print(file_name +".csv file writting end")
    csv_file.close()

def get_csv_list():
    csvlist = list()
    file_path = 'static/data/packet/'
    for file in os.listdir(file_path):
        if file.endswith('.csv'):
            csvlist.append(file)

    csvlist.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    return csvlist

if __name__ == '__main__':
    sys.exit(main())