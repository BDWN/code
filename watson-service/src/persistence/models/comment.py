"""comment.py"""
from persistence.models import BaseModel, Post, Fact, Person
from peewee import ForeignKeyField

class Comment(BaseModel):
    """Comment definition"""

    post = ForeignKeyField(Post, related_name='comments')
    fact = ForeignKeyField(Fact, related_name='comments')
    person = ForeignKeyField(Person, related_name='comments')

    def as_dict(self):
        """Convert current instance to dictionary."""
        c_timestamp = self.creation_timestamp
        m_timestamp = self.modification_timestamp

        return {
            'id': self.get_id(),
            'post_id': self.post_id,
            'fact_id': self.fact_id,
            'person_id': self.person_id,
            'creation_timestamp': c_timestamp,
            'modification_timestamp': m_timestamp
        }
