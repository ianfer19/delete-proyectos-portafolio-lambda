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
        
        if not name:
            print("ERROR: Service received empty name")
            raise ValueError("El project_name es obligatorio para la eliminación directa.")

        print(f"DEBUG: Service received project_id={project_id}, name={name}")

        # 2. Eliminar usando PK y SK directamente
        print(f"DEBUG: Calling ProjectRepository.delete_project directly with id={project_id}, name={name}")
        delete_item = ProjectRepository.delete_project(project_id, name)
        print(f"DEBUG: Delete result: {delete_item}")
        return delete_item
