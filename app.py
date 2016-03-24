"""
This script runs the application using a development server.
"""

import bottle
import os
import sys
import bottle_mysql

# controllers package contains all the HTTP handlers for our server and must be imported.
from controllers import *

app = bottle.Bottle()
plugin = bottle_mysql.Plugin(dbuser='admin', dbpass='changeme', dbname='test')
app.install(plugin)


if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    bottle.debug(True)


def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published."""
    return bottle.default_app()

if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('PORT', '8080'))
    except ValueError:
        PORT = 5555

    @bottle.route('/static/<filepath:path>')
    def server_static(filepath):
        """Handler for static files, used with the development server.
        When running under a production server such as IIS or Apache,
        the server should be configured to serve the static files."""
        return bottle.static_file(filepath, root=STATIC_ROOT)

    # Starts a local test server.
    bottle.run(server='wsgiref', host='0.0.0.0', port=PORT)
