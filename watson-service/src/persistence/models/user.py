"""user.py"""
from persistence.models import BaseModel
from peewee import CharField, ForeignKeyField

class User(BaseModel):
    """User definition"""

    subject = CharField(unique=True, null=False)

    def as_dict(self):
        """Convert current instance to dictionary."""
        c_timestamp = self.creation_timestamp
        m_timestamp = self.modification_timestamp

        return {
            'id': self.get_id(),
            'subject': self.subject,
            'creation_timestamp': c_timestamp,
            'modification_timestamp': m_timestamp
        }
