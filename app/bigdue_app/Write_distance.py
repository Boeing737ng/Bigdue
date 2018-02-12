import csv
import UrlGeoloc
import Calulate_distance

class Write_distance:
    
    def __init__(self):
        self.urlGeoloc = UrlGeoloc.UrlGeoloc()
        self.calculate_distance = Calulate_distance.Calculate_distance()
        return

    def write_map_edge_distance_count(self, file_name, duplicate_map_edge):
        print("write map edge distance")
        csv_file = open(file_name + "/distance/edge_distance_count.csv", 'w', newline='')
        writer = csv.writer(csv_file)

        writer.writerow(
            ['src_ip', 'dst_ip', 'src_lat', 'src_lng', 'dst_lat', 'dst_lng', 'count', 'distance'])

        duplicate = duplicate_map_edge

        for key, value in duplicate.items():
            splited = key.split(',')
            distance = self.calculate_distance.calculate_distance_btw_two_geoloc([splited[2], splited[3]], [splited[4], splited[5]])
            writer.writerow(
                [splited[0], splited[1], splited[2], splited[3], splited[4], splited[5], value, distance])

        csv_file.close()



    def check_duplicate_of_graph_edge_size(self, data):
        duplicate = {}
        for read_data in data:
            dup_key = read_data['src_ipaddress']+","+read_data['dst_ipaddress']

            try:
                duplicate[dup_key] += read_data['bytes']
            except:
                duplicate[dup_key] = read_data['bytes']
        return duplicate

    def check_duplicate_of_map_edge_size(self, data):
        graph_edge = self.check_duplicate_of_graph_edge_size(data)

        duplicate = {}
        for key, value in graph_edge.items():
            splited = key.split(',')
            geoloc = self.urlGeoloc.get_url_geoloc(splited[0])
            geoloc2 = self.urlGeoloc.get_url_geoloc(splited[1])
            dup_key = str(splited[0]) + ',' + str(splited[1]) + ',' + str(geoloc['lat']) + ',' + str(geoloc['lng']) + ',' + str(
                geoloc2['lat']) + ',' + str(geoloc2['lng'])
            try:
                duplicate[dup_key] += value
            except:
                duplicate[dup_key] = value
        return duplicate

    def write_map_edge_distance_size(self, file_name, data):
        print("write map edge distance")
        csv_file = open(file_name + "/distance/edge_distance_size.csv", 'w', newline='')
        writer = csv.writer(csv_file)

        writer.writerow(
            ['src_ip', 'dst_ip', 'src_lat', 'src_lng', 'dst_lat', 'dst_lng', 'size', 'distance'])

        duplicate = self.check_duplicate_of_map_edge_size(data)

        for key, value in duplicate.items():
            splited = key.split(',')
            distance = self.calculate_distance.calculate_distance_btw_two_geoloc([splited[2], splited[3]], [splited[4], splited[5]])
            writer.writerow(
                [splited[0], splited[1], splited[2], splited[3], splited[3], splited[5], value, distance])

        csv_file.close()