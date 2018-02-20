import csv
import os

class Write_time:

    def __init__(self):
        self.remove_time_csv_file_list()
    
    def write_time_src(self, data, filename):
        print("write time src")
        data_process = dict()
        with open('static/data/time/' + filename + '_src.csv', 'w') as csvfile:
            fieldnames = ['ipaddress', 'date', 'time', 'data size', 'count']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            for read_data in data:

                ipaddress = read_data['src_ipaddress']
                date = read_data['timestamp']

                temp_data = data_process.get(ipaddress + date,
                                    {'ipaddress': read_data['src_ipaddress'],
                                     'date': read_data['timestamp'],
                                     'time': read_data['timestamp'],
                                     'data size': read_data['packet_size'],
                                     'count': 1
                                     })
                temp_data['count'] += 1

                data_process[ipaddress + date] = temp_data

            for row in data_process:
                #print(data_process[row])
                writer.writerow(data_process[row])

    def write_time_dst(self, data, filename):
        print("write time dst")
        data_process = dict()
        with open('static/data/time/' + filename + '_dst.csv', 'w') as csvfile:
            fieldnames = ['ipaddress', 'date', 'time', 'data size', 'count']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()

            for read_data in data:
                ipaddress = read_data['dst_ipaddress']
                date = read_data['timestamp']

                temp_data = data_process.get(ipaddress + date,
                                    {'ipaddress': read_data['dst_ipaddress'],
                                     'date': read_data['timestamp'],
                                     'time': read_data['timestamp'],
                                     'data size': read_data['packet_size'],
                                     'count': 1
                                     })
                temp_data['count'] += 1

                data_process[ipaddress + date] = temp_data

            for row in data_process:
                #print(data_process[row])
                writer.writerow(data_process[row])

    def remove_time_csv_file_list(self):
        file_path = os.getcwd()+'/static/data/time/'
        for file in os.listdir(file_path):
            if file.endswith('.csv'):
                os.remove(file_path+file)