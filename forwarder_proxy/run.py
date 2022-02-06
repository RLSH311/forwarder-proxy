import os

from flask import Flask

from forwarder_proxy.factory import create_app


app: Flask = create_app(os.getenv('FLASK_CONFIG') or 'Default')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
