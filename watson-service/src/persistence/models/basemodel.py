"""basemodel.py"""
from datetime import datetime
from persistence import DATABASE
from peewee import Model, DateTimeField

class BaseModel(Model):
    """BaseModel definition"""

    creation_timestamp = DateTimeField(default=datetime.now)
    modification_timestamp = DateTimeField(default=datetime.now)

    class Meta:
        "BaseModel.Meta definition"

        database = DATABASE
