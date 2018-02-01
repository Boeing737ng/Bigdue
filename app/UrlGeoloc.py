import json
from urllib.request import urlopen

class urlGeoloc:

    def __init__(self):
        self.response_url = "http://freegeoip.net/json/"

    def get_url_geoloc(self, ipaddress):
        url_geoloc = urlopen(self.response_url+ipaddress).read().decode('utf-8')
        response_json = json.loads(url_geoloc)
        return response_json