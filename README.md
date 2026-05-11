# To-do List Management API

## Overview
This project implements a Python-based RESTful API for managing a to-do list with CRUD operations using SQLite. It is built with Flask and follows a modular architecture.

## Architecture
- **API Layer**: `app/routes` — Handles HTTP requests and responses.
- **Domain Layer**: `app/services` — Contains business logic.
- **Persistence Layer**: `app/models` and `app/repositories` — ORM models and data access.
- **Config Module**: `app/config.py` — Environment-based configuration.
- **Logging Module**: `app/logging_config.py` — Structured logging.
- **Error Module**: `app/errors.py` — Centralized error handling.
- **Tests**: `tests/` — Unit tests for API endpoints.

## Mapping from User Stories
Each user story corresponds to an endpoint:
- Create Task → POST `/api/tasks/`
- View All Tasks → GET `/api/tasks/`
- View Single Task → GET `/api/tasks/<id>`
- Update Task → PUT `/api/tasks/<id>`
- Delete Task → DELETE `/api/tasks/<id>`
- Error Handling → Centralized in `app/errors.py`

## Running Locally
```bash
pip install -r requirements.txt
python run.py
```
API will be available at `http://localhost:5000/api/tasks`.

## Deployment
- Use environment variables for `DATABASE_URI` and `SECRET_KEY`.
- Deploy with a WSGI server like Gunicorn.
- Ensure logs directory is writable.

## Assumptions
- SQLite is used for simplicity; can be replaced with another DB.
- Basic validation is implemented; can be extended.