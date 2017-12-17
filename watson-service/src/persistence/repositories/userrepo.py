"""userrepo.py"""
from persistence.models import User

class UserRepo():
    """UserRepo definition"""

    def __init__(self, database):
        self.database = database

    # Default

    def get_all(self):
        """Get all users."""
        return User.select().execute()

    def get_byid(self, identifier):
        """Get a user by id."""
        try:
            return User.get(User.id == identifier)
        except User.DoesNotExist:
            return None

    def create(self, subject):
        """Creates a new user."""
        user = User()
        user.subject = subject

        user.save()
        return user

    # Specific

    def get_bysubject(self, subject):
        """Get a user by subject."""
        try:
            return User.get(User.subject == subject)
        except User.DoesNotExist:
            return self.create(subject)
