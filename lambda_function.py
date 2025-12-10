import json
from services.project_service import ProjectService
from utils import http_responses

def lambda_handler(event, context):
    """
    Handler principal para la Lambda de actualización de proyectos.
    """
    print(f"Received event: {json.dumps(event)}")

    try:
        # Obtener projectId de pathParameters
        # API Gateway: /proyectos/{ProjectId}
        project_id = None
        if event.get('pathParameters') and event['pathParameters'].get('ProjectId'):
            project_id = event['pathParameters']['ProjectId']
        
        # Fallback: intentar por si viene como parameter lowercase o en el body (menos probable en DELETE standard)
        if not project_id and event.get('pathParameters') and event['pathParameters'].get('id'):
            project_id = event['pathParameters']['id']

        if not project_id:
            # Intento desesperado de buscar en body si pathParameters fallo
            if event.get('body'):
                 try:
                    body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']
                    project_id = body.get('projectId')
                 except:
                     pass

        if not project_id:
            return http_responses.bad_request("Falta el ProjectId en pathParameters.")

        # Llamar al servicio
        deleted_project = ProjectService.delete_project(project_id)

        return http_responses.success(deleted_project)

    except ValueError as ve:
        print(f"Validation error: {ve}")
        return http_responses.bad_request(str(ve))
    except Exception as e:
        print(f"Internal error: {e}")
        return http_responses.internal_server_error("Error interno del servidor.")
