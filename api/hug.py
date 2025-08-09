from http.server import BaseHTTPRequestHandler
import json

# Храним счетчик в памяти (для демо)
COUNTER = 0

class Handler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
    
    def do_GET(self):
        global COUNTER
        self._set_headers()
        self.wfile.write(json.dumps({'count': COUNTER}).encode())
    
    def do_POST(self):
        global COUNTER
        COUNTER += 1
        self._set_headers()
        self.wfile.write(json.dumps({'count': COUNTER}).encode())

def handler(request, response):
    h = Handler(request, response, None)
    if request.method == 'GET':
        h.do_GET()
    elif request.method == 'POST':
        h.do_POST()
    return response