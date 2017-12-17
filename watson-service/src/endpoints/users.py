"""users.py"""
from endpoints import APP, RESPONSES
from endpoints.decorators import requires_auth
from flask import jsonify, _app_ctx_stack
from persistence import USER_REPO

@APP.route('/api/users')
def get_users():
    """Returns all users as JSON."""
    users = USER_REPO.get_all()
    return jsonify([u.as_dict() for u in users])

@APP.route('/api/user/<identifier>')
def get_user_byid(identifier):
    """Returns a single user (by identifier) as JSON."""
    user = USER_REPO.get_byid(identifier)
    if user is None:
        return RESPONSES['not_found']('User {0} not found,'.format(identifier))

    return jsonify(user.as_dict())

@APP.route('/api/user/current')
@requires_auth
def get_user_current():
    """Returns the current user as JSON."""
    subject = _app_ctx_stack.top.current_user['sub']
    user = USER_REPO.get_bysubject(subject)
    if user is None:
        return RESPONSES['not_found']('User {0} not found.'.format(subject))

    return jsonify(user.as_dict())
