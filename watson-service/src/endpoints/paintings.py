"""paintings.py"""
from endpoints import APP, RESPONSES
from flask import jsonify, request
from persistence import PAINTING_REPO, PERSON_REPO

@APP.route('/api/paintings')
def get_paintings():
    """Returns all paintings as JSON."""
    paintings = PAINTING_REPO.get_all()
    return jsonify([p.as_dict() for p in paintings])

@APP.route('/api/painting/<identifier>')
def get_painting_byid(identifier):
    """Returns a single painting (by identifier) as JSON."""
    painting = PAINTING_REPO.get_byid(identifier)
    if painting is None:
        return RESPONSES['not_found']('Painting {0} not found,'.format(identifier))

    return jsonify(painting.as_dict())

@APP.route('/api/painting', methods=['POST'])
def create_painting():
    """Creates a new painting."""
    name = request.form.get('name')
    wikidata = request.form.get('wikidata')
    person_id = request.form.get('person')

    person = PERSON_REPO.get_byid(person_id)
    painting = PAINTING_REPO.create(name, wikidata, person)
    return RESPONSES['created']('Painting created.', painting.as_dict())
