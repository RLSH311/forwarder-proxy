from setuptools import setup

version: str = '1.0.0'

setup(
    name='forwarder_proxy',
    version=version,
    packages=['forwarder_proxy'],
    url='',
    license='',
    author='Harel Shimon',
    author_email='harel.shimon99@gmail.com',
    description='forwarder proxy',
    install_requires=[
        'flask',
        'flask_restful',
        'flask_api'
    ]
)
