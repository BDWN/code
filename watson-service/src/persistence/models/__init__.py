"""__init__.py"""
from persistence.models.basemodel import BaseModel
from persistence.models.person import Person
from persistence.models.painting import Painting
from persistence.models.user import User
from persistence.models.profile import Profile
from persistence.models.post import Post
from persistence.models.fact import Fact
from persistence.models.comment import Comment

MODEL_LIST = [Person, Painting, User, Profile, Post, Fact, Comment]
