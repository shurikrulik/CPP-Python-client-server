import socket
import base64
port = 8888
client = socket.socket()
client.connect(('localhost', port))

key="cts"

while True:

	data = input()
	key_length = len(key)
	data_encoded = base64.b64encode(bytes(data, "UTF-8"))
	data_length = len(data_encoded)
	message = key_length.to_bytes(4, byteorder='big') + bytes(key, "UTF-8") + data_length.to_bytes(4, byteorder='big') + data_encoded
	client.send(message)
        
client.close()
