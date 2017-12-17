"""postrepo.py"""
from persistence.models import Post

class PostRepo():
    """PostRepo definition"""

    def __init__(self, database):
        self.database = database

    # Default

    def get_all(self):
        """Get all posts."""
        return Post.select().execute()

    def get_byid(self, identifier):
        """Get a post by id."""
        try:
            return Post.get(Post.id == identifier)
        except Post.DoesNotExist:
            return None

    def create(self, user, painting, description, photo):
        """Creates a new post."""

        post = Post()
        post.user = user
        post.painting = painting
        post.description = description
        post.photo = photo

        post.save()
        return post

    # Specific

    # ...
