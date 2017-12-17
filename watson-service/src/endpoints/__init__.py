"""__init__.py"""
from endpoints.auxiliaries import RESPONSES
from flask import Flask
from flask_cors import CORS

APP = Flask(__name__, static_folder='../static')
CORS(APP)

# pylint: disable=C0413
# pylint: disable=C0412
import endpoints.comments
import endpoints.facts
import endpoints.paintings
import endpoints.persons
import endpoints.posts
import endpoints.users
import endpoints.profiles
