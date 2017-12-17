"""profilerepo.py"""
from persistence.models import Profile

class ProfileRepo():
    """ProfileRepo definition"""

    def __init__(self, database):
        self.database = database

    # Default

    def get_all(self):
        """Get all profiles."""
        return Profile.select().execute()

    def get_byid(self, identifier):
        """Get a profile by id."""
        try:
            return Profile.get(Profile.id == identifier)
        except Profile.DoesNotExist:
            return None

    def create(self, user, concepts):
        """Creates a new profile."""

        profile = Profile()
        profile.user = user
        profile.date = concepts['date']
        profile.location = concepts['location']
        profile.profession = concepts['profession']
        profile.people = concepts['people']
        profile.technique = concepts['technique']
        profile.story = concepts['story']
        profile.value = concepts['value']
        profile.zeitgeist = concepts['zeitgeist']
        profile.animals = concepts['animals']
        profile.architecture = concepts['architecture']
        profile.clothing = concepts['clothing']

        profile.save()
        return profile

    # Specific

    # ...
