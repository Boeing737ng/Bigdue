import sys
import csv

class Src_vis(object):
    def __init__(self):
        self.data = list()

    def feed(self, data):
        self.data.append(data)

    def export_csv(self):
        data_process = dict()
        with open('csvfile/src.csv', 'w') as csvfile:
            fieldnames = ['ipaddress', 'date', 'time', 'data size', 'count']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()

            for read_data in self.data:
                ipaddress = read_data[1]
                date = read_data[0]

                temp_data = data_process.get(ipaddress + date,
                                    {'ipaddress': '"' + read_data[1] + '"',
                                     'date': read_data[0],
                                     'time': read_data[0],
                                     'data size': read_data[5],
                                     'count': 1
                                     })
                temp_data['count'] += 1

                data_process[ipaddress + date] = temp_data

            for row in data_process:
                #print(data_process[row])
                writer.writerow(data_process[row])

    def print_data(self):
        print(self.data)
