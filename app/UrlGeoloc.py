import json
from urllib.request import urlopen
import geoip2.database

class urlGeoloc:

    def __init__(self):
        self.response_url = "http://freegeoip.net/json/"
        self.reader = geoip2.database.Reader('geolite/GeoLite2-City.mmdb')
        checkip = urlopen('http://checkip.dyndns.org').read()
        self.public_ip = str(checkip).split('IP Address: ')[1].split('<')[0]

    def get_url_geoloc(self, ipaddress):
        try:
            response = self.reader.city(ipaddress)
        except:
            response = self.reader.city(self.public_ip)
            
        return [response.location.latitude, response.location.longitude, response.country.iso_code]
        
    # def get_url_geoloc(self, ipaddress):
    #     url_geoloc = urlopen(self.response_url+ipaddress).read().decode('utf-8')
    #     response_json = json.loads(url_geoloc)
        
    #     if response_json['country_code'] == "":
    #         # print("-------------------in if")
    #         # 공유기 사용시 (192.168.) 공인ip 확인
    #         checkip = urlopen('http://checkip.dyndns.org').read()
    #         ipaddress = self.get_public_ipaddr(checkip)
    #         url_geoloc = urlopen(self.response_url+ipaddress).read().decode('utf-8')
    #         response_json = json.loads(url_geoloc)
    #     print(response_json)
    #     return [response_json['latitude'], response_json['longitude'], response_json['country_code']]


# test = urlGeoloc()
# print(test.get_url_geoloc('192.168.0.5'))
# print(test.get_url_geoloc('66.253.158.34'))
# print(test.get_url_geoloc('23.35.201.168'))