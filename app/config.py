import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key")
    DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///todo.db")
    DEBUG = os.environ.get("DEBUG", True)