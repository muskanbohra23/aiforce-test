from app.repositories.task_repository import TaskRepository
from app.models.task import Task
from app.errors import APIError

class TaskService:
    @staticmethod
    def list_tasks():
        return [task.to_dict() for task in TaskRepository.get_all()]

    @staticmethod
    def get_task(task_id):
        task = TaskRepository.get_by_id(task_id)
        if not task:
            raise APIError("Task not found", 404)
        return task.to_dict()

    @staticmethod
    def create_task(data):
        if "title" not in data or not data["title"]:
            raise APIError("Title is required", 400)
        new_task = Task(
            title=data["title"],
            description=data.get("description", ""),
            status=data.get("status", "pending")
        )
        TaskRepository.create(new_task)
        return new_task.to_dict()

    @staticmethod
    def update_task(task_id, data):
        task = TaskRepository.get_by_id(task_id)
        if not task:
            raise APIError("Task not found", 404)
        if "title" in data:
            task.title = data["title"]
        if "description" in data:
            task.description = data["description"]
        if "status" in data:
            task.status = data["status"]
        TaskRepository.update()
        return task.to_dict()

    @staticmethod
    def delete_task(task_id):
        task = TaskRepository.get_by_id(task_id)
        if not task:
            raise APIError("Task not found", 404)
        TaskRepository.delete(task)
        return {"message": "Task deleted successfully"}