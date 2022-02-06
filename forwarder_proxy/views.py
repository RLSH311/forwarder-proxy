from flask_restful import Api

from forwarder_proxy.resources.index import IndexApi

api: Api = Api()

api.add_resource(IndexApi, '/')
