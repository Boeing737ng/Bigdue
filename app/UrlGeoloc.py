import json
from urllib.request import urlopen

class urlGeoloc:

    def __init__(self):
        self.response_url = "http://freegeoip.net/json/"

    def get_url_geoloc(self, ipaddress):
        url_geoloc = urlopen(self.response_url+ipaddress).read()
        response_json = json.loads(url_geoloc)
        
        if response_json['country_code'] == "":
            # print("-------------------in if")
            # 공유기 사용시 (192.168.) 공인ip 확인
            checkip = urlopen('http://checkip.dyndns.org').read()
            ipaddress = self.get_public_ipaddr(checkip)
            url_geoloc = urlopen(self.response_url+ipaddress).read()
            response_json = json.loads(url_geoloc)
        
        return [response_json['latitude'], response_json['longitude'], response_json['country_code']]

    def get_public_ipaddr(self, ipaddr):
        return str(ipaddr).split('IP Address: ')[1].split('<')[0]

# test = urlGeoloc()
# print(test.get_url_geoloc('192.168.1.5'))
# print(test.get_url_geoloc('66.253.158.34'))
# print(test.get_url_geoloc('23.35.201.168'))