"""commentrepo.py"""
from persistence.models import Comment

class CommentRepo():
    """CommentRepo definition"""

    def __init__(self, database):
        self.database = database

    # Default

    def get_all(self):
        """Get all comments."""
        return Comment.select().execute()

    def get_byid(self, identifier):
        """Get a comment by id."""
        try:
            return Comment.get(Comment.id == identifier)
        except Comment.DoesNotExist:
            return None

    def create(self, post, fact, person):
        """Creates a new comment."""

        comment = Comment()
        comment.post = post
        comment.fact = fact
        comment.person = person

        comment.save()
        return comment

    # Specific

    # ...
