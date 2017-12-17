"""__init__.py"""
from os import getenv
from json import loads

def get_storage_credentials(bluemix):
    """Returns the proper storage credentials based on environment."""

    if bluemix:
        vcap = loads(getenv('VCAP_SERVICES', '{}'))
        return vcap['cloud-object-storage'][0]['credentials']
    else:
        return {
            'apikey': '?',
            'endpoints': '?',
            'resource_instance_id': '?'
        }

BLUEMIX = bool(getenv('BLUEMIX', ''))
STORAGE_CREDENTIALS = get_storage_credentials(BLUEMIX)

# pylint: disable=C0413
from services.bluemix import StorageClient
from services.watson import PaintingClassifier

# Create service singletons
STORAGE_CLIENT = StorageClient(STORAGE_CREDENTIALS)
PAINTING_CLASSIFIER = PaintingClassifier('?')
