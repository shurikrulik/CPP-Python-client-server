import socket
import base64


port = 8888
client = socket.socket()
client.connect(('localhost', port))

stage = 1
key_size = 0
msg_size = 0
key = ''
msg = ''
expected_key = b'cts'

while True:

        data = client.recv(4096)
        if data != b'':
            while len(data) > 0:
                if stage == 1: 
                    key_size = int.from_bytes(data[:4], 'big')
                    data = data[4:]
                    stage = 2
                if stage == 2 and data != b'':
                    key = data[:key_size]
                    data = data[key_size:]
                    stage = 3
                if stage == 3 and data != b'':
                    msg_size = int.from_bytes(data[:4], 'big')
                    data = data[4:]
                    stage = 4
                if stage == 4 and data != b'':
                    msg = data
                    stage = 1
                    data = b''
                    if key == expected_key and msg_size!=0:
                        print(base64.b64decode(msg))
                elif data == b'' and stage == 4:
                    stage = 1

client.close()
