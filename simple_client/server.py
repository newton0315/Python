# server.py

import socket

HOST, PORT = '0.0.0.0', 1400

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#refer to client.py
s.bind((HOST, PORT))
s.listen(1)#listen for 1 connection

conn, addr = s.accept()#start the actual data flow

print('connected to:', addr)

while 1:
    data = conn.recv(1024).decode('utf-8')#receive 1024 bytes and decode using ascii
    if not data:
        break
    conn.send((data + ' [ addition by server ]').encode('utf-8'))

conn.close()
