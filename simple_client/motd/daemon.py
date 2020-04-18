#!/usr/bin/env python3

import http.server
import socketserver

import threading
#from motd import make_page
from motd import make_page

handler = http.server.SimpleHTTPRequestHandler

def update_motd():
	motd.make_page('data.ko')
	print("index.html updated")

with socketserver.TCPServer(('', 10001), handler) as httpd:
	threading.Timer(10.0, update_motd).start()
	print('Server listening on port 10001...')
	httpd.serve_forever()

