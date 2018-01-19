import pcap
# import l4_Layer from Layer

from Layer import l4_Layer
def test():
    nic_devs = pcap.findalldevs()

    if len(nic_devs) < 1:
       print("no network card")

    print("My Network Card Names : ", nic_devs)
    
    # nic_name = input('Input the Network Card Names : ')

    read_whole_packet = pcap.pcap(name="en0", promisc=True, immediate=True, timeout_ms=50)

    for ts, pkt in read_whole_packet:
        print("--------------------------------")
        # print(pkt)
        retrieved_data = retrieve_data(pkt)
        if not(None in retrieved_data):
            print(retrieved_data)
        else :
            print("None!!!!!!!!!!!!!")

        # retrieved_data = retrieve_data(pkt)
        # if not(None in retrieved_data):
        #     packet_deque.append(retrieved_data)
        #     print(retrieved_data)

def retrieve_data(data):
    receive = l4_Layer.l4_Layer(data)
    src_ipaddress = receive.get_src_ipaddress()
    dst_ipaddress = receive.get_dst_ipaddress()
    src_port = receive.get_src_port()
    dst_port = receive.get_dst_port()

    return [src_ipaddress, src_port, dst_ipaddress, dst_port]

test()