try:
    import Read_packet
except ImportError:
    from app.makecsv import Read_packet

try:
    import Write_distance
except ImportError:
    from app.makecsv import Write_distance

try:
    import Write_graph
except ImportError:
    from app.makecsv import Write_graph

try:
    import Write_map
except ImportError:
    from app.makecsv import Write_map

import sys

def main(argv):
    start = argv[0]
    end = argv[1]
    filename = "1234"
    read_packet = Read_packet.Read_packet()

    write_graph = Write_graph.Write_graph()
    write_map = Write_map.Write_map()
    write_distance = Write_distance.Write_distance()

    data = read_packet.read_packet(argv[0], argv[1])

    graph_node = write_graph.write_graph_node(data, filename)
    graph_edge = write_graph.write_graph_edge(data, filename)
            
    write_map.write_map_node(graph_node, filename)
    write_map.write_map_edge(graph_edge, filename)
            
    duplicate_map_edge = write_map.check_duplicate_of_map_edge(graph_edge)
            
    write_distance.write_map_edge_distance_count(duplicate_map_edge, filename)
    write_distance.write_map_edge_distance_size(data, filename)

if __name__ == '__main__':
    sys.exit(main())