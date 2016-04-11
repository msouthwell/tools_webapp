from bottle import route, view, request, response
from datetime import datetime

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        year=datetime.now().year)
