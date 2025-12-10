import boto3
import os
from botocore.exceptions import ClientError


class ProjectRepository:
    _dynamodb = boto3.resource('dynamodb')
    _table_name = os.environ.get('iam-portafolio-projects-pdn', 'iam-portafolio-projects-pdn')  # Default or env var
    _table = _dynamodb.Table(_table_name)

    @classmethod
    def delete_project(cls, project_id, project_name):
        """
        Elimina un proyecto existente en DynamoDB.
        Construye dinamicamente la UpdateExpression basada en los campos proporcionados.
        """
        print(f"DEBUG: Repository.delete_project called with id={project_id}, name={project_name}")

        try:
            response = cls._table.delete_item(
                Key={
                    "projectId": project_id,
                    "name": project_name
                },
                ReturnValues="ALL_OLD"
            )
            print(f"DEBUG: DynamoDB delete response: {response}")
            return response.get('Attributes')
        except ClientError as e:
            print(f"Error deleting item: {e}")
            raise e

    @classmethod
    def get_project_by_id(cls, project_id):
        """
        Obtiene un proyecto por su projectId.
        Dado que solo tenemos la PK, hacemos una Query.
        """
        print(f"DEBUG: Repository.get_project_by_id called with id={project_id}")
        try:
            response = cls._table.query(
                KeyConditionExpression=boto3.dynamodb.conditions.Key('projectId').eq(project_id)
            )
            print(f"DEBUG: DynamoDB query response: {response}")
            items = response.get('Items', [])
            result = items[0] if items else None
            print(f"DEBUG: Repository found item: {result}")
            return result
        except ClientError as e:
            print(f"Error getting item: {e}")
            raise e
