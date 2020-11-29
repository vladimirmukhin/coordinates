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
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        print(f"x-request-id      : {self.headers['x-request-id']}")
        print(f"x-b3-traceid      : {self.headers['x-b3-traceid']}")
        print(f"x-b3-spanid       : {self.headers['x-b3-spanid']}")
        print(f"x-b3-parentspanid : {self.headers['x-b3-parentspanid']}")
        print(f"x-b3-sampled      : {self.headers['x-b3-sampled']}")
        print(f"x-b3-flags        : {self.headers['x-b3-flags']}")
        print(f"b3                : {self.headers['b3']}")

        
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