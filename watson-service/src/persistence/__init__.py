"""__init__.py"""
from os import getenv
from json import loads
from urllib.parse import urlparse
from peewee import PostgresqlDatabase, SqliteDatabase

def get_database(bluemix):
    """Returns the proper database instance based on environment."""
    if bluemix:
        vcap = loads(getenv('VCAP_SERVICES', '{}'))
        uri = urlparse(vcap['compose-for-postgresql'][0]['credentials']['uri'])

        user = uri.username
        password = uri.password
        database = uri.path[1:]
        host = uri.hostname
        port = uri.port

        return PostgresqlDatabase(database, user=user, password=password, host=host, port=port)
    else:
        return SqliteDatabase('watsonservice.db', threadlocals=True)

BLUEMIX = bool(getenv('BLUEMIX', ''))
DATABASE = get_database(BLUEMIX)

# pylint: disable=C0413
from persistence.repositories import UserRepo, PersonRepo
from persistence.repositories import PostRepo, CommentRepo
from persistence.repositories import PaintingRepo, FactRepo
from persistence.repositories import ProfileRepo

# Create repository singletons
USER_REPO = UserRepo(DATABASE)
PERSON_REPO = PersonRepo(DATABASE)
POST_REPO = PostRepo(DATABASE)
COMMENT_REPO = CommentRepo(DATABASE)
PAINTING_REPO = PaintingRepo(DATABASE)
FACT_REPO = FactRepo(DATABASE)
PROFILE_REPO = ProfileRepo(DATABASE)
