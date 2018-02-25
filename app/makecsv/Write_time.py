import csv
import os
from operator import itemgetter
from time import gmtime, strftime
class Write_time:

    def __init__(self):
        self.remove_time_csv_file_list()

    def get_count(self, x):
        return x[1]['count']

    def write_time_src(self, data, filename):
        print("write time src")
        data_process = dict()
        data_dict = dict()
        with open('static/data/time/' + filename + '_src.csv', 'w') as csvfile:
            fieldnames = ['ipaddress', 'date', 'time', 'data size', 'count']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()

            for read_data in data:
                ipaddress = read_data['src_ipaddress']
                data_dict[ipaddress] = data_dict.get(ipaddress, 0) + 1

            sorted_data = sorted(data_dict.items(), key=itemgetter(1), reverse=True)
            topset = set()
            for top in sorted_data[0:10]:
                topset.add(top[0])

            for read_data in data:
                ipaddress = read_data['src_ipaddress']
                data_ymd = read_data['timestamp']
                data_ymd = strftime("%Y%m%d", gmtime(int(float(data_ymd))))

                if not ipaddress in topset:
                    continue

                temp_data = data_process.get(ipaddress + data_ymd,
                                    {'ipaddress': read_data['src_ipaddress'],
                                     'date': read_data['timestamp'],
                                     'time': data_ymd,
                                     'data size': 0,
                                     'count': 1
                                     })
                temp_data['count'] += 1
                temp_data['data size'] += int(read_data['packet_size'])

                data_process[ipaddress + data_ymd] = temp_data

            for row in data_process.values():
                writer.writerow(row)

    def write_time_dst(self, data, filename):
        print("write time dst")
        data_process = dict()
        data_dict = dict()
        with open('static/data/time/' + filename + '_dst.csv', 'w') as csvfile:
            fieldnames = ['ipaddress', 'date', 'time', 'data size', 'count']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()

            for read_data in data:
                ipaddress = read_data['dst_ipaddress']
                data_dict[ipaddress] = data_dict.get(ipaddress, 0) + 1

            sorted_data = sorted(data_dict.items(), key=itemgetter(1), reverse=True)
            topset = set()
            for top in sorted_data[0:10]:
                topset.add(top[0])

            for read_data in data:
                ipaddress = read_data['dst_ipaddress']
                data_ymd = read_data['timestamp']
                data_ymd = strftime("%Y%m%d", gmtime(int(float(data_ymd))))

                if not ipaddress in topset:
                    continue

                temp_data = data_process.get(ipaddress + data_ymd,
                                    {'ipaddress': read_data['dst_ipaddress'],
                                     'date': read_data['timestamp'],
                                     'time': data_ymd,
                                     'data size': 0,
                                     'count': 1
                                     })
                temp_data['count'] += 1
                temp_data['data size'] += int(read_data['packet_size'])

                data_process[ipaddress + data_ymd] = temp_data

            for row in data_process.values():
                writer.writerow(row)

    def remove_time_csv_file_list(self):
        file_path = os.getcwd()+'/static/data/time/'
        for file in os.listdir(file_path):
            if file.endswith('.csv'):
                os.remove(file_path+file)
