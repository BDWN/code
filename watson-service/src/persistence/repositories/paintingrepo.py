"""paintingrepo.py"""
from persistence.models import Painting

class PaintingRepo():
    """PaintingRepo definition"""

    def __init__(self, database):
        self.database = database

    # Default

    def get_all(self):
        """Get all paintings."""
        return Painting.select().execute()

    def get_byid(self, identifier):
        """Get a painting by id."""
        try:
            return Painting.get(Painting.id == identifier)
        except Painting.DoesNotExist:
            return None

    def get_bywikidata(self, wikidata_id):
        """Get a painting by wikidata id."""
        try:
            return Painting.get(Painting.wikidata == wikidata_id)
        except Painting.DoesNotExist:
            return None

    def create(self, name, wikidata, person):
        """Creates a new painting."""

        painting = Painting()
        painting.name = name
        painting.wikidata = wikidata
        painting.person = person

        painting.save()
        return painting

    # Specific

    # ...
