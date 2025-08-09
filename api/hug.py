from http.server import BaseHTTPRequestHandler
import json
import os

counter = int(os.environ.get('HUG_COUNTER', '0'))

def handler(request, response):
    global counter
    
    # Обработка GET-запроса
    if request.method == "GET":
        response.status_code = 200
        response.headers["Content-Type"] = "application/json"
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.body = json.dumps({"count": counter}).encode()
        return response

    # Обработка POST-запроса
    if request.method == "POST":
        counter += 1
        os.environ['HUG_COUNTER'] = str(counter)
        
        response.status_code = 200
        response.headers["Content-Type"] = "application/json"
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.body = json.dumps({"count": counter}).encode()
        return response

    # Для других методов
    response.status_code = 405
    response.body = b'Method Not Allowed'
    return response