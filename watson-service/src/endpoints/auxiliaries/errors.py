"""errors.py"""
from endpoints import APP
from flask import jsonify

class AuthError(Exception):
    """AuthError definition"""

    def __init__(self, error, status_code):
        super(AuthError, self).__init__('AuthError exception')
        self.error = error
        self.status_code = status_code

@APP.errorhandler(AuthError)
def handle_auth_error(ex):
    """Handles a AuthError exception"""
    response = jsonify(ex.error)
    response.status_code = ex.status_code

    return response
