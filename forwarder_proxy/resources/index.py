from flask_api import status
from flask_restful import Resource

from setup import version


class IndexApi(Resource):
    def get(self):
        service_information: dict = {
            'description': 'This is a forwarder proxy',
            'version': version
        }

        return service_information, status.HTTP_200_OK
