import http.server
import socketserver

with open('data.txt', 'r') as f:
	line = f.readline()

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', 10001), handler) as httpd:
	print('Server listening on port 10001...')
	httpd.serve_forever()
