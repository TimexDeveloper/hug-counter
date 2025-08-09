from http.server import BaseHTTPRequestHandler
import json

# Глобальная переменная для хранения состояния
COUNTER = 0

def handler(request, response):
    class HugHandler(BaseHTTPRequestHandler):
        def _set_headers(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
        
        def do_GET(self):
            self._set_headers()
            self.wfile.write(json.dumps({'count': COUNTER}).encode())
        
        def do_POST(self):
            global COUNTER
            COUNTER += 1
            self._set_headers()
            self.wfile.write(json.dumps({'count': COUNTER}).encode())

    h = HugHandler(request, response, None)
    if request.method == 'GET':
        h.do_GET()
    elif request.method == 'POST':
        h.do_POST()
    
    return response