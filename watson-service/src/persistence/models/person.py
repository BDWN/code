"""commenter.py"""
from persistence.models import BaseModel
from peewee import CharField

class Person(BaseModel):
    """Person definition"""

    name = CharField(unique=False, null=False)
    photo = CharField(unique=False, null=False)

    def as_dict(self):
        """Convert current instance to dictionary."""
        c_timestamp = self.creation_timestamp
        m_timestamp = self.modification_timestamp

        return {
            'id': self.get_id(),
            'name': self.name,
            'photo': self.photo,
            'creation_timestamp': c_timestamp,
            'modification_timestamp': m_timestamp
        }
