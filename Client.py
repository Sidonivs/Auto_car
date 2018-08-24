#!/usr/bin/env python3

import socket

def my_send(item):
	TCP_IP = "192.168.0.112"
	TCP_PORT = 1234
	BUFFER_SIZE = 4096

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP,TCP_PORT))
	message = item.read(BUFFER_SIZE)
	while(message):
		s.send(message)
		message = item.read(BUFFER_SIZE)
	s.shutdown(socket.SHUT_WR)
	data = s.recv(BUFFER_SIZE)
	s.close()
	
	print("received data: ", data)

with open("/home/pi/Downloads/fish.jpeg", "rb") as image:
	my_send(image)
