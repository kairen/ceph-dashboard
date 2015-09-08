from django.db import models

# Create your models here.

from ceph_rest_client.wrapper import CephWrapper

class ModelsData:

    def __init__(self):
        self.rest_client = CephWrapper(
            endpoint='http://localhost:8000/api/v1/',
            debug=False
        )

    def fsid(self):
        response = self.rest_client.fsid(body='json')
        return response[1]

    def status(self):
        response = self.rest_client.status(body='json')
        return response[1]

    def health(self):
        response = self.rest_client.health(body='json')
        return response[1]["summary"]