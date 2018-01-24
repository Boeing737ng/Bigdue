"""
start timestamp
end timestamp
src ip
src port
dst ip
dst port
No packets
length of data(bytes)
"""

class tcp_flow:
    # def check_for_syn(self):
    def __init__(self):
        return

    def create_key_for_packet_received(self, retrieved_data):
        packet_entry_key = str(retrieved_data[1])+str(retrieved_data[2])\
                           +str(retrieved_data[3])+str(retrieved_data[4])

        print(packet_entry_key)
        return packet_entry_key

