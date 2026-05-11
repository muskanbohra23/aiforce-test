from flask import Flask
from app.config import Config
from app.routes.task_routes import task_bp
from app.errors import register_error_handlers
from app.logging_config import configure_logging
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    configure_logging()
    logging.info("Starting To-do List Management API")

    # Register Blueprints
    app.register_blueprint(task_bp, url_prefix="/api/tasks")

    # Register Error Handlers
    register_error_handlers(app)

    return app