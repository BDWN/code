"""factrepo.py"""
from persistence.models import Fact

class FactRepo():
    """FactRepo definition"""

    def __init__(self, database):
        self.database = database

    # Default

    def get_all(self):
        """Get all fact."""
        return Fact.select().execute()

    def get_byid(self, identifier):
        """Get a fact by id."""
        try:
            return Fact.get(Fact.id == identifier)
        except Fact.DoesNotExist:
            return None

    def create(self, painting, description):
        """Creates a new painting."""

        fact = Fact()
        fact.painting = painting
        fact.description = description

        fact.save()
        return fact

    # Specific

    # ...
