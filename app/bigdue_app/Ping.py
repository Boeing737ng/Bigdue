import core

class Ping:

    def __init__(self):
        pass
        
    def get_avg_rtt(self, ipaddress):
        r = core.ping(ipaddress, udp = True)
        if r.avg_rtt == None:
            return 0
        return r.avg_rtt

    def get_max_rtt(self, ipaddress):
        r = core.ping(ipaddress, udp = True)
        if r.max_rtt == None:
            return 0
        return r.max_rtt

    def get_min_rtt(self, ipaddress):
        r = core.ping(ipaddress, udp = True)
        if r.min_rtt == None:
            return 0
        return r.min_rtt