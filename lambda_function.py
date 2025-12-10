import json
from services.project_service import ProjectService
from utils import http_responses

def lambda_handler(event, context):
    """
    Handler principal para la Lambda de actualización de proyectos.
    """
    print(f"Received event: {json.dumps(event)}")

    try:
        # Obtener projectId de pathParameters o del body
        project_id = None
        if event.get('pathParameters') and event['pathParameters'].get('id'):
            project_id = event['pathParameters']['id']
        
        # Parsear body
        body = {}
        if event.get('body'):
            if isinstance(event['body'], str):
                body = json.loads(event['body'])
            else:
                body = event['body']

        # Si no vino en pathParameters, intentar sacarlo del body
        if not project_id:
            project_id = body.get('projectId')

        if not project_id:
            return http_responses.bad_request("Falta el projectId (en pathParameters o body).")

        # Llamar al servicio
        deleted_project = ProjectService.delete_project(body)

        return http_responses.success(deleted_project)

    except ValueError as ve:
        print(f"Validation error: {ve}")
        return http_responses.bad_request(str(ve))
    except Exception as e:
        print(f"Internal error: {e}")
        return http_responses.internal_server_error("Error interno del servidor.")
