import socket
import base64
port = 8888
client = socket.socket()
client.connect(('10.1.17.65', port))
data = (client.recv(4096))

while True:

	data = (client.recv(4096))
	if len(data) > 8:
		print(base64.b64decode(data[3:]))
#		print(data[3:])
    
client.close() 
