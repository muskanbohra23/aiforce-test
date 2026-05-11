from flask import jsonify

class APIError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

def register_error_handlers(app):
    @app.errorhandler(APIError)
    def handle_api_error(error):
        response = jsonify({"error": error.message})
        response.status_code = error.status_code
        return response

    @app.errorhandler(404)
    def handle_not_found(error):
        response = jsonify({"error": "Resource not found"})
        response.status_code = 404
        return response

    @app.errorhandler(500)
    def handle_server_error(error):
        response = jsonify({"error": "Internal server error"})
        response.status_code = 500
        return response