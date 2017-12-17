"""personrepo.py"""
from persistence.models import Person

class PersonRepo():
    """PersonRepo definition"""

    def __init__(self, database):
        self.database = database

    # Default

    def get_all(self):
        """Get all person."""
        return Person.select().execute()

    def get_byid(self, identifier):
        """Get a person by id."""
        try:
            return Person.get(Person.id == identifier)
        except Person.DoesNotExist:
            return None

    def create(self, name, photo):
        """Creates a new person."""

        person = Person()
        person.name = name
        person.photo = photo

        person.save()
        return person

    # Specific

    # ...
