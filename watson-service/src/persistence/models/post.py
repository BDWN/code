"""post.py"""
from persistence.models import BaseModel, User, Painting
from peewee import CharField, ForeignKeyField

class Post(BaseModel):
    """Post definition"""

    user = ForeignKeyField(User, related_name='posts')
    painting = ForeignKeyField(Painting, related_name='posts')
    description = CharField(unique=False, null=True)
    photo = CharField(unique=True, null=False)

    def as_dict(self):
        """Convert current instance to dictionary."""
        c_timestamp = self.creation_timestamp
        m_timestamp = self.modification_timestamp

        return {
            'id': self.get_id(),
            'user_id': self.user_id,
            'painting_id': self.painting_id,
            'description': self.description,
            'photo': self.photo,
            'creation_timestamp': c_timestamp,
            'modification_timestamp': m_timestamp
        }
