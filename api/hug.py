import json

# Глобальная переменная для счетчика
counter = 0

def handler(request, response):
    global counter
    
    # Устанавливаем заголовки
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"
    
    # Обработка GET-запроса
    if request.method == "GET":
        response.body = json.dumps({"count": counter}).encode()
        return response
    
    # Обработка POST-запроса
    if request.method == "POST":
        counter += 1
        response.body = json.dumps({"count": counter}).encode()
        return response
    
    # Для других методов
    response.status = 405
    response.body = json.dumps({"error": "Method not allowed"}).encode()
    return response