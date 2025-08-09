from http.server import BaseHTTPRequestHandler
import json

# Глобальная переменная (сбросится при перезапуске сервера)
hug_count = 0

class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        global hug_count
        self._set_headers()
        self.wfile.write(json.dumps({"count": hug_count}).encode())

    def do_POST(self):
        global hug_count
        hug_count += 1
        self._set_headers()
        self.wfile.write(json.dumps({"count": hug_count}).encode())

# Для Vercel Serverless
def handler(request, response):
    h = Handler(request, {}, None)
    if request.method == 'GET':
        h.do_GET()
    elif request.method == 'POST':
        h.do_POST()
    return response