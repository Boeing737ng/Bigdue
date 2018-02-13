import csv

class Write_graph:
    
    def __init__(self):
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

    def write_graph_node(self, file_name, data):
        print("write graph_node")
        
        # csv_file = open(file_name+"/graph/node.csv", 'w', newline='')
        csv_file = open("static/data/graph/"+file_name, 'w', newline='')
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

    def write_graph_edge(self, file_name, data):
        print("write graph_edge")
        # csv_file = open(file_name+"/graph/edge.csv", 'w', newline='')
        csv_file = open("static/data/graph/"+file_name, 'w', newline='')
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