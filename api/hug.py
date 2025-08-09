from http.server import BaseHTTPRequestHandler
import json

# Глобальная переменная для хранения состояния
COUNTER = 0

def handler(request, response):
    # Устанавливаем заголовки
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    # Глобальная переменная для счетчика (временное решение)
    global count
    try:
        count
    except NameError:
        count = 0
    
    # Обработка GET-запроса
    if request.method == 'GET':
        response.body = f'{{"count": {count}}}'.encode()
        return response
    
    # Обработка POST-запроса
    if request.method == 'POST':
        count += 1
        response.body = f'{{"count": {count}}}'.encode()
        return response
    
    # Для других методов
    response.status = 405
    response.body = b'Method Not Allowed'
    return response