import core

class Ping:

    def __init__(self):
        pass
        
    def get_avg_rtt(self, ipaddress):
        r = core.ping(ipaddress, udp = True)
        return r.avg_rtt

    def get_max_rtt(self, ipaddress):
        r = core.ping(ipaddress, udp = True)
        return r.max_rtt

    def get_min_rtt(self, ipaddress):
        r = core.ping(ipaddress, udp = True)
        return r.min_rtt