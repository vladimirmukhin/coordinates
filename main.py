import http.server
import socketserver
from random import randrange
import json

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json.dumps({'altitude': self.generateCoordinates('alt'), 'latitude': self.generateCoordinates('lat')}), 'utf-8'))

    def generateCoordinates(self, coordinate_type):
        if coordinate_type == 'alt':
            return randrange(-90,90)
        if coordinate_type == 'lat':
            return randrange(-180,180)


PORT = 8001

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()