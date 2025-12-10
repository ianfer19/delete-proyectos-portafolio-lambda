import time
from repositories.project_repository import ProjectRepository


class ProjectService:
    @staticmethod
    def delete_project(payload: dict):
        """
        Elimina un proyecto.
        """
        project_id = payload.get("projectId")
        if not project_id:
            raise ValueError("El project_id es obligatorio.")

        project_name = payload.get("name")
        if not project_name:
            raise ValueError("El nombre (name) es obligatorio porque es parte de la llave primaria.")

        # Llamar al repositorio
        delete_item = ProjectRepository.delete_project(project_id, project_name)
        return delete_item
