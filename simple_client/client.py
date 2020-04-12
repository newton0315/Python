# client.py

import socket

HOST, PORT = '192.168.0.101', 1400

s = socket.socket(

            socket.AF_INET,     #           ADDRESS FAMILIES
                                #Name                   Purpose
                                #AF_UNIX, AF_LOCAL      Local communication
                                #AF_INET                IPv4 Internet protocols
                                #AF_INET6               IPv6 Internet protocols
                                #AF_APPLETALK           Appletalk
                                #AF_BLUETOOTH           Bluetooth


            socket.SOCK_STREAM  #           SOCKET TYPES
                                #Name           Way of Interaction
                                #SOCK_STREAM    TCP
                                #SOCK_DGRAM     UDP
)
s.connect((HOST, PORT))

while True:
	message = input("Any string (<1024 bytes): ")
	if message == 'Q' or message == 'q':
		print("Closing connection. Bye~")
		break;
	s.send(message.encode('utf-8'))#in UDP use sendto()
	data = s.recv(1024)#in UDP use recvfrom()
	print(repr(data.decode('utf-8')))

s.close()#end the connection
