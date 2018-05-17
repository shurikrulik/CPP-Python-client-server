import socket

import base64

port = 8888

client = socket.socket()

client.connect(('10.1.17.65', port))

while True:

    tosend = input()

    a = client.send(((bytes("\x00\x00\x00\x03cts\x00\x00\x00\x20", "utf-8") + base64.b64encode(bytes(tosend, "UTF-8")))))



client.close()

