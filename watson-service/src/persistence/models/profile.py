"""profile.py"""
from persistence.models import BaseModel, User
from peewee import BooleanField, ForeignKeyField

class Profile(BaseModel):
    """Profile definition"""

    user = ForeignKeyField(User, related_name='profile')
    date = BooleanField(null=False, default=False)
    location = BooleanField(null=False, default=False)
    profession = BooleanField(null=False, default=False)
    people = BooleanField(null=False, default=False)
    technique = BooleanField(null=False, default=False)
    story = BooleanField(null=False, default=False)
    value = BooleanField(null=False, default=False)
    zeitgeist = BooleanField(null=False, default=False)
    animals = BooleanField(null=False, default=False)
    architecture = BooleanField(null=False, default=False)
    clothing = BooleanField(null=False, default=False)

    def as_dict(self):
        """Convert current instance to dictionary."""
        c_timestamp = self.creation_timestamp
        m_timestamp = self.modification_timestamp

        return {
            'id': self.get_id(),
            'user': self.user_id,
            'date': self.date,
            'location': self.location,
            'profession': self.profession,
            'people': self.people,
            'technique': self.technique,
            'story': self.story,
            'value': self.value,
            'zeitgeist': self.zeitgeist,
            'animals': self.animals,
            'architecture': self.architecture,
            'clothing': self.clothing,
            'creation_timestamp': c_timestamp,
            'modification_timestamp': m_timestamp
        }


        return {
            'date': False,
            'location': False,
            'profession': False,
            'people': False,
            'technique': False,
            'story': False,
            'value': False,
            'zeitgeist': False,
            'animals': False,
            'architecture': False,
            'clothing': False
        }