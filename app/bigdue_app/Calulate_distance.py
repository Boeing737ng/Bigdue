from math import sin, cos, sqrt, atan2, radians

class Calculate_distance:
    def __init__(self):
        return

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

