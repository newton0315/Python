#!/usr/bin/env python3

import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', 10001), handler) as httpd:
	print('Server listening on port 10001...')
	httpd.serve_forever()
