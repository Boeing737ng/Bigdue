import csv
try:
    import UrlGeoloc
except ImportError:
    from app.bigdue_app import UrlGeoloc
try:
    import Calulate_distance
except ImportError:
    from app.bigdue_app import Calulate_distance
# import Ping

class Write_distance:
    
    def __init__(self):
        self.urlGeoloc = UrlGeoloc.UrlGeoloc()
        self.calculate_distance = Calulate_distance.Calculate_distance()
        # self.ping = Ping.Ping()
        pass

    def write_map_edge_distance_count(self, file_name, duplicate_map_edge):
        print("write map edge distance")
        # csv_file = open(file_name + "/distance/edge_distance_count.csv", 'w', newline='')
        csv_file = open("static/data/distance/"+file_name, 'w', newline='')
        writer = csv.writer(csv_file)

        writer.writerow(
            ['src_lat', 'src_lng', 'dst_lat', 'dst_lng', 'count', 'distance', 'rtt'])

        duplicate = duplicate_map_edge
        timestamp_list = {}

        for key, value in duplicate.items():
            splited = key.split(',')
            reserved_key = splited[2]+','+splited[3]+','+splited[0]+','+splited[1]
            try:
                timestamp_list[key]['packet_num'] += value['packet_num']
                timestamp_list[key]['rtt'] = float(value['timestamp']) - float(timestamp_list[key]['rtt'])
            except:
                try:
                    timestamp_list[reserved_key]['packet_num'] += value['packet_num']
                    timestamp_list[reserved_key]['rtt'] = float(value['timestamp']) - float(timestamp_list[reserved_key]['rtt'])
                except:
                    timestamp_list[key] = {
                        'packet_num' : value['packet_num'],
                        'rtt' : float(value['timestamp'])
                    }

        for key, value in timestamp_list.items():
            splited = key.split(',')
            distance = self.calculate_distance.calculate_distance_btw_two_geoloc([splited[0], splited[1]], [splited[2], splited[3]])
            rtt = value['rtt']
            count = value['packet_num']
            if rtt < 10000:
                writer.writerow([splited[0], splited[1], splited[2], splited[3], count, distance, rtt])
        # for key, value in duplicate.items():
        #     splited = key.split(',')
        #     distance = self.calculate_distance.calculate_distance_btw_two_geoloc([splited[2], splited[3]], [splited[4], splited[5]])
        #     src_rtt = self.ping.get_avg_rtt(splited[0])
        #     dst_rtt = self.ping.get_avg_rtt(splited[1])
        #     writer.writerow([
        #         splited[0],
        #         splited[1],
        #         splited[2],
        #         splited[3],
        #         splited[4],
        #         splited[5],
        #         value,
        #         distance,
        #         src_rtt,
        #         dst_rtt])

        csv_file.close()



    def check_duplicate_of_graph_edge_size(self, data):
        duplicate = {}
        for read_data in data:
            dup_key = read_data['src_ipaddress']+","+read_data['dst_ipaddress']

            # try:
            #     duplicate[dup_key] += read_data['bytes']
            # except:
            #     duplicate[dup_key] = read_data['bytes']

            try:
                # duplicate[dup_key]['packet_num'] += 1
                # duplicate[dup_key]['timestamp'] += read_data['timestamp']
                duplicate[dup_key]['bytes'] += read_data['bytes']
            except:
                duplicate[dup_key] = {
                    # 'packet_num' : 1,
                    'timestamp' : read_data['timestamp'],
                    'bytes' : read_data['bytes']
                    }

        return duplicate

    def check_duplicate_of_map_edge_size(self, data):
        graph_edge = self.check_duplicate_of_graph_edge_size(data)

        duplicate = {}
        for key, value in graph_edge.items():
            splited = key.split(',')
            geoloc = self.urlGeoloc.get_url_geoloc(splited[0])
            geoloc2 = self.urlGeoloc.get_url_geoloc(splited[1])
            dup_key = str(geoloc['lat']) + ',' + str(geoloc['lng']) + ',' + str(
                geoloc2['lat']) + ',' + str(geoloc2['lng'])
            try:
                # duplicate[dup_key]['packet_num'] += value['packet_num']
                # duplicate[dup_key]['timestamp'] += value['timestamp']
                duplicate[dup_key]['bytes'] += value['bytes']
            except:
                duplicate[dup_key] = {
                    # 'packet_num' : value['packet_num'],
                    'timestamp' : value['timestamp'],
                    'bytes' : value['bytes']
                }
        
        # for key, value in duplicate.items():
        #     duplicate[key]['timestamp'] /= duplicate[key]['packet_num']

        return duplicate

    def write_map_edge_distance_size(self, file_name, data):
        print("write map edge distance")
        # csv_file = open(file_name + "/distance/edge_distance_size.csv", 'w', newline='')
        csv_file = open("static/data/distance/"+file_name, 'w', newline='')
        writer = csv.writer(csv_file)

        writer.writerow(
            ['src_lat', 'src_lng', 'dst_lat', 'dst_lng', 'size', 'distance', 'rtt'])

        duplicate = self.check_duplicate_of_map_edge_size(data)
        timestamp_list = {}

        for key, value in duplicate.items():
            splited = key.split(',')
            reserved_key = splited[2]+','+splited[3]+','+splited[0]+','+splited[1]
            try:
                timestamp_list[key]['bytes'] += value['bytes']
                timestamp_list[key]['rtt'] = float(value['timestamp']) - float(timestamp_list[key]['rtt'])
            except:
                try:
                    timestamp_list[reserved_key]['bytes'] += value['bytes']
                    timestamp_list[reserved_key]['rtt'] = float(value['timestamp']) - float(timestamp_list[reserved_key]['rtt'])
                except:
                    timestamp_list[key] = {
                        'bytes' : value['bytes'],
                        'rtt' : float(value['timestamp'])
                    }

        for key, value in timestamp_list.items():
            splited = key.split(',')
            distance = self.calculate_distance.calculate_distance_btw_two_geoloc([splited[0], splited[1]], [splited[2], splited[3]])
            rtt = value['rtt']
            count = value['bytes']
            if rtt < 10000:
                writer.writerow([splited[0], splited[1], splited[2], splited[3], count, distance, rtt])

        # print(duplicate)
        # for key, value in duplicate.items():
        #     splited = key.split(',')
        #     distance = self.calculate_distance.calculate_distance_btw_two_geoloc([splited[0], splited[1]], [splited[2], splited[3]])
        #     src_rtt = self.ping.get_avg_rtt(splited[0])
        #     dst_rtt = self.ping.get_avg_rtt(splited[1])
        #     writer.writerow(
        #         [splited[0], splited[1], splited[2], splited[3], value, distance, src_rtt, dst_rtt])

        csv_file.close()