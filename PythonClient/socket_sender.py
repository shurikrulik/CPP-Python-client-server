import socket
import base64
port = 8888
client = socket.socket()
client.connect(('10.1.17.65', port))
prefix = b'\x00\x00\x00\x03'
while True:
    
    tosend = input()
    mymessage = b'rcv\x00\x00\x00\x20' + base64.b64encode(bytes(tosend, 'UTF-8'))
#    print(mymessage)
    a = client.send(prefix)
    a = client.send(mymessage)
       
client.close() 
