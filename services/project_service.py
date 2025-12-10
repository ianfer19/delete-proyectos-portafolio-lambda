import time
from repositories.project_repository import ProjectRepository


class ProjectService:
    @staticmethod
    def delete_project(project_id: str):
        """
        Elimina un proyecto dado su ID.
        Busca el nombre (SK) usando el ID (PK) y luego elimina.
        """
        if not project_id:
            raise ValueError("El project_id es obligatorio.")

        # 1. Buscar el proyecto para obtener el 'name' (Sort Key)
        existing_project = ProjectRepository.get_project_by_id(project_id)
        if not existing_project:
            raise ValueError(f"No se encontró el proyecto con id: {project_id}")

        project_name = existing_project.get("name")
        if not project_name:
             raise ValueError("El proyecto encontrado no tiene 'name', no se puede eliminar.")

        # 2. Eliminar usando PK y SK
        delete_item = ProjectRepository.delete_project(project_id, project_name)
        return delete_item
