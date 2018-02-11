import pyping

class Ping:

    def __init__(self):
         pass
        
    def get_rtt(self, ipaddress):
        r = pyping.ping(ipaddress, udp = True)
        return [r.ret_code, r.avg_rtt]

s = Ping()
print(s.get_rtt("www.naver.com"))