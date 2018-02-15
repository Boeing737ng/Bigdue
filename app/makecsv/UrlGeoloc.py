import json
from urllib.request import urlopen
import geoip2.database
import os

class UrlGeoloc:

    def __init__(self):
        current_path = os.getcwd()
        print(current_path)
        self.reader = geoip2.database.Reader(os.getcwd()+'/geolite/GeoLite2-City.mmdb')
        self.set_public_ipaddress()

    def get_url_geoloc(self, ipaddress):
        try:
            response = self.reader.city(ipaddress)
        except:
            response = self.reader.city(self.get_public_ipaddress())
        
        geoloc_dup = {
            'lat' : response.location.latitude,
            'lng' : response.location.longitude,
            'country' : response.country.name,
            'state' : response.subdivisions.most_specific.name,
            'city' : response.city.name
        }
        # [response.location.latitude, response.location.longitude, response.country.name, response.subdivisions.most_specific.name, response.city.name]
        return geoloc_dup

    def set_public_ipaddress(self, ipaddress=None):
        if ipaddress is None:
            checkip = urlopen('http://checkip.dyndns.org').read()
            ipaddress = str(checkip).split('IP Address: ')[1].split('<')[0]
            
        self.public_ip = ipaddress

    def get_public_ipaddress(self):
        return self.public_ip