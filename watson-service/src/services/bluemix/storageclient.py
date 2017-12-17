"""storageclient.py"""
from os import path
from ibm_boto3 import client
from ibm_botocore.client import Config
from requests import get

class StorageClient:
    """StorageClient definition"""

    def __init__(self, credentials):
        credentials = credentials
        endpoints = get(credentials['endpoints']).json()

        iam_host = endpoints['identity-endpoints']['iam-token']
        cos_host = endpoints['service-endpoints']['cross-region']['eu']['public']['eu-geo']

        self.base_url = 'https://s3.ams-eu-geo.objectstorage.softlayer.net'
        self.cos = client(
            's3',
            ibm_api_key_id=credentials['apikey'],
            ibm_service_instance_id=credentials['resource_instance_id'],
            ibm_auth_endpoint="https://" + iam_host + "/oidc/token",
            config=Config(signature_version='oauth'),
            endpoint_url="https://" + cos_host
        )

    def get_objects(self, bucket):
        """Returns all buckets in a specific bucket."""
        response = self.cos.list_objects(Bucket=bucket)
        return [object['Key'] for object in response['Contents']]

    def set_object_access(self, acl, file, bucket):
        """Set access for a specific object."""
        self.cos.put_object_acl(ACL=acl, Bucket=bucket, Key=file)

    def store_object(self, file, bucket):
        """Store a object in a specific bucket."""
        name = path.basename(file)
        self.cos.upload_file(file, bucket, name)

    def get_url(self, bucket, file):
        """Returns a url for a specific object."""
        return '{0}/{1}/{2}'.format(self.base_url, bucket, file)
