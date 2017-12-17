"""fact.py"""
from persistence.models import BaseModel, Painting
from peewee import CharField, ForeignKeyField

class Fact(BaseModel):
    """Fact definition"""

    painting = ForeignKeyField(Painting, related_name='facts')
    description = CharField(unique=False, null=True)

    def as_dict(self):
        """Convert current instance to dictionary."""
        c_timestamp = self.creation_timestamp
        m_timestamp = self.modification_timestamp

        return {
            'id': self.get_id(),
            'painting_id': self.painting_id,
            'description': self.description,
            'creation_timestamp': c_timestamp,
            'modification_timestamp': m_timestamp
        }
