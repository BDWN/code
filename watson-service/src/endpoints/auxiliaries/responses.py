"""responses.py"""
from flask import jsonify

def created(message='', entity=None):
    """Returns a 201 response."""
    response = jsonify({'status': 201, 'message': message, 'entity': entity})
    response.status_code = 201

    return response

def bad_request(message=''):
    """Returns a 400 error response."""
    response = jsonify({'status': 400, 'message': message})
    response.status_code = 400

    return response

def not_found(message=''):
    """Returns a 404 error response."""
    response = jsonify({'status': 404, 'message': message})
    response.status_code = 404

    return response

def internal_server_error(message=''):
    """Returns a 500 error response."""
    response = jsonify({'status': 500, 'message': message})
    response.status_code = 500

    return response

def not_implemented(message=''):
    """Returns a 501 error response."""
    response = jsonify({'status': 501, 'message': message})
    response.status_code = 501

    return response

RESPONSES = {
    'created': created,
    'not_found': not_found,
    'bad_request': bad_request,
    'internal_server_error': internal_server_error,
    'not_implemented': not_implemented
}
