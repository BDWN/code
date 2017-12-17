"""painting.py"""
from persistence.models import BaseModel, Person
from peewee import CharField, ForeignKeyField

class Painting(BaseModel):
    """Painting definition"""

    name = CharField(unique=False, null=False)
    wikidata = CharField(unique=True, null=False)
    person = ForeignKeyField(Person, related_name='paintings')

    def as_dict(self):
        """Convert current instance to dictionary."""
        c_timestamp = self.creation_timestamp
        m_timestamp = self.modification_timestamp

        return {
            'id': self.get_id(),
            'name': self.name,
            'wikidata': self.wikidata,
            'person_id': self.person_id,
            'creation_timestamp': c_timestamp,
            'modification_timestamp': m_timestamp
        }
