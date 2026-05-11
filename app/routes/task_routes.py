from flask import Blueprint, request, jsonify
from app.services.task_service import TaskService

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/", methods=["GET"])
def list_tasks():
    return jsonify(TaskService.list_tasks())

@task_bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    return jsonify(TaskService.get_task(task_id))

@task_bp.route("/", methods=["POST"])
def create_task():
    data = request.get_json()
    return jsonify(TaskService.create_task(data)), 201

@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    return jsonify(TaskService.update_task(task_id, data))

@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    return jsonify(TaskService.delete_task(task_id))