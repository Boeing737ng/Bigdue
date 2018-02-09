import json
from urllib.request import urlopen
import geoip2.database
from math import sin, cos, sqrt, atan2, radians

class urlGeoloc:

    def __init__(self):
        self.reader = geoip2.database.Reader('geolite/GeoLite2-City.mmdb')
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
    
    def calculate_distance_btw_two_geoloc(self, src_ip_geoloc, dst_ip_geoloc):
        # approximate radius of earth in km
        R = 6373.0

        src_latitude = radians(float(src_ip_geoloc[0]))
        src_longitude = radians(float(src_ip_geoloc[1]))
        dst_latitude = radians(float(dst_ip_geoloc[0]))
        dst_longitude = radians(float(dst_ip_geoloc[1]))

        dlon = dst_longitude - src_longitude
        dlat = dst_latitude - src_latitude

        a = sin(dlat / 2) ** 2 + cos(src_latitude) * cos(dst_latitude) * sin(
            dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        # print("Result:", distance)
        # print("Should be:", 278.546, "km")
        return distance

