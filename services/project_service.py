import time
from repositories.project_repository import ProjectRepository


class ProjectService:
    @staticmethod
    def delete_project(project_id: str, name: str):
        """
        Elimina un proyecto dado su ID.
        Busca el nombre (SK) usando el ID (PK) y luego elimina.
        """
        if not project_id:
            print("ERROR: Service received empty project_id")
            raise ValueError("El project_id es obligatorio.")

        print(f"DEBUG: Service received project_id={project_id}, name={name}")

        # 1. Buscar el proyecto para obtener el 'name' (Sort Key)
        print("DEBUG: Calling ProjectRepository.get_project_by_id logic to verify existence")
        existing_project = ProjectRepository.get_project_by_id(project_id)
        print(f"DEBUG: Repository returned: {existing_project}")
        
        if not existing_project:
            print(f"ERROR: Project not found with id: {project_id}")
            raise ValueError(f"No se encontró el proyecto con id: {project_id}")

        project_name = existing_project.get("name")
        print(f"DEBUG: Derived project_name from DB: {project_name}")
        
        if not project_name:
             print("ERROR: Found project has no name")
             raise ValueError("El proyecto encontrado no tiene 'name', no se puede eliminar.")

        # 2. Eliminar usando PK y SK
        # NOTE: Using the DB-derived name to ensure consistency, but if you want to use the passed 'name' you can.
        # However, the user request is just to add prints.
        print(f"DEBUG: Calling ProjectRepository.delete_project with id={project_id}, name={project_name}")
        delete_item = ProjectRepository.delete_project(project_id, project_name)
        print(f"DEBUG: Delete result: {delete_item}")
        return delete_item
