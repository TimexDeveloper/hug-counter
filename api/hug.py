from http.server import BaseHTTPRequestHandler
import json

def handler(request, response):
    class HugHandler(BaseHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _set_headers(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

        def do_GET(self):
            self._set_headers()
            self.wfile.write(json.dumps({'count': 0}).encode())

        def do_POST(self):
            self._set_headers()
            self.wfile.write(json.dumps({'count': 1}).encode())

    h = HugHandler(request, response, None)
    if request.method == 'GET':
        h.do_GET()
    elif request.method == 'POST':
        h.do_POST()
    
    return response