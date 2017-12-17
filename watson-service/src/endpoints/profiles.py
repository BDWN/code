"""profiles.py"""
from json import loads
from endpoints import APP, RESPONSES
from flask import jsonify, request
from persistence import USER_REPO, PROFILE_REPO

@APP.route('/api/profiles')
def get_profiles():
    """Returns all profiles as JSON."""
    profiles = PROFILE_REPO.get_all()
    return jsonify([p.as_dict() for p in profiles])

@APP.route('/api/profile/<identifier>')
def get_profile_byid(identifier):
    """Returns a single profile (by identifier) as JSON."""
    profile = PROFILE_REPO.get_byid(identifier)
    if profile is None:
        return RESPONSES['not_found']('Profile {0} not found,'.format(identifier))

    return jsonify(profile.as_dict())

@APP.route('/api/profile', methods=['POST'])
def create_profile():
    """Creates a new profile."""
    user_id = request.form.get('user')
    concepts = request.form.get('concepts')

    if concepts is None:
        return RESPONSES['bad_request']('No valid concepts array in payload.')

    user = USER_REPO.get_byid(user_id)
    if user is None:
        return RESPONSES['bad_request']('No valid user ID in payload.')

    profile = PROFILE_REPO.create(user, loads(concepts))
    return RESPONSES['created']('Profile created.', profile.as_dict())
