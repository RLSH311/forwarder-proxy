from flask import Flask
from forwarder_proxy.config import get_configuration
from forwarder_proxy.views import api


def create_app(config_name: str) -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(get_configuration(config_name))

    api.init_app(app)

    return app
