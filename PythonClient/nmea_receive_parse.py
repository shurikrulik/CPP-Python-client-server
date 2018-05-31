import socket
import base64
import re
import pynmea2
from math import cos, sin

port = 8888
client = socket.socket()
client.connect(('10.3.141.143', port))

# approximate earth radius
R = 6378137

while True:

        data = client.recv(4096)
#        print(data)
        if data != b'':
            data1 = data.decode("UTF-8")
            GPRMC = re.search('\$GPRMC(.+?)\r\n',data1).group(0)
            GPRMC = pynmea2.parse(GPRMC)
            GPGGA = re.search('\$GPGGA(.+?)\r\n',data1).group(0)
            GPGGA = pynmea2.parse(GPGGA)
            print("lat: ", GPRMC.lat, "  lon: ", GPRMC.lon)
            lat = float(GPRMC.lat)
            lon = float(GPRMC.lon)
            x = R * cos(lat) * cos(lon)
            y = R * cos(lat) * sin(lon)
            print("X: ", x, "Y: ", y)
            print("Qual: ", GPGGA.gps_qual, "Num sats: ", GPGGA.num_sats)

client.close()
