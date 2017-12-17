"""persons.py"""
from endpoints import APP, RESPONSES
from flask import jsonify, request
from persistence import PERSON_REPO

@APP.route('/api/persons')
def get_persons():
    """Returns all persons as JSON."""
    persons = PERSON_REPO.get_all()
    return jsonify([p.as_dict() for p in persons])

@APP.route('/api/person/<identifier>')
def get_person_byid(identifier):
    """Returns a single person (by identifier) as JSON."""
    person = PERSON_REPO.get_byid(identifier)
    if person is None:
        return RESPONSES['not_found']('Person {0} not found,'.format(identifier))

    return jsonify(person.as_dict())

@APP.route('/api/person', methods=['POST'])
def create_person():
    """Creates a new person."""
    name = request.form.get('name')
    photo = request.form.get('photo')

    person = PERSON_REPO.create(name, photo)
    return RESPONSES['created']('Personperson created.', person.as_dict())
    