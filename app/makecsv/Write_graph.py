import csv
import os

class Write_graph:
    
    def __init__(self):
        self.remove_graph_csv_file_list()
        pass

    def check_duplicate_of_graph_node(self, data):
        duplicate = {}
        for read_data in data:
            dup_key = read_data['src_ipaddress']

            try:
                duplicate[dup_key] += 1
            except:
                duplicate[dup_key] = 1

            dup_key = read_data['dst_ipaddress']
            try:
                duplicate[dup_key] += 1
            except:
                duplicate[dup_key] = 1
        
        return duplicate

    def write_graph_node(self, data, filename):
        print("write graph_node")
        
        # csv_file = open(file_name+"/graph/node.csv", 'w', newline='')
        # if os.path.isfile("static/data/graph/node.csv"):
        #     os.remove("static/data/graph/node.csv")
        #     print('old node file deleted')
        csv_file = open("static/data/graph/"+filename+"_node.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        
        writer.writerow(['node', 'weight'])

        duplicate = self.check_duplicate_of_graph_node(data)

        for key, value in duplicate.items():
            writer.writerow([key, value])

        csv_file.close()

        return duplicate

    def check_duplicate_of_graph_edge(self, data):
        duplicate = {}
        timestamp = {}
        for read_data in data:
            dup_key = read_data['src_ipaddress']+","+read_data['dst_ipaddress']

            # try:
            #     duplicate[dup_key] += 1
            # except:
            #     duplicate[dup_key] = 1
            try:
                duplicate[dup_key]['packet_num'] += 1
                # duplicate[dup_key]['timestamp'] += read_data['timestamp']
            except:
                duplicate[dup_key] = {
                    'packet_num' : 1,
                    'timestamp' : read_data['timestamp']
                    }
        return duplicate

    def write_graph_edge(self, data, filename):
        print("write graph_edge")
        # csv_file = open(file_name+"/graph/edge.csv", 'w', newline='')
        if os.path.isfile("static/data/graph/"+filename+"_edge.csv"):
            os.remove("static/data/graph/edge.csv")
            print('old edge file deleted')
        csv_file = open("static/data/graph/edge.csv", 'w', newline='')
        writer = csv.writer(csv_file)
        
        writer.writerow(['src_ipaddress', 'dst_ipaddress', 'packet_num', 'timestamp'])
        
        duplicate = self.check_duplicate_of_graph_edge(data)
    
        # max_value = max(duplicate.values())
        max_value = max(value['packet_num'] for value in duplicate.values())

        for key, value in duplicate.items():
            value_ratio = value['packet_num']/max_value * 10
            splited = key.split(',')
            writer.writerow([splited[0], splited[1], value_ratio, value['timestamp']])

        csv_file.close()

        return duplicate

    def remove_graph_csv_file_list(self):
        file_path = os.getcwd()+'/static/data/graph/'
        for file in os.listdir(file_path):
            if file.endswith('.csv'):
                os.remove(file_path+file)