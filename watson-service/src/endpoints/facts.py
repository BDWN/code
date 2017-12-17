"""facts.py"""
from endpoints import APP, RESPONSES
from flask import jsonify, request
from persistence import FACT_REPO, PAINTING_REPO

@APP.route('/api/facts')
def get_facts():
    """Returns all facts as JSON."""
    facts = FACT_REPO.get_all()
    return jsonify([f.as_dict() for f in facts])

@APP.route('/api/fact/<identifier>')
def get_fact_byid(identifier):
    """Returns a single fact (by identifier) as JSON."""
    fact = FACT_REPO.get_byid(identifier)
    if fact is None:
        return RESPONSES['not_found']('Fact {0} not found,'.format(identifier))

    return jsonify(fact.as_dict())

@APP.route('/api/fact', methods=['POST'])
def create_fact():
    """Creates a new fact."""
    description = request.form.get('description')
    painting_id = request.form.get('painting')
    if painting_id:
        painting = PAINTING_REPO.get_byid(painting_id)
        if not painting:
            return RESPONSES['bad_request']('No valid painting ID in payload.')

    fact = FACT_REPO.create(painting, description)
    return RESPONSES['created']('Fact created.', fact.as_dict())
    