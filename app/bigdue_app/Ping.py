import core

class Ping:

    def __init__(self):
         pass
        
    def get_avg_rtt(self, ipaddress):
        r = core.ping(ipaddress, udp = True)
        # print(r.destination_ip)
        return r.avg_rtt

    def get_max_rtt(self, ipaddress):
        r = core.ping(ipaddress, udp = True)
        return r.max_rtt

    def get_min_rtt(self, ipaddress):
        r = core.ping(ipaddress, udp = True)
        return r.min_rtt

# s = Ping()
# print(s.get_avg_rtt('172.226.93.134'))
#  src_ip, dst_ip, src_lat, src_lng, dst_lat, dst_lng, distance, rrt