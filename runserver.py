"""
Run the DEV server
"""

from os import environ
from example import APP

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    APP.run(HOST, PORT)
