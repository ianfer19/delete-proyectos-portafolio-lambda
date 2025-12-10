import json

def build_response(status_code, body):
    """
    Genera una respuesta HTTP estandarizada con cabeceras CORS.
    """
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",  # Permitir todos los orígenes (ajustar según necesidad)
            "Access-Control-Allow-Methods": "OPTIONS, POST, PUT, GET, DELETE",
            "Access-Control-Allow-Headers": "Content-Type, Authorization"
        },
        "body": json.dumps(body)
    }

def success(data):
    return build_response(200, data)

def bad_request(message):
    return build_response(400, {"error": message})

def not_found(message):
    return build_response(404, {"error": message})

def internal_server_error(message):
    return build_response(500, {"error": message})
